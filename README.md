# Graph Processing with GraphFrames in PySpark

## Overview
This project demonstrates how to use the GraphFrames library in PySpark to perform graph analytics. The project involves creating a graph from a dataset of nodes and edges, performing graph operations like shortest path, PageRank, and connected components, and visualizing the graph and its results.

## Prerequisites
To run this project, you need to have the following installed on your machine:
- Python (3.6 or later)
- Apache Spark (3.x)
- PySpark
- GraphFrames
- Pandas
- NetworkX
- Matplotlib

### Installing Dependencies
You can install the necessary Python packages using pip:
```bash
pip install pyspark pandas networkx matplotlib
```

You also need to download the GraphFrames package. This can be done by specifying it in the Spark session builder as shown in the code.

## Project Structure
- `graph_processing_with_graphframes.py`: The main Python script that runs the GraphFrames workflow.

## Dataset
The dataset used in this project consists of nodes representing users and edges representing relationships between users in a social network.

## Running the Project
1. **Create a Spark Session with GraphFrames**:
   The script starts by creating a Spark session with the GraphFrames package included.

2. **Create a Graph from Nodes and Edges**:
   The script creates two DataFrames, one for vertices (nodes) and one for edges.

3. **Create a GraphFrame**:
   The vertices and edges DataFrames are used to create a GraphFrame.

4. **Perform Graph Operations**:
   - **Shortest Path**: Calculates the shortest path from one vertex to another.
   - **PageRank**: Runs the PageRank algorithm on the graph.
   - **Connected Components**: Identifies connected components in the graph.

5. **Visualize the Graph and Results**:
   The script uses NetworkX and Matplotlib to visualize the graph and its results.



### Steps to Execute
1. **Clone the Repository**:
   If you have the script in a GitHub repository, clone it using:
   ```bash
   git clone https://github.com/yourusername/graphframes-example.git
   cd graphframes-example
   ```

2. **Run the Script**:
   Execute the Python script:
   ```bash
   python graph_processing_with_graphframes.py
   ```

## Conclusion
This project showcases how to use GraphFrames in PySpark to perform graph analytics on a social network dataset. The tasks include creating a graph, performing operations like shortest path, PageRank, and connected components, and visualizing the results using NetworkX and Matplotlib.

## Resources
- [GraphFrames Documentation](https://graphframes.github.io/graphframes/docs/_site/index.html)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
- [NetworkX Documentation](https://networkx.github.io/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Special thanks to the developers of PySpark, GraphFrames, and the open-source community for providing valuable tools and resources.
