from typing import Any, Dict, List, Tuple

import lamindb as lamin
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/introspection")


class Column(BaseModel):
    key: str
    type: str
    primary_key: bool
    foreign_keys: List[Tuple[str, str]]
    nullable: bool
    default: Any


class TableSchema(BaseModel):
    key: str
    primary_keys: List[str]
    foreign_keys: List[Tuple[str, str]]
    columns: Dict[str, Column]


class Database(BaseModel):
    key: str
    tables: Dict[str, TableSchema]


@router.get("/", response_model=Database)
async def get_db_schema():
    schema = lamin.schema._core.get_db_metadata_as_dict()
    return schema


@router.get("/{name}")
async def get_table(name: str):
    schema_name = name.split(".")[0] if "." in name else "public"
    table_name = name.split(".")[-1]
    table_metaclass = lamin.schema._table.table_meta.get_model(table_name)

    # Rows
    table_df = lamin.select(table_metaclass).df()
    rows = table_df.to_dict(orient="records")

    # Schema
    table_object = lamin.schema._core.get_table_object(f"{schema_name}.{table_name}")
    schema = lamin.schema._core.get_table_metadata_as_dict(table_object)

    return {"schema": schema, "rows": rows}
