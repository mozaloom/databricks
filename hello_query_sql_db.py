#!/usr/bin/env python

from dblib.querydb import querydb
import click

#build a command group
@click.group()
def cli():
    """CLI for querying a SQL database.
    
    example:
    ./hello_query_sql_db.py query --query "SELECT * FROM default.diamonds LIMIT 2"""
    pass

@cli.command()
@click.option("--query", default="SELECT * FROM default.diamonds LIMIT 2", help="SQL query to execute.")

def cli_query(query):
    """Execute a SQL query."""
    result = querydb(query)

if __name__ == "__main__":
    cli()

