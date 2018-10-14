## Neo4j table to graph:

this project is used to convert table data into csv that neo4j import can used to import your data 
you only need to supply your data and model on how to transform the data into the nodes and edges of the
graph ( as you can see in the data folder) 

and run the neo4j-admin commend: 

```
$> neo4j-admin.bat import --database "test.db"  \
  --nodes "output\nodes_header.csv, output\nodes.csv"  \
  --relationships "output\edges_header.csv, output\edges.csv"
```

for any other question suggestion or any other request feel free to contact me.
