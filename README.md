# Databricks Management Toolkit

A Python toolkit for interacting with Databricks clusters and executing SQL queries against Databricks databases.

## Overview

This repository provides utilities for:
- Listing and managing Databricks clusters
- Executing SQL queries against Databricks databases
- Command-line interfaces for database and cluster operations

## Repository Structure

```
├── LICENSE
├── Makefile
├── README.md
├── cli-manage-db.py           # CLI for Databricks cluster management
├── dblib/                     # Core library package
│   ├── __init__.py
│   ├── manage_databricks.py   # Functions for Databricks cluster operations
│   └── querydb.py             # Functions for SQL query execution
├── hello_databricks_cluster.py # Example script for listing clusters
├── hello_query_sql_db.py       # Example script for querying SQL databases
└── requirements.txt            # Python dependencies
```

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export DATABRICKS_HOST="<your-databricks-workspace-url>"
   export DATABRICKS_TOKEN="<your-personal-access-token>"
   export DATABRICKS_SERVER_HOSTNAME="<your-sql-warehouse-server>"
   export DATABRICKS_HTTP_PATH="<your-sql-warehouse-http-path>"
   ```

## Usage

### Databricks Cluster Management

The `dblib.manage_databricks` module provides functions for working with Databricks clusters:

```python
from dblib.manage_databricks import list_clusters

# List all clusters in your workspace
clusters = list_clusters()
```

Example output:
```
Cluster name, cluster ID
my-cluster-1, 1234-567890-abcd123
my-cluster-2, 5678-123456-wxyz789
```

### SQL Query Execution

The `dblib.querydb` module allows you to execute SQL queries against Databricks databases:

```python
from dblib.querydb import querydb

# Execute a SQL query
results = querydb("SELECT * FROM default.data LIMIT 2")
```

### Command-Line Interface

#### Cluster Management CLI

Use the cluster management CLI to list clusters:

```
python cli-manage-db.py list-clusters
```

For help:
```
python cli-manage-db.py --help
```

#### SQL Query CLI

Use the SQL query CLI to execute queries:

```
python hello_query_sql_db.py query --query "SELECT * FROM default.diamonds LIMIT 2"
```

For help:
```
python hello_query_sql_db.py --help
```

## Environment Variables

The following environment variables need to be set:

- `DATABRICKS_HOST`: Your Databricks workspace URL (e.g., `https://your-org.cloud.databricks.com`)
- `DATABRICKS_TOKEN`: Your Databricks personal access token
- `DATABRICKS_SERVER_HOSTNAME`: Your SQL warehouse server hostname
- `DATABRICKS_HTTP_PATH`: Your SQL warehouse HTTP path

## Dependencies

- `databricks-cli`: Official Databricks CLI for cluster management
- `databricks-sql-connector`: SQL connector for Databricks
- `click`: Library for creating command-line interfaces

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

See the [LICENSE](LICENSE) file for details.