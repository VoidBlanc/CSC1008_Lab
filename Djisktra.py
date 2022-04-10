import sys
from DataStructure.Graph import Graph


def dijkstra(graph, src, dest):
    shortest_distance = {}  # records the cost to reach to • that node. Going LO be updated as we move along the graph
    track_predecessor = {}  # keep track of the path that has • Led us to this node
    unseenNodes = graph  # to iterate through the entire graph.
    infinity = sys.maxsize  # infinity can basically be considered a very Large number
    path = []  # going to trace our journey back to the source • node optimal route•
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[src] = 0
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options = graph[min_distance_node].items()
        for child, cost in path_options:
            if cost + shortest_distance[min_distance_node] < shortest_distance[child]:
                shortest_distance[child] = cost + shortest_distance[min_distance_node]
                track_predecessor[child] = min_distance_node
        unseenNodes.pop(min_distance_node)

    currNode = dest
    while currNode != src:
        try:
            path.insert(0, currNode)
            currNode = track_predecessor[currNode]
        except KeyError:
            print("Path is not reachable")
            break
    path.insert(0, src)

    if shortest_distance[dest] != infinity:
        print("Shortest distance is " + str(shortest_distance[dest]))
        print("Optimal path is " + str(path))


graph = Graph()

dijkstra(graph.graph, 'A', 'E')