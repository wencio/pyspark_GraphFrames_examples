from pyspark.sql import SparkSession
from graphframes import GraphFrame
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Create Spark session
spark = SparkSession.builder \
    .appName("GraphFrames Example") \
    .config("spark.jars.packages", "graphframes:graphframes:0.8.2-spark3.0-s_2.12") \
    .getOrCreate()

# Create DataFrame for vertices (nodes)
vertices = spark.createDataFrame([
    ("1", "Alice"),
    ("2", "Bob"),
    ("3", "Charlie"),
    ("4", "David"),
    ("5", "Ed")
], ["id", "name"])

# Create DataFrame for edges
edges = spark.createDataFrame([
    ("1", "2", "friend"),
    ("2", "3", "friend"),
    ("3", "4", "follow"),
    ("4", "5", "follow"),
    ("5", "1", "friend")
], ["src", "dst", "relationship"])

# Create the GraphFrame
graph = GraphFrame(vertices, edges)

# Perform Shortest Path
shortest_paths = graph.shortestPaths(landmarks=["1", "2"])
shortest_paths.show()

# Perform PageRank
pagerank = graph.pageRank(resetProbability=0.15, maxIter=10)
pagerank.vertices.select("id", "pagerank").show()

# Perform Connected Components
connected_components = graph.connectedComponents()
connected_components.show()

# Visualization with NetworkX
# Convert to Pandas for NetworkX
vertices_pd = vertices.toPandas()
edges_pd = edges.toPandas()

# Create NetworkX graph
G = nx.from_pandas_edgelist(edges_pd, "src", "dst", create_using=nx.DiGraph())
labels = dict(zip(vertices_pd.id, vertices_pd.name))

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, labels=labels, node_size=2000, node_color="skyblue", pos=nx.spring_layout(G))
plt.show()

# Stop Spark session
spark.stop()
