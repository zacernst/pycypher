"""Queries are searches for facts..."""

from __future__ import annotations


class Query:  # pylint: disable=too-few-public-methods
    """Abstract base class."""


class QueryValueOfNodeAttribute(Query):
    """Ask what the value of a specific attribute is for a specific node."""  # pylint: disable=too-few-public-methods

    def __init__(self, node_id: str, attribute: str):
        self.node_id = node_id
        self.attribute = attribute


class QueryValueOfRelationshipAttribute(Query):
    """Not implemented"""  # pylint: disable=too-few-public-methods

    def __init__(self, relationship_id: str, attribute: str):
        self.relationship_id = relationship_id
        self.attribute = attribute
