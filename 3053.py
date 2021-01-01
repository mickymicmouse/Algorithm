import math

r = int(input())
def uclidean(r):
    area = math.pow(r,2)*math.pi
    print(round(area, 6))

def taxi(r):
    area = math.pow(r,2)*2
    print(round(area,6))

uclidean(r)
taxi(r)