'''
This module contains several functions that allow the user
to read from file and write into the file oriented and non-oriented
graphs, get the components of a non-oriented graph and strongly
connected components of a directed graph. It also contains functions
that can find the articulation points and bridges of an undirected
graph.
'''


############
# Part 1
############


def read_csv_non_oriented(path:str)->dict:
    """
    Read csv-file and create a dict.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', delete = False) as tmp:
    ...     _ = tmp.write('1,2\\n1,3\\n2,3\\n2,4\\n2,5\\n3,4\\n4,5\\n5,1')
    >>> output = read_csv_non_oriented(tmp.name)
    >>> output == {1: [2, 3, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [2, 3, 5], 5: [2, 4, 1]}
    True
    """
    with open(path, 'r', encoding='UTF-8') as file:
        graph={}
        for line in file:
            line=line.strip().split(',')
            u, v = line
            try:
                graph[int(u)] += [int(v)]
            except KeyError:
                graph[int(u)] = [int(v)]
            try:
                graph[int(v)] += [int(u)]
            except KeyError:
                graph[int(v)] = [int(u)]
    return graph

def read_csv_oriented(path:str)->dict:
    """
    Read csv-file and create a dict.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', delete = False) as tmp:
    ...     _ = tmp.write('1,2\\n1,3\\n2,3\\n2,4\\n2,5\\n3,4\\n4,5\\n5,1')
    >>> output = read_csv_oriented(tmp.name)
    >>> output == {1: [2, 3], 2: [3, 4, 5], 3: [4], 4: [5], 5: [1]}
    True
    """
    with open(path, 'r', encoding='UTF-8') as file:
        graph={}
        for line in file:
            line=line.strip().split(',')
            u, v = line
            try:
                graph[int(u)] += [int(v)]
            except KeyError:
                graph[int(u)] = [int(v)]
    return graph


############
# Part 2
############


def write_file_non_oriented(path:str, graph:dict):
    """
    Write graph in csv-file.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w+', delete = False) as tmp:
    ...     write_file_non_oriented(tmp.name, \
{1: [2, 3, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [2, 3, 5], 5: [1, 2, 4]})
    ...     output = read_csv_non_oriented(tmp.name)
    >>> output == {1: [2, 3, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [2, 3, 5], 5: [1, 2, 4]}
    True
    """
    with open(path, 'w', encoding='UTF-8') as file:
        result=[]
        length=len(graph.keys())
        counter=1
        iterator = iter(graph)
        while counter!=length:
            key = next(iterator)
            for ver in graph[key]:
                pair=''
                pair_check=''
                pair+=str(key)+','+str(ver)+'\n'
                pair_check+=str(ver)+','+str(key)+'\n'
                if pair_check in result:
                    continue
                result.append(pair)
            counter+=1
        for edge in result:
            file.write(edge)


def write_file_oriented(path:str, graph:dict):
    """
    Write graph in csv-file.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w+', delete = False) as tmp:
    ...     write_file_oriented(tmp.name, \
{1: [2, 3], 2: [3, 4, 5], 3: [4], 4: [5], 5: [1]})
    ...     output = read_csv_oriented(tmp.name)
    >>> output == {1: [2, 3], 2: [3, 4, 5], 3: [4], 4: [5], 5: [1]}
    True
    """
    with open(path, 'w', encoding='UTF-8') as file:
        length=len(graph.keys())
        counter=0
        iterator = iter(graph)
        while counter!=length:
            key=next(iterator)
            pair=''
            for ver in graph[key]:
                pair+=str(key)+','+str(ver)+'\n'
            file.write(pair)
            counter+=1


############
# Part 3
############


def graph_checking(graph: dict) -> bool:
    """
    dict -> bool

    Checks whether the graph is presented in 
    the correct form.    
    """
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if node not in graph.get(neighbor, []):
                return False
    return True

def graph_component(graph: dict) -> list:
    """
    dict -> list
    Searches graph's components. Return 2D list, where list
    has number of edges of component.
    
    >>> graph_component({1: [2, 3], 2: [3], 3: [1, 2]})
    'Введіть правильно граф'
    >>> graph_component({1: [2], 2: [1, 3], 3: [2, 4], 4: [3]})
    [1]
    >>> graph_component({1: [2], 2: [1, 3], 3: [2, 4], 4: [3], 5: [6], 6: [5]})
    [1, 5]
    """
    if graph_checking(graph):
        visited = []
        res = []

        def visit_nodes(at):
            if at in res:
                return res
            res.append(at)
            neighbor = graph[at]
            for node in neighbor:
                visit_nodes(node)

        for node in graph:
            if node not in [num for lst in visited for num in lst]:
                visit_nodes(node)
                visited.append(res.copy())
                res = []
        return [min(component) for component in visited]
    else:
        return 'Введіть правильно граф'


############
# Part 4
############


def tarjans_algorithm(graph: dict):
    '''
    A function that utilizes the Tarjan's algorithm to find
    all strongly connected components of a directed graph.

    >>> tarjans_algorithm({0: [1], 1: [2], 2: [3, 4], 3: [0], 4: [5], 5: [6], 6: [4, 7]})
    [0, 4, 7]
    '''
    def dfs(v: int, index: int, stack: list, indices: dict,\
             lowlinks: dict, result: list):

        indices[v] = index
        lowlinks[v] = index
        index += 1
        stack.append(v)

        for neighbor in graph.get(v, []):
            if not neighbor in indices:
                index = dfs(neighbor, index, stack, indices, lowlinks, result)
                lowlinks[v] = min(lowlinks[v], lowlinks[neighbor])
            elif neighbor in stack:
                lowlinks[v] = min(lowlinks[v], indices[neighbor])

        if lowlinks[v] == indices[v]:
            scc = []
            while True:
                node = stack.pop()
                scc.append(node)
                if node == v:
                    break
            result.append(min(scc))

        return index

    indices = {}
    lowlinks = {}
    stack = []
    result = []

    index = 0
    for v in graph:
        if not v in indices:
            index = dfs(v, index, stack, indices, lowlinks, result)

    return sorted(result)


############
# Part 5
############


def articulation_finder(graph: dict):
    '''
    A function based on Tarjan's algorithm that finds all
    articulation points of a graph and returns a list of them.

    >>> articulation_finder({1: [2, 6], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3], 5: [2, 3], 6: [1, 7],\
7: [6], 8: [9], 9: [8, 10, 11], 10: [9, 11], 11: [9, 10]})
    [1, 2, 3, 6, 9]
    '''

    info = {}
    result = []

    for vertex in sorted(graph):
        if not vertex in info:
            info[vertex] = [0, 0, None]
            articulation_recursive(graph, vertex, info, result, 1)
    return sorted(result)

def articulation_recursive(graph: dict, vertex: int, info: dict, result: list, step: int):
    '''
    An enchanced version of dfs based on the Tarjan's algorithm,
    used by the articulation_finder function. 
    '''

    children = 0

    for connection in graph[vertex]:
        if not connection in info:
            info[connection] = [step, step, vertex]
            articulation_recursive(graph, connection, info, result, step + 1)
            children += 1
            info[vertex][0] = min(info[vertex][0], info[connection][0])

            if not info[vertex][2] is None and info[connection][0] >= info[vertex][1]:
                result.append(vertex)

        elif connection != info[vertex][2]:
            info[vertex][0] = min(info[vertex][0], info[connection][1])

    if info[vertex][2] is None and children > 1:
        result.append(vertex)


############
# Part 6
############


def bridge_finder(graph: dict):
    '''
    A function based on Tarjan's algorithm that finds all
    bridges of a graph and returns a list of them.

    >>> bridge_finder({1: [2, 6], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3], 5: [2, 3], 6: [1, 7],\
7: [6], 8: [9], 9: [8, 10, 11], 10: [9, 11], 11: [9, 10]})
    [[3, 4], [1, 2], [6, 7], [1, 6], [8, 9]]
    '''

    info = {}
    result = []

    for vertex in sorted(graph):
        if not vertex in info:
            info[vertex] = [0, 0, None]
            bridge_recursive(graph, vertex, info, result, 1)
    return result

def bridge_recursive(graph: dict, vertex: int, info: dict, result: list, step: int):
    '''
    An enchanced version of dfs based on the Tarjan's algorithm,
    used by the bridge_finder function. 
    '''

    for connection in graph[vertex]:
        if not connection in info:
            info[connection] = [step, step, vertex]
            bridge_recursive(graph, connection, info, result, step + 1)
            info[vertex][0] = min(info[vertex][0], info[connection][0])

            if info[connection][0] > info[vertex][1]:
                result.append(sorted([vertex, connection]))

        elif connection != info[vertex][2]:
            info[vertex][0] = min(info[vertex][0], info[connection][1])

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
