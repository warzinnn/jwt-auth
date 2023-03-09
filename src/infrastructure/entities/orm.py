from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import class_mapper, registry
from sqlalchemy.orm.exc import UnmappedClassError

from src.domain.model.user import User

mapper_registry = registry()

user_table = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("passwd", String, nullable=False),
    Column("role", String, nullable=False),
)


def is_mapped_class(cls):
    try:
        class_mapper(cls)
    except (ArgumentError, UnmappedClassError):
        return False
    else:
        return True


def configure_mappers():
    if not is_mapped_class(User):
        mapper_registry.map_imperatively(User, user_table)
