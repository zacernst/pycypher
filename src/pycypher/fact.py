"""
Facts are simple atomic statements that have a truth value.
"""

from __future__ import annotations

from typing import Any, Generator, List

from pycypher.query import Query, QueryValueOfNodeAttribute


class AtomicFact:  # pylint: disable=too-few-public-methods
    """
    Abstract base class for specific types of `Fact`.

    This class serves as a base for creating various types of facts in the system.
    It is intended to be subclassed and not used directly.

    Attributes:
        None

    Methods:
        None
    """

    pass


class FactNodeHasLabel(AtomicFact):
    """
    Represents a fact that a node has a specific label.

    Attributes:
        node_id (str): The ID of the node.
        label (str): The label of the node.

    Methods:
        __repr__(): Returns a string representation of the FactNodeHasLabel instance.
        __eq__(other: Any): Checks equality between this instance and another FactNodeHasLabel instance.
    """

    def __init__(self, node_id: str, node_label: str):
        self.node_id = node_id
        self.label = node_label

    def __repr__(self):
        return f"NodeHasLabel: {self.node_id} {self.label}"

    def __eq__(self, other: Any):
        return (
            isinstance(other, FactNodeHasLabel)
            and self.node_id == other.node_id
            and self.label == other.label
        )


class FactRelationshipHasLabel(AtomicFact):
    """
    Represents a fact that a relationship has a specific label.

    Attributes:
        relationship_id (str): The ID of the relationship.
        relationship_label (str): The label of the relationship.

    Methods:
        __repr__(): Returns a string representation of the fact.
        __eq__(other: Any) -> bool: Checks equality between this fact and another.
    """

    def __init__(self, relationship_id: str, relationship_label: str):
        self.relationship_id = relationship_id
        self.relationship_label = relationship_label

    def __repr__(self):
        return (
            f"NodeHasLabel: {self.relationship_id} {self.relationship_label}"
        )

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FactRelationshipHasLabel)
            and self.relationship_id == other.relationship_id
            and self.relationship_label == other.relationship_label
        )


class FactRelationshipHasAttributeWithValue(AtomicFact):
    """
    Represents a fact that a relationship has a specific attribute with a given value.

    Attributes:
        relationship_id (str): The ID of the relationship.
        attribute (str): The attribute of the relationship.
        value (Any): The value of the attribute.

    Args:
        relationship_id (str): The ID of the relationship.
        attribute (str): The attribute of the relationship.
        value (Any): The value of the attribute.
    """

    def __init__(self, relationship_id: str, attribute: str, value: Any):
        self.relationship_id = relationship_id
        self.attribute = attribute
        self.value = value


class FactNodeHasAttributeWithValue(AtomicFact):
    """
    Represents a fact that a node has a specific attribute with a given value.

    Attributes:
        node_id (str): The identifier of the node.
        attribute (str): The attribute of the node.
        value (Any): The value of the attribute.

    Methods:
        __repr__(): Returns a string representation of the fact.
        __eq__(other: Any): Checks equality between this fact and another fact.
    """

    def __init__(self, node_id: str, attribute: str, value: Any):
        self.node_id = node_id
        self.attribute = attribute
        self.value = value

    def __repr__(self) -> str:
        return f"NodeHasAttributeWithValue: {self.node_id} {self.attribute} {self.value}"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FactNodeHasAttributeWithValue)
            and (self.node_id == other.node_id)
            and (self.attribute == other.attribute)
            and (self.value == other.value)
        )


class FactNodeRelatedToNode(AtomicFact):
    """
    Represents a fact that one node is related to another node with a specific relationship label.

    Attributes:
        node1_id (str): The ID of the first node.
        node2_id (str): The ID of the second node.
        relationship_label (str): The label of the relationship between the two nodes.

    Methods:
        __repr__() -> str: Returns a string representation of the fact.
        __eq__(other: Any) -> bool: Checks if this fact is equal to another fact.
    """

    def __init__(self, node1_id: str, node2_id: str, relationship_label: str):
        self.node1_id = node1_id
        self.node2_id = node2_id
        self.relationship_label = relationship_label

    def __repr__(self) -> str:
        return f"NodeRelatedToNode: {self.node1_id} {self.relationship_label} {self.node2_id}"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FactNodeRelatedToNode)
            and self.node1_id == other.node1_id
            and self.node2_id == other.node2_id
            and self.relationship_label == other.relationship_label
        )


class FactRelationshipHasSourceNode(AtomicFact):
    """
    Represents a fact that a relationship has a source node.

    Attributes:
        relationship_id (str): The ID of the relationship.
        source_node_id (str): The ID of the source node.

    Methods:
        __repr__(): Returns a string representation of the FactRelationshipHasSourceNode instance.
        __eq__(other: Any): Checks equality between this instance and another FactRelationshipHasSourceNode instance.
    """

    def __init__(self, relationship_id: str, source_node_id: str):
        self.relationship_id = relationship_id
        self.source_node_id = source_node_id

    def __repr__(self) -> str:
        return f"RelationshipHasSourceNode: {self.relationship_id} {self.source_node_id}"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FactRelationshipHasSourceNode)
            and self.relationship_id == other.relationship_id
            and self.source_node_id == other.source_node_id
        )


class FactRelationshipHasTargetNode(AtomicFact):
    """
    Represents a fact that a relationship has a target node.

    Attributes:
        relationship_id (str): The ID of the relationship.
        target_node_id (str): The ID of the target node.

    Methods:
        __repr__() -> str:
            Returns a string representation of the FactRelationshipHasTargetNode instance.

        __eq__(other: Any) -> bool:
            Checks if this instance is equal to another instance of FactRelationshipHasTargetNode.
    """

    def __init__(self, relationship_id: str, target_node_id: str):
        self.relationship_id = relationship_id
        self.target_node_id = target_node_id

    def __repr__(self) -> str:
        return f"RelationshipHasTargetNode: {self.relationship_id} {self.target_node_id}"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FactRelationshipHasTargetNode)
            and self.relationship_id == other.relationship_id
            and self.target_node_id == other.target_node_id
        )


class FactCollection:
    """
    A collection of AtomicFact objects with various utility methods for querying and manipulating the facts.

    Attributes:
        facts (List[AtomicFact]): A list of AtomicFact objects.

    Methods:
        __iter__() -> Generator[AtomicFact]:
            Yields each fact in the collection.

        __repr__() -> str:
            Returns a string representation of the FactCollection.

        __getitem__(index: int) -> AtomicFact:
            Returns the fact at the specified index.

        __setitem__(index: int, value: AtomicFact):
            Sets the fact at the specified index to the given value.

        __delitem__(index: int):
            Deletes the fact at the specified index.

        __len__() -> int:
            Returns the number of facts in the collection.

        insert(index: int, value: AtomicFact):
            Inserts a fact at the specified index.

        relationship_has_source_node_facts() -> Generator[FactRelationshipHasSourceNode]:
            Yields facts that are instances of FactRelationshipHasSourceNode.

        relationship_has_target_node_facts() -> Generator[FactRelationshipHasTargetNode]:
            Yields facts that are instances of FactRelationshipHasTargetNode.

        node_has_label_facts() -> Generator[FactNodeHasLabel]:
            Yields facts that are instances of FactNodeHasLabel.

        node_has_attribute_with_value_facts() -> Generator[FactNodeHasAttributeWithValue]:
            Yields facts that are instances of FactNodeHasAttributeWithValue.

        relationship_has_attribute_with_value_facts() -> Generator[FactRelationshipHasAttributeWithValue]:
            Yields facts that are instances of FactRelationshipHasAttributeWithValue.

        query(query: Query) -> Any:
            Executes a query on the collection and returns the result.
            Raises:
                ValueError: If the query cannot be resolved or if multiple values are found for a QueryValueOfNodeAttribute.
                NotImplementedError: If the query type is unknown.
    """

    def __init__(self, facts: List[AtomicFact]):
        self.facts: List[AtomicFact] = facts

    def __iter__(self) -> Generator[AtomicFact]:
        yield from self.facts

    def __repr__(self) -> str:
        return f"FactCollection: {len(self.facts)}"

    def __getitem__(self, index: int) -> AtomicFact:
        return self.facts[index]

    def __setitem__(self, index: int, value: AtomicFact):
        self.facts[index] = value

    def __delitem__(self, index: int):
        del self.facts[index]

    def __len__(self):
        return len(self.facts)

    def insert(self, index: int, value: AtomicFact):
        """
        Insert an AtomicFact into the facts list at the specified index.

        Args:
            index (int): The position at which to insert the value.
            value (AtomicFact): The AtomicFact object to be inserted.

        Returns:
            None
        """
        self.facts.insert(index, value)

    def relationship_has_source_node_facts(self):
        """
        Generator method that yields facts of type FactRelationshipHasSourceNode.

        This method iterates over the `facts` attribute of the instance and yields
        each fact that is an instance of the FactRelationshipHasSourceNode class.

        Yields:
            FactRelationshipHasSourceNode: Facts that are instances of FactRelationshipHasSourceNode.
        """
        for fact in self.facts:
            if isinstance(fact, FactRelationshipHasSourceNode):
                yield fact

    def relationship_has_target_node_facts(self):
        """
        Generator method that yields facts of type FactRelationshipHasTargetNode.

        Iterates over the `facts` attribute of the instance and yields each fact
        that is an instance of FactRelationshipHasTargetNode.

        Yields:
            FactRelationshipHasTargetNode: Facts that are instances of FactRelationshipHasTargetNode.
        """
        for fact in self.facts:
            if isinstance(fact, FactRelationshipHasTargetNode):
                yield fact

    def node_has_label_facts(self):
        """
        Generator function that yields facts of type `FactNodeHasLabel`.

        Iterates over the `facts` attribute and yields each fact that is an instance
        of `FactNodeHasLabel`.

        Yields:
            FactNodeHasLabel: Facts that are instances of `FactNodeHasLabel`.
        """
        for fact in self.facts:
            if isinstance(fact, FactNodeHasLabel):
                yield fact

    def node_has_attribute_with_value_facts(self):
        """
        Generator method that yields facts of type FactNodeHasAttributeWithValue.

        Iterates over the list of facts and yields each fact that is an instance
        of FactNodeHasAttributeWithValue.

        Yields:
            FactNodeHasAttributeWithValue: Facts that are instances of FactNodeHasAttributeWithValue.
        """
        for fact in self.facts:
            if isinstance(fact, FactNodeHasAttributeWithValue):
                yield fact

    def relationship_has_attribute_with_value_facts(self):
        """
        Generator function that yields facts of type FactRelationshipHasAttributeWithValue.

        Iterates over the `facts` attribute and yields each fact that is an instance of
        FactRelationshipHasAttributeWithValue.

        Yields:
            FactRelationshipHasAttributeWithValue: Facts that are instances of FactRelationshipHasAttributeWithValue.
        """
        for fact in self.facts:
            if isinstance(fact, FactRelationshipHasAttributeWithValue):
                yield fact

    def query(self, query: Query) -> Any:
        """
        Executes a query to retrieve information based on the type of the query.

        Args:
            query (Query): The query object containing the parameters for the query.

        Returns:
            Any: The result of the query. The type of the result depends on the query type.

        Raises:
            ValueError: If the query is of type QueryValueOfNodeAttribute and no matching facts are found,
                        or if multiple matching facts are found, or if an unknown error occurs.
            NotImplementedError: If the query type is not recognized.
        """
        if isinstance(query, QueryValueOfNodeAttribute):
            facts = [
                fact
                for fact in self.node_has_attribute_with_value_facts()
                if fact.node_id == query.node_id
                and fact.attribute == query.attribute
            ]
            if len(facts) == 1:
                return facts[0].value
            elif len(facts) == 0:
                raise ValueError(f"Could not find value for {query}")
            elif len(facts) > 1:
                raise ValueError(f"Found multiple values for {query}")
            else:
                raise ValueError("Unknown error")
        else:
            raise NotImplementedError(f"Unknown query type {query}")
