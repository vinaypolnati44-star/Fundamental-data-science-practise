// Neo4j Cypher Queries

CREATE (a:Person {name:'Alice', age:25});
CREATE (b:Person {name:'Bob', age:27});
CREATE (c:Person {name:'Charlie', age:30});

CREATE (a)-[:FRIENDS_WITH]->(b);
CREATE (b)-[:FRIENDS_WITH]->(c);
CREATE (a)-[:COLLEAGUE_OF]->(c);

MATCH (n) RETURN n;
