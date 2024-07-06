import pytest
import json
from src.parser.graph_json_parser import GraphJsonParser

@pytest.fixture
def setup_json_file(tmp_path):
    data = [
        {"resource_id": "organization1", "type": "organization", "ancestors": [], "bindings": []},
        {"resource_id": "folder1", "type": "folder", "ancestors": ["folder1", "organization1"], "bindings": []},
        {"resource_id": "folder2", "type": "folder", "ancestors": ["folder2", "organization1"], "bindings": []},
        {"resource_id": "folder3", "type": "folder", "ancestors": ["folder3", "folder1", "organization1"],
         "bindings": []},
        {"resource_id": "resource1", "type": "resource", "ancestors": ["resource1", "folder1", "organization1"],
         "bindings": [{"role": "owner", "members": ["user:alex@test.authomize.com"]}]},
        {"resource_id": "resource2", "type": "resource", "ancestors": ["resource2", "folder2", "organization1"],
         "bindings": [{"role": "editor", "members": ["user:alex@test.authomize.com"]},
                      {"role": "viewer", "members": ["user:ron@test.authomize.com"]}]}
    ]

    file_path = tmp_path / "example.jsonl"
    with open(file_path, 'w') as f:
        for line in data:
            f.write(f"{json.dumps(line)}\n")

    return file_path


def test_graph_json_parser(setup_json_file):
    parser = GraphJsonParser()
    parsed_data = list(parser.parse(setup_json_file))

    expected_data = [
        {"resource_id": "organization1", "type": "organization", "ancestors": [], "bindings": []},
        {"resource_id": "folder1", "type": "folder", "ancestors": ["folder1", "organization1"], "bindings": []},
        {"resource_id": "folder2", "type": "folder", "ancestors": ["folder2", "organization1"], "bindings": []},
        {"resource_id": "folder3", "type": "folder", "ancestors": ["folder3", "folder1", "organization1"],
         "bindings": []},
        {"resource_id": "resource1", "type": "resource", "ancestors": ["resource1", "folder1", "organization1"],
         "bindings": [{"role": "owner", "members": ["user:alex@test.authomize.com"]}]},
        {"resource_id": "resource2", "type": "resource", "ancestors": ["resource2", "folder2", "organization1"],
         "bindings": [{"role": "editor", "members": ["user:alex@test.authomize.com"]},
                      {"role": "viewer", "members": ["user:ron@test.authomize.com"]}]}
    ]

    #HERE THIS IS A BAD PRACTICE AND IN REALITY I WOULD USE SPECIFIC LINED AND HAVE BETTER MSG
    assert parsed_data == expected_data, "Parsed data should match the expected data"

