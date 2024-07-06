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
