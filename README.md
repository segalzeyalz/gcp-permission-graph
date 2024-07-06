# Permission Graph Builder

This project builds a permission graph from a JSON lines file and allows querying the graph for resource hierarchies, identity permissions, and resource identities.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/segalzeyalz/gcp-permission-graph
   cd permission-graph-builder
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Building the Graph

To build the graph from a JSON1 file:

```bash
python main.py data/example.json1
```

### Querying the Graph

#### Get the Hierarchy of a Resource

To get the hierarchy of a specific resource:

```bash
python main.py data/example.json1 --resource-hierarchy <RESOURCE_ID>
```

Example:

```bash
python main.py data/example.json1 --resource-hierarchy resource1
```

#### Get the Permissions of an Identity

To get the permissions of a specific identity:

```bash
python main.py data/example.json1 --identity-permissions <IDENTITY_ID>
```

Example:

```bash
python main.py data/example.json1 --identity-permissions user:alex@test.authomize.com
```

#### Get the Identities with Permissions on a Resource

To get the identities with permissions on a specific resource:

```bash
python main.py data/example.json1 --resource-identities <RESOURCE_ID>
```

Example:

```bash
python main.py data/example.json1 --resource-identities resource1
```

## Example Usage
To build the graph and query it using the example data:

```bash
python example_usage.py
```

This will output:
```
Resource Hierarchy for 'resource1': ['folder1', 'organization1']
Permissions for 'user:alex@test.authomize.com': [('resource1', 'RESOURCE', 'owner'), ('resource2', 'RESOURCE', 'editor')]
Identities with permissions on 'resource2': [('user:alex@test.authomize.com', 'editor'), ('user:ron@test.authomize.com', 'viewer')]
```

## Development

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

Make sure you have `pytest` installed. You can install it by running:

```bash
pip install pytest
```

### Project Structure

- `main.py`: The entry point of the CLI application.
- `src/`: Contains the source code for the graph, nodes, edges, parser, and builder.
- `tests/`: Contains the test cases for the project.
- `data/`: Contains sample data files.

### Method Efficiency and Trade-Offs

methods and trade-offs

| Method                     | Current Complexity | Way to Improve                                     | Trade-Offs                                                            |
|----------------------------|--------------------|----------------------------------------------------|----------------------------------------------------------------------|
| `add_node`                 | O(1)               | Efficient as is                                    | N/A                                                                  |
| `add_edge`                 | O(1)               | Efficient as is                                    | N/A                                                                  |
| `get_resource_hierarchy`   | O(n)               | Use `parent_map` for efficient parent lookups      | Increased memory usage and complexity of maintaining `parent_map`    |
| `get_identity_permissions` | O(n)               | Use `permission_map` for efficient permission lookups | Increased memory usage and complexity of maintaining `permission_map`|
| `get_resource_identities`  | O(1)               | Already optimized using `permission_map`           | N/A                                                                  |

### Alternative Approaches

#### Depth-First Search (DFS) or Breadth-First Search (BFS)

Using DFS/BFS for `get_resource_hierarchy`:
- **Implementation**: Perform a DFS or BFS starting from the given resource and traverse upwards to build the hierarchy.
- **Complexity**: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
- **Trade-Offs**: 
  - **Memory Usage**: Lower memory usage compared to maintaining a hashmap.
  - **Performance**: Potentially slower than O(1) lookups, especially for dense graphs.
  - **Implementation Complexity**: Moderate, involves additional code for traversal.

#### Adjacency Lists without Hashmaps

Using adjacency lists for `get_identity_permissions` and `get_resource_identities`:
- **Implementation**: Store edges directly connected to each node using lists or arrays indexed by node IDs.
- **Complexity**: O(V + E) for traversing nodes and edges.
- **Trade-Offs**: 
  - **Memory Usage**: Slightly lower memory usage compared to hashmaps.
  - **Performance**: Lookup operations are O(V + E), slower than O(1) hash lookups.
  - **Implementation Complexity**: Higher, involves manual management of lists and careful indexing.

These approaches offer alternatives to hashmaps/dictionaries, balancing memory usage and performance based on specific needs and constraints.
