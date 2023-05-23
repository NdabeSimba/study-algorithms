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

# ----------------------------------------------------------------------

# baekjoon 2338 https://www.acmicpc.net/problem/2338

# A = int(input())
# B = int(input())
# print(A + B, A - B, A * B, sep="\n")

# ----------------------------------------------------------------------

# print(*[i+1 for i in range(int(input()))],sep="\n")

# ----------------------------------------------------------------------

# line = list(input())
# for i in range(len(line)):
#     if line[i].isupper() == True:
#         line[i] = line[i].lower()
#     else:
#         line[i] = line[i].upper()
# print(*line,sep='')

# ----------------------------------------------------------------------

hashmap = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
}

print(hashmap[input()])