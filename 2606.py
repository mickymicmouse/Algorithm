N = int(input())
com = dict()
for i in range(N):
    com[i+1]=set()

n = int(input())
for i in range(n):
    a,b = list(map(int, input().split(' ')))
    com[a].add(b)
    com[b].add(a)


def bfs(start, com):
    queue = [start]
    visited=[start]
    while queue:
        for i in com[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited
bfs(1,com)
print(len(visited)-1)


def dfs(start, com):
    
    for i in com[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, com)

visited=[1]
dfs(1,com)
print(len(visited)-1)
visited


