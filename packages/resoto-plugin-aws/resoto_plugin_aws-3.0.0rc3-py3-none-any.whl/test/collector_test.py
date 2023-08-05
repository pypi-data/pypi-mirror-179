import json
import logging
import threading
from typing import Type

from _pytest.logging import LogCaptureFixture
from botocore.exceptions import ClientError
from networkx import DiGraph, is_directed_acyclic_graph

from resoto_plugin_aws.collector import AwsAccountCollector, all_resources, called_collect_apis
from resoto_plugin_aws.resource.base import AwsResource, AwsRegion, GraphBuilder
from resotolib.core.model_export import dataclasses_to_resotocore_model
from test import account_collector, builder, aws_client, aws_config, no_feedback  # noqa: F401
from test.resources import BotoErrorSession


def test_collect(account_collector: AwsAccountCollector) -> None:
    account_collector.collect()

    def count_kind(clazz: Type[AwsResource]) -> int:
        count = 0
        for node in account_collector.graph.nodes:
            if isinstance(node, clazz):
                count += 1
        return count

    for resource in all_resources:
        assert count_kind(resource) > 0, "No instances of {} found".format(resource.__name__)

    # make sure all threads have been joined
    assert len(threading.enumerate()) == 1
    # ensure the correct number of nodes and edges
    assert count_kind(AwsResource) == 147
    assert len(account_collector.graph.edges) == 376


def test_dependencies() -> None:
    model = dataclasses_to_resotocore_model({AwsResource})

    def for_edge_type(edge_type: str) -> DiGraph:
        graph = DiGraph()
        for kind in model:
            if (successors := kind.get("successor_kinds")) and edge_type in successors:
                for successor in successors[edge_type]:
                    graph.add_edge(kind["fqn"], successor)
        return graph

    def show_graph(graph: DiGraph) -> str:
        result = "digraph {\n"
        for start, end in graph.edges:
            result += "  " + start + "->" + end + "\n"
        result += "}"
        return result

    assert is_directed_acyclic_graph(for_edge_type("default")), show_graph(for_edge_type("default"))
    assert is_directed_acyclic_graph(for_edge_type("delete")), show_graph(for_edge_type("delete"))


def test_collect_region(
    account_collector: AwsAccountCollector, builder: GraphBuilder, caplog: LogCaptureFixture
) -> None:
    account_collector.config.sessions().session_class_factory = BotoErrorSession(
        ClientError({"Error": {"Code": "UnauthorizedOperation"}}, "test")
    )

    with caplog.at_level(logging.ERROR):
        account_collector.collect_region(AwsRegion(id="us-east-1", name="us-east-1"), builder)
    assert (
        "Not authorized to collect aws_redshift_cluster resources"
        " in account 123 region us-east-1 - skipping resource"
    ) in caplog.text


def test_all_called_apis() -> None:
    allow = [api.action_string() for api in called_collect_apis()]
    allowed = ", ".join(f'"{a}"' for a in allow)
    statement = f"""{{
    "Version": "2012-10-17",
    "Statement": [
        {{
            "Sid": "AllowResotoAccess",
            "Effect": "Allow",
            "Action": [{allowed}],
            "Resource": "*"
        }}
    ]
    }}
    """
    assert json.loads(statement)
    assert len(allow) >= 74
    assert "s3:ListBuckets" in allow
