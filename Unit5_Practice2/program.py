// Neo4j Cypher Queries

MATCH (p:Person)
WHERE p.age > 26
RETURN p.name, p.age;

MATCH (:Person)-[r:FRIENDS_WITH]->(:Person)
RETURN COUNT(r);

MATCH (a:Person {name:'Alice'})-[:FRIENDS_WITH]->(friends)
RETURN friends.name;

MATCH (a)-[:FRIENDS_WITH]->(b)-[:FRIENDS_WITH]->(c)
RETURN a.name, c.name;
