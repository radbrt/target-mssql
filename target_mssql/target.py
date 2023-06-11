"""mssql target class."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.target_base import SQLTarget

from target_mssql.sinks import mssqlSink


class Targetmssql(SQLTarget):
    """Singer target for mssql."""

    name = "target-mssql"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "sqlalchemy_url",
            th.StringType,
            description="SQLAlchemy connection string",
        ),
        th.Property(
            "username",
            th.StringType,
            description="SQL Server username",
        ),
        th.Property(
            "password",
            th.StringType,
            description="SQL Server password",
        ),
        th.Property(
            "host",
            th.StringType,
            description="SQL Server host",
        ),
        th.Property(
            "port",
            th.StringType,
            default="1433",
            description="SQL Server port",
        ),
        th.Property(
            "database",
            th.StringType,
            description="SQL Server database",
        ),
        th.Property(
            "default_target_schema",
            th.StringType,
            description="Default target schema to write to",
        ),
        th.Property(
            "column_renaming",
            th.StringType,
            default="snake_lowercase",
            description="Column renaming strategy",
        ),
    ).to_dict()

    default_sink_class = mssqlSink


if __name__ == "__main__":
    Targetmssql.cli()
