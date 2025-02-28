[![Install and run tests](https://github.com/zacernst/pycypher/actions/workflows/makefile.yml/badge.svg)](https://github.com/zacernst/pycypher/actions/workflows/makefile.yml)

[![Build Sphinx documentation](https://github.com/zacernst/pycypher/actions/workflows/docs.yml/badge.svg)](https://github.com/zacernst/pycypher/actions/workflows/docs.yml)

[![Deploy documentation to Github Pages](https://github.com/zacernst/pycypher/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/zacernst/pycypher/actions/workflows/pages/pages-build-deployment)

# pycypher Package Overview

`pycypher` is a Python package designed for building **reactive, graph-based data processing pipelines**. It allows you to define how data is ingested, how knowledge is represented, how constraints are applied, and how actions are triggered in response to changes in the data. The system is designed to be ETL compatible, reactive, and extensible.

## Core Principles

*   **Data Ingestion:** Read data from various sources.
*   **Knowledge Representation:** Store information as atomic facts.
*   **Constraint Definition:** Express rules about the data.
*   **Reactive Triggers:** Automatically execute actions when conditions are met.
*   **Data Output:** Write processed data to different file formats.

## Key Modules and Their Responsibilities

The `pycypher` package is organized into several core modules, each with a distinct role:

1.  **`data_source.py` - Data Ingestion**

    *   **Purpose:** Handles the intake of raw data from external sources and prepares it for processing.
    *   **Key Classes:**
        *   **`DataSource` (Abstract Base Class):** Defines the common interface for all data sources. Subclasses must implement the `rows()` method to yield data.
        *   **`DataSourceMapping`**: A class to define how to convert raw data into one or more facts.
        *   **`FixtureDataSource`:** A data source for testing, reading from an in-memory list. It can hang, delay, or loop, which is useful for testing.
        *   **`CSVDataSource`:** Reads data from CSV files.
        *   **`ParquetFileDataSource`:** Reads data from Parquet files.
    *   **Functionality:**
        *   **Abstraction:** The abstract `DataSource` class allows the rest of the system to work with various data sources without knowing their specifics.
        *   **URI-Based:** Data sources can be created from URIs, providing flexibility.
        *   **Generator Output:** The `rows()` method uses a generator for efficient processing of potentially large or streaming datasets.
        *   **Queue-Based:** Data sources use a queue to send data to downstream processors, enabling asynchronous processing.
        * **Mapping:** `DataSource` objects can have one or more mappings attached, which specify how to convert the raw data into facts.
        * **Schema:** `DataSource` objects can have a schema attached, which will cast the raw data into the correct types.
        * **Raw Data**: `DataSource` objects output shallow dictionaries.

2.  **`fact.py` - Fact Representation**

    *   **Purpose:** Stores information about the graph data as atomic "facts."
    *   **Key Classes:**
        *   **`AtomicFact` (Abstract Base Class):** The base class for all fact types.
        *   **`FactNodeHasLabel`:** A node has a specific label.
        *   **`FactRelationshipHasLabel`:** A relationship has a specific label.
        *   **`FactNodeHasAttributeWithValue`:** A node has an attribute with a specific value.
        * **`FactRelationshipHasAttributeWithValue`**: A relationship has an attribute with a specific value.
        * **`FactNodeRelatedToNode`**: A node is related to another node through a specific relationship.
        * **`FactRelationshipHasSourceNode`**: A relationship has a specific source node.
        * **`FactRelationshipHasTargetNode`**: A relationship has a specific target node.
        *   **`FactCollection`:** A container to store and query a collection of facts.
    *   **Functionality:**
        *   **Atomic Units:** Facts are the basic units of knowledge within the system.
        *   **Graph-Like:** Facts represent nodes, relationships, and their attributes.
        *   **Querying:** `FactCollection` allows querying for facts that match certain criteria.
        * **Constraint Checking:** Facts implement the `__add__` method, allowing them to be checked against a `Constraint`.

3.  **`solver.py` - Constraint Definition**

    *   **Purpose:** Defines the rules and conditions (constraints) that are applied to the graph data.
    *   **Key Classes:**
        *   **`Constraint` (Abstract Base Class):** The base class for all constraint types.
        *   **`IsTrue`:** Checks if a predicate is true.
        * **`ConstraintVariableRefersToSpecificObject`**: Checks if a variable refers to a specific object.
        *   **`ConstraintNodeHasLabel`:** A node has a specific label.
        *   **`ConstraintRelationshipHasSourceNode`:** A relationship has a specific source node.
        *   **`ConstraintRelationshipHasTargetNode`:** A relationship has a specific target node.
        * **`ConstraintRelationshipHasLabel`**: A relationship has a specific label.
        * **`ConstraintNodeHasAttributeWithValue`**: A node has a specific attribute with a certain value.
    *   **Functionality:**
        *   **Rule Definition:** Constraints define what conditions must be met.
        *   **Cypher-Like:** Many constraint types resemble concepts in the Cypher query language.
        *   **Extensibility:** New constraint types can be added by subclassing `Constraint`.
        * **Predicates:** Constraints can evaluate predicates.
        * **Equality**: Constraints can be compared with the equality operator.
        * **Hashing**: Constraints can be used in sets and dictionaries.

4. **`query.py` - Query Definition**:
    * **Purpose**: Defines how to query the `FactCollection`.
    * **Key Classes**:
        * `Query` (Abstract Base Class): The common interface for queries.
        * `QueryNodeLabel`: A query to return the label of a node.
        * `QueryValueOfNodeAttribute`: A query to return the value of a node's attribute.
        * `NullResult`: A special object returned when a query returns no results.
    * **Functionality**:
        * Allows the `FactCollection` to be queried for specific facts.
        * Can be extended with new query types.

5.  **`writer.py` - Data Output**

    *   **Purpose:** Handles the output of processed data to various file formats.
    *   **Key Classes:**
        *   **`TableWriter` (Abstract Base Class):** The common interface for table writers.
        *   **`ParquetTableWriter`:** Writes data to Parquet files.
        *   **`CSVTableWriter`:** Writes data to CSV files.
    *   **Functionality:**
        *   **Tabular Output:** Writes data in a tabular format (rows and columns).
        *   **URI-Based:** Output destinations are specified using URIs.
        *   **Generator Input:** `TableWriter` classes take a generator of data to enable efficient processing.
        *   **Format-Specific Logic:** Each `TableWriter` subclass handles the specifics of writing to its file format.
        * **File Extension Detection**: The correct `TableWriter` subclass is selected based on the file extension.
        * **Entity Table Output**: There is a function to easily output all the facts for a particular node label.

6.  **`goldberg.py` - Pipeline Orchestration**

    *   **Purpose:** Manages the overall flow of data through the entire pipeline.
    *   **Key Class:**
        *   **`Goldberg`:** The central coordinator of the system.
    *   **Functionality:**
        *   **Component Management:** Creates and manages data sources, fact collections, and triggers.
        *   **Thread Management:** Starts and stops the threads.
        *   **Queue Management:** Uses queues to connect components and manage the data flow.
        *   **Trigger Execution:** Executes triggers when their constraints are met.
        *   **Monitoring:** Tracks the status of components and provides insights.
        * **Trigger Registration**: The `cypher_trigger` decorator allows for the creation of new triggers.

7. **`message_types.py`**:
    * **Purpose**: Define the message types used for the queues.
    * **Key Classes**:
        * `RawDatum`: a message type to send a raw row of data.
        * `EndOfData`: A message type to indicate that a data source is done.

8. **`cypher_trigger.py`**:
    * **Purpose**: Define the `CypherTrigger` class.
    * **Key Class**:
        * `CypherTrigger`: A reactive trigger, that fires when all of its constraints are met.
    * **Functionality**:
        * Holds a list of constraints.
        * Contains the function to execute when all constraints are satisfied.
        * Contains the variable name and attribute that are being monitored/set.

9. **`util`**:
    * **Purpose**: Contains utility functions.
    * **Key Classes**:
        * `QueueGenerator`: A class to wrap the `queue.Queue` class.
    * **Key Functions**:
        * `ensure_uri`: Convert a string into a parsed `ParseResult` object.

## Data Flow and Workflow

1.  **Data Ingestion:** A `DataSource` reads raw data and adds `RawDatum` objects to a queue. It adds `EndOfData` to the queue when it is finished.
2.  **Fact Generation:** Raw data is processed, and `AtomicFact` objects are created.
3.  **Fact Storage:** Facts are stored in a `FactCollection`.
4.  **Constraint Evaluation:** New facts are checked against constraints.
5.  **Trigger Execution:** When all constraints are met, a `CypherTrigger` is executed.
6.  **Data Output:** `TableWriter` objects are used to write processed data or new facts to files.

## Extensibility

`pycypher` is designed to be extended:

*   **New Data Sources:** Add support for new data sources by subclassing `DataSource`.
*   **New File Formats:** Add support for new file output formats by subclassing `TableWriter`.
*   **New Constraints:** Add new constraint types by subclassing `Constraint`.
* **New Queries**: Add new query types by subclassing `Query`.
* **New Mappings**: Create new types of mappings, by subclassing `DataSourceMapping`.

## Use Cases

*   **ETL Pipelines:** Build complex ETL pipelines with reactive logic.
*   **Data Validation:** Enforce rules about the data.
*   **Reactive Systems:** Build systems where actions are automatically triggered based on data changes.
*   **Knowledge Graphs:** Create and manage knowledge graphs.
*   **Data Integration:** Connect different data sources and systems.
* **Pattern Matching**: Define complex patterns to look for in the data.

## Summary

`pycypher` provides a robust, flexible, and extensible framework for building reactive graph-based data processing pipelines. It focuses on:

*   **Graph-like Data:** Modeling data with nodes, relationships, and attributes.
*   **Atomic Facts:** Representing knowledge as individual facts.
*   **Constraints:** Defining rules about the data.
*   **Reactive Triggers:** Automating actions based on data changes.
*   **Extensibility:** Allowing the addition of new data sources, constraints, and output formats.
* **ETL**: The library is designed for ETL operations.
* **Reactive**: The library automatically executes triggers, when constraints are satisfied.

The documentation is [here](https://zacernst.github.io/pycypher/).