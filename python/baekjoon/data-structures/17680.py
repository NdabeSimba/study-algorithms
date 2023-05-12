import sys
input = sys.stdin.readline

num = int(input())
num_lis = []

for _ in range(num):
    num_lis.append(int(input()))

num_lis.append(0)

for i in reversed(num_lis):
    print(i)