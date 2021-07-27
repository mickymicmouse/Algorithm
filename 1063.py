import sys
input = sys.stdin.readline

king, stone, n = input().split(' ')

oper=[]
for i in range(n):
    oper.append(input().strip())

cols=['A','B','C','D','E','F','G','H']
rows=['1','2','3','4','5','6','7','8']

col = king[0]
row = king[1]
stone_col = stone[0]
stone_row = stone[1]

def R():
    global row, col
    row_idx = rows.index(row)
    if row_idx+1>=8:
        return
    else:
        row = rows[row_idx+1]
    if row==stone_row and col==stone_col:
        R()

def L():
    global row,col
    row_idx = rows.index(row)
    if row_idx-1<0:
        return
    else:
        row = rows[row_idx-1]
    if row==stone_row and col==stone_col:
        L()
    
def B():
    global row,col
    col_idx = cols.index(col)
    if col_idx+1>=8:
        return
    else:
        col = cols[col_idx+1]
    if row==stone_row and col==stone_col:
        B()

def T():
    global row,col
    col_idx = cols.index(col)
    if col_idx-1<0:
        return
    else:
        col = cols[col_idx-1]
    if row==stone_row and col==stone_col:
        T()

def RT():
    global row,col
    row_idx = rows.index(row)
    col_idx = cols.index(col)
    if col_idx+1>=8 or row_idx-1<0:
        return
    else:
        row = rows[row_idx-1]
        col = cols[col_idx+1]
    if row==stone_row and col==stone_col:
        RT()

def LT():
    global row,col
    row_idx = rows.index(row)
    col_idx = cols.index(col)
    if col_idx-1<0 or row_idx-1<0:
        return
    else:
        row = rows[row_idx-1]
        col = cols[col_idx-1]
    if row==stone_row and col==stone_col:
        LT()

def RB():
    global row,col
    row_idx = rows.index(row)
    col_idx = cols.index(col)
    if col_idx+1>=8 or row_idx+1>=8:
        return
    else:
        row = rows[row_idx+1]
        col = cols[col_idx+1]
    if row==stone_row and col==stone_col:
        RB()

def LB():
    global row,col
    row_idx = rows.index(row)
    col_idx = cols.index(col)
    if col_idx-1<0 or row_idx+1>=8:
        return
    else:
        row = rows[row_idx+1]
        col = cols[col_idx-1]
    if row==stone_row and col==stone_col:
        LB()



for order in oper:
    if order == 'R':
        R()
    if order == 'L':
        L()
    if order == 'B':
        B()
    if order == 'T':
        T()
    if order == 'RT':
        RT()
    if order == 'LT':
        LT()
    if order == 'RB':
        RB()
    if order == 'LB':
        LB()
print
