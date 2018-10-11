from heapq import *


def all_shortest_paths(graph):
    """
    Floyd-Warshall algorithm.

    Parameters
    ----------
        'graph' : a Graph object

    Returns
    -------
        A matrix M (list of list) where M[i][j] = the length of the
        shortest path from vertex i to vertex j
    """
    adj = graph.adjacency_matrix()
    n = len(adj)
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 0:
                adj[i][j] = float("inf")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    return adj


def shortest_path(graph, v_start, v_end, heuristic):
    """
    A* algorithm

    Parameters
    ----------
        'graph' : a Graph object
            graph on which to perform the search

        'v_start' : a Vertex object
            Starting point of the algorithm

        'v_end' : a Vertex object
            Target point of the algorithm

        'heuristic' : a function (Vertex a, Vertex b) -> weight
            Evaluate the distance from a to b

    Returns
    -------
        The length l and the sequence of vertices of (one of the) shortest
        paths from v_start to v_end
    """
    heap = [(0, 0, v_start, None)]
    dist = dict()
    origin = dict()
    t = 0
    while not heap.empty() and v_end not in dict:
        weight, node, _, father = heappop(heap)
        if node in dist:
            continue
        dist[node] = weight
        origin[node] = father
        for edge in graph.get_edges(node):
            neighbour = edge.end,
            if dist[neighbour] == -1:
                t += 1
                newweight = weight + h(neighbour, v_end) + edge.weight
                heappush((newweight, t, neighbour, node))

    def recover(node):
        ans = []
        while origin[node] is not None:
            ans.append(node)
            node = origin[node]
        return ans
    return dist[v_end], recover(v_end)


def dijkstra(graph, v_start, v_end):
    """
    A* algorithm

    Parameters
    ----------
        'graph' : a Graph object
            graph on which to perform the search

        'v_start' : a Vertex object
            Starting point of the algorithm

        'v_end' : a Vertex object
            Target point of the algorithm

    Returns
    -------
        The length l and the sequence of vertices of (one of the) shortest
        paths from v_start to v_end
    """
    def no_heuristic(a, b):
        return 0
    return shortest_path(graph, v_start, v_end, no_heuristic)


def diameter(graph):
    """
    The diameter is defined as the longest shortest path among all pairs
    of vertices. It is by convention infinite for non-connected graphs

    Parameters
    ----------
        'graph' : a Graph object
            The graph on which to perform the algorithm

    Returns
    -------
        The diameter of the graph.
    """
    paths = all_shortest_paths(graph)
    n = len(paths)
    mini = float("inf")
    for i in range(n):
        for j in range(n):
            if paths[i][j] <= mini:
                mini = paths[i][j]
    return mini
