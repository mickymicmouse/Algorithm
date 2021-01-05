import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
n_list = list(map(int,input().split(' ')))
m = int(input())
m_list = list(map(int,input().split(' ')))
n_list.sort()

def search(x, line):
    num = len(line)
    

    if num==0:
        return False
    else:
        if x>line[num//2]:
            return search(x, line[num//2+1:])
        elif x<line[num//2]:
            return search(x,line[:num//2])
        else:
            return True
    

for i in m_list:
    result = search(i, n_list)

    if result:
        print(1)
    else:
        print(0)
    