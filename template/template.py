# -*-coding:utf-8-*-

from cowpy import cow


def bfs(graph, start, end):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print path
                return (True, path)
            # 两个点不想连 则跳过
            if current not in graph:
                continue
        visited = visited + graph[current]
    return (False, path)


def dfs(graph, start, end):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print path
                return (True, path)
            # 两个点不想连 则跳过
            if current not in graph:
                continue
        visited = graph[current] + visited
    return (False, path)


graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
}


def main():
    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    print 'bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found')
    print 'dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found')

    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    print 'bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found')
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    print 'dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found')


def traverse(graph, start, end, action):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                return (True, path)
            # 两个顶点之间没有连接 则跳过
            if current not in graph:
                continue
        visited = action(visited, graph[current])
    return (False, path)


def extend_bfs_path(visited, current):
    return visited + current


def extend_dfs_path(visited, current):
    return current + visited


# template的完整代码
def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def generate_banner(msg, style=dots_style):
    print '--- start of banner ---'
    print style(msg)
    print '--- end of banner ---\n\n'


def template_main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style, cow_style)]


if __name__ == '__main__':
    main()
    bfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_bfs_path)
    dfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_dfs_path)
    print 'bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found')
    print 'dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found')
    template_main()