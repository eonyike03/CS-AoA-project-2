class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        # Path Compression
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        # Union by Rank
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # already in the same set

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True
def kruskal(vertices, edges):
    """
    vertices: List of vertex labels
    edges: List of tuples (weight, u, v)
    Returns: List of MST edges and total weight
    """
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    #  Sort all edges by ascending weight
    edges.sort()

    # Iterate over edges and pick ones that don't form a cycle
    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


vertices = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

edges = [
    (2451, "New York", "Los Angeles"),
    (713, "New York", "Chicago"),
    (1018, "New York", "Houston"),
    (1631, "New York", "Phoenix"),
    (94, "New York", "Philadelphia"),
    (1745, "Los Angeles", "Chicago"),
    (1374, "Los Angeles", "Houston"),
    (357, "Los Angeles", "Phoenix"),
    (2705, "Los Angeles", "Philadelphia"),
    (1205, "Chicago", "Houston"),
    (1743, "Chicago", "Phoenix"),
    (759, "Chicago", "Philadelphia"),
    (1627, "Houston", "Phoenix"),
    (1548, "Houston", "Philadelphia"),
    (1416, "Phoenix", "Philadelphia"),
    (1371, "San Antonio", "San Diego"),
    (1372, "San Antonio", "Dallas"),
    (1175, "San Antonio", "San Jose"),
    (1467, "San Diego", "Dallas"),
    (1461, "San Diego", "San Jose"),
    (1436, "Dallas", "San Jose")
]
mst_edges, total = kruskal(vertices, edges)

print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} == {w}")

print(f"Total Weight: {total}")
