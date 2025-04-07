#!/usr/bin/env python
from dblib.manage_databricks import list_clusters
import click


#build a command line group
@click.group()
def cli():
    """Manages Databricks CLI
    
    Example usage:
    ./cli-manage-db.py list-clusters
    """

@cli.command("list-clusters")
def list_clusters_cli():
    """List all clusters"""
    list_clusters()    

#run the cli
if __name__ == "__main__":
    cli() 