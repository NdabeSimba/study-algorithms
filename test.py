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

# hashmap = {
#     "A+": 4.3,
#     "A0": 4.0,
#     "A-": 3.7,
#     "B+": 3.3,
#     "B0": 3.0,
#     "B-": 2.7,
#     "C+": 2.3,
#     "C0": 2.0,
#     "C-": 1.7,
#     "D+": 1.3,
#     "D0": 1.0,
#     "D-": 0.7,
#     "F": 0.0,
# }

# print(hashmap[input()])

# ----------------------------------------------------------------------

# hr, min, sec = map(int, input().split())
# plus_sec = int(input())

# sec += plus_sec % 60
# plus_sec = plus_sec // 60

# if sec >= 60:
#     sec -= 60
#     min += 1

# min += plus_sec % 60
# plus_sec = plus_sec // 60

# if min >= 60:
#     min -= 60
#     hr += 1

# hr += plus_sec % 24

# if hr >= 24:
#     hr -= 24

# print(hr, min, sec)

# ----------------------------------------------------------------------

# print(*reversed(range(1,int(input())+1)),sep="\n")

# ----------------------------------------------------------------------

# print(*sorted(list(map(int, input().split()))))

# ----------------------------------------------------------------------

# if __name__ == '__main__':
#     n = int(input())
#     lis = map(int,input().split())
#     print(hash(tuple(lis)))

# ----------------------------------------------------------------------

# while True:
#     line = list(input().lower())
#     count = 0
#     if line[0] == '#':
#         break
#     else:
#         for i in range(len(line)):
#             if line[i] in ['sum','e','i','o','u']:
#                 count += 1
#         print(count)

# ----------------------------------------------------------------------

# while True:
#     name, age, weight = map(str, input().split())
#     if name == "#" and age == weight == '0':
#         break
#     if int(age) > 17 or int(weight) >= 80:
#         print(name, "Senior")
#     else:
#         print(name, "Junior")

# ----------------------------------------------------------------------

# Lj, area = map(int, input().split())
# p1, p2, p3, p4, p5 = map(int, input().split())
# print(
#     p1 - (Lj * area),
#     p2 - (Lj * area),
#     p3 - (Lj * area),
#     p4 - (Lj * area),
#     p5 - (Lj * area),
# )

# ----------------------------------------------------------------------

# R1, S = map(int, input().split())
# print(2*S-R1)

# ----------------------------------------------------------------------

# sum, dif = map(int, input().split())

# if sum < dif:
#     print(-1)
# else:
#     a = (sum + dif) // 2
#     b = (sum - dif) // 2
#     if (a + b) == sum and (a - b) == dif:
#         print(max(a, b), min(a, b))
#     else:
#         print(-1)

# ----------------------------------------------------------------------

# try:
#     while True :
#         print(input())
# except:
#     exit()

