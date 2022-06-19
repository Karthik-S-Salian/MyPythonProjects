def depthFirstTraversal(graph, start):
    stack = [start]
    current = None
    while len(stack) > 0:
        current = stack.pop()
        print(current)
    for neighbor in graph[current]:
        stack.append(neighbor)


def recursive_depthFirstTraversal(graph, start):
    print(start)
    for neighbour in graph[start]:
        recursive_depthFirstTraversal(graph, neighbour)


def breadthFirstTraversal(graph, start):
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


def recursive_breadthFirstTraversal(graph, start):
    pass


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    recursive_depthFirstTraversal(graph,"f")
