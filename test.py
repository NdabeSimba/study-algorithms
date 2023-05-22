# baekjoon 10988 https://www.acmicpc.net/problem/10988
# 31256	kb 40 ms

# word = list(input())
# result = True
# for i in range(len(word) // 2):
#     if word[i] != word[-i - 1]:
#         result = False
#         break
# if result == True:
#     print(1)
# else:
#     print(0)

# ----------------------------------------------------------------------

# baekjoon 2738 https://www.acmicpc.net/problem/2738
# 31256 kb, 60 ms
# 31256 kb, 56 ms

# N, M = map(int, input().split())
# lis1 = []
# lis2 = []
# result = []
# for i in range(N):
#     lis1.append(list(map(int, input().split())))
# for i in range(N):
#     lis2.append(list(map(int, input().split())))
# for i in range(N):
#     for j in range(M):
#         result.append(int(lis1[i][j]) + int(lis2[i][j]))
# for i in range(0, len(result), 3):
#     print(*result[i : i + 3])

# N, M = map(int, input().split())
# lis1 = []
# lis2 = []
# for i in range(N):
#     lis1.append(list(map(int, input().split())))
# for i in range(N):
#     lis2.append(list(map(int, input().split())))
# for i in range(N):
#     for j in range(M):

#         print(int(lis1[i][j]) + int(lis2[i][j]), end=' ')
#     print()

# ----------------------------------------------------------------------

# baekjoon 1271 https://www.acmicpc.net/problem/1271

# mon, peo = map(int, input().split())
# print(mon // peo, mon % peo,sep="\n")

# ----------------------------------------------------------------------

# baekjoon 1809 https://www.acmicpc.net/problem/1809

# golfscript
# "(___)
# (o o)____/
#  @@      \\
#   \\ ____,/
#   //   //
#  ^^   ^^"