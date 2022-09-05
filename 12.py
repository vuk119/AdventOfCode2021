def is_small(node):
    return node == node.lower()

def dfs(nodes, connections, node, small_visited, sum, double_small) -> int:
    if node == "end":
        sum += 1
        return sum

    # Add this to visited and count paths
    if is_small(node):
        small_visited.add(node)

    # Count paths
    for next_node in connections[node]:
        if next_node == "start":
            continue

        if not next_node in small_visited:
            sum = dfs(nodes, connections, next_node, small_visited, sum, double_small) # Visit small node without changing double_small

        if double_small is False:
            if next_node in small_visited:
                small_visited.remove(next_node)
                sum = dfs(nodes, connections, next_node, small_visited, sum, True) # V
                small_visited.add(next_node)
    # Remove from visited
    if is_small(node):
        small_visited.remove(node)
    return sum

def solve1(nodes, connections) -> int:

    small_visited = set()
    sum = 0
    return dfs(nodes, connections, "start", small_visited, sum, True)

def solve2(nodes, connections) -> int:

    small_visited = set()
    sum = 0
    return dfs(nodes, connections, "start", small_visited, sum, False)

with open("12.txt", "r") as file:
    s = file.read()

connections_raw = s[:-1].split("\n")
nodes = set()
connections = {}

for c in connections_raw:
    n1, n2 = c.split("-")

    if n1 not in nodes:
        nodes.add(n1)
        connections[n1] = []
    if n2 not in nodes:
        nodes.add(n2)
        connections[n2] = []

    connections[n1].append(n2)
    connections[n2].append(n1)

print(solve1(nodes, connections))
print(solve2(nodes, connections))
