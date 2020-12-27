nodes, lines, start=list(map(int, input().split(' ')))
com=dict()

for i in range(nodes):
    com[i+1]=set()
for i in range(lines):
    a,b = list(map(int,input().split(' ')))
    com[a].add(b)
    com[b].add(a)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop(0)]:
            if i not in visited_bfs:
                visited_bfs.append(i)
                queue.append(i)
    

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited_dfs:
            visited_dfs.append(i)
            dfs(i, dic)




visited_dfs=[start]
dfs(start,com)

print(*visited_dfs)

visited_bfs=[start]
bfs(start, com)

print(*visited_bfs)





