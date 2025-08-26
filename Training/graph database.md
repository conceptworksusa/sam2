# Graph database
 A graph database is a type of NoSQL database designed to store, map, and query relationships between data efficiently.
 
### graph databases use:

1. Nodes to represent entities (like people, places, or things)

2. Edges (or relationships) to represent connections between nodes

3. Properties to store information about nodes and edges


```bash


CREATE (alice:Person {name: "Alice"})
CREATE (bob:Person {name: "Bob"})
CREATE (alice)-[:FRIENDS_WITH]->(bob)

```
This creates two people (nodes) and a relationship(edge) showing Alice is friends with Bob.

## Example

```bash


(Alice) ---[FRIEND]---> (Bob)
   |                        |
 [LIKES]                [FRIEND]
   |                        |
(Chocolate)            (Charlie)


```

Nodes: Alice, Bob, Charlie, Chocolate

Edges: FRIEND, LIKES

Properties: A node like Alice might have a property like name: "Alice"
## Common Use Cases

1. Social networks (users connected to other users)

2. Recommendation engines (users connected to products, ratings, etc.)

3. Fraud detection (transactions and their links)

4. Network & IT operations (devices and their dependencies)


# Tools
1. Neo4j (most popular)

2. Amazon Neptune

3. ArangoDB

4. OrientDB

5. TigerGraph


## Advantages

1. Natural data modeling

2. Performance                                                                                

3. Schema flexibility

4. Efficient traversal

## Disadvantages

1. Less mature than relational DBs

2. Not ideal for heavy transactional systems

# Difference b/w GDB AND RDBMS

## GDB

1. Data Model: Nodes and Edges (graph structure)
2. Relationships: Directly stored as edges between nodes
3. Schema: Flexible or schema-less
4. Query Language: Cypher
5. Traversal Speed: Fast for deep and complex relationships
6. Ease of Relationship Queries: Simple and intuitive
7. Best Use Cases: Highly connected data (e.g., social networks, fraud detection)
8. Performance on Deep Queries:Constant-time traversal
9. ex: graph traversal


## RDBMS

1. Data Model: Tables (rows and columns)
2. Relationships: Managed using foreign keys and JOINs
3. Schema:  predefined
4. Query Language: SQL
5. Traversal Speed: Slower with complex joins
6. Ease of Relationship: Complex (many JOINs)
7. Best Use Cases: Structured data (e.g., finance, inventory)
8. Performance on Deep Queries: Slower with depth
9. ex: SQL joins