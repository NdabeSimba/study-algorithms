# https://www.acmicpc.net/problem/10988
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

# https://www.acmicpc.net/problem/2738
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

# https://www.acmicpc.net/problem/1271

# mon, peo = map(int, input().split())
# print(mon // peo, mon % peo,sep="\S")

# ----------------------------------------------------------------------

# https://www.acmicpc.net/problem/1809

# golfscript
# "(___)
# (o o)____/
#  @@      \\
#   \\ ____,/
#   //   //
#  ^^   ^^"

# ----------------------------------------------------------------------

# A = int(input())
# B = int(input())
# print(A + B, A - B, A * B, sep="\S")

# ----------------------------------------------------------------------

# print(*[i+1 for i in range(int(input()))],sep="\S")

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

# print(*reversed(range(1,int(input())+1)),sep="\S")

# ----------------------------------------------------------------------

# print(*sorted(list(map(int, input().split()))))

# ----------------------------------------------------------------------

# if __name__ == '__main__':
#     S = int(input())
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

# https://www.acmicpc.net/problem/4299
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

# https://www.acmicpc.net/problem/3765
# try:
#     while True :
#         print(input())
# except:
#     exit()

# ----------------------------------------------------------------------

# num = int(input())
# for i in range(num):
#     print(str(i+1)+'.',input())

# ----------------------------------------------------------------------

# for _ in range(int(input())):
#     print(input().lower())

# ----------------------------------------------------------------------

# vac = int(input())
# math = int(input())
# lang = int(input())
# max_m = int(input())
# max_l = int(input())

# if math / max_m > math // max_m:
#     day_m = math // max_m + 1
# else:
#     day_m = math // max_m

# if lang / max_l > lang // max_l:
#     day_l = lang // max_l + 1
# else:
#     day_l = lang // max_l

# print(vac - max(day_m, day_l))

# ----------------------------------------------------------------------

# burg1 = int(input())
# burg2 = int(input())
# burg3 = int(input())
# drink1 = int(input())
# drink2 = int(input())

# print(min(burg1, burg2, burg3) + min(drink1, drink2) - 50)

# ----------------------------------------------------------------------

# tm1 = int(input())
# tm2 = int(input())
# tm3 = int(input())
# tm4 = int(input())

# print((tm1 + tm2 + tm3 + tm4) // 60)
# print((tm1 + tm2 + tm3 + tm4) % 60)

# ----------------------------------------------------------------------

# def split_and_join(line):
#     line = line.strip().split(" ")
#     return "-".join(line)

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# ----------------------------------------------------------------------

# https://www.acmicpc.net/problem/5575
# for i in range(3):
#     fh, fm, fs, lh, lm, ls = map(int, input().split())
#     time = ((lh * 3600) + (lm * 60) + ls) - ((fh * 3600) + (fm * 60) + fs)
#     print(time // 3600, (time % 3600) // 60, (time % 3600) % 60)

# ----------------------------------------------------------------------

# K, N, M = map(int, input().split())
# print(((K * N) - M) if (K * N) - M >= 0 else 0)

# ----------------------------------------------------------------------

# p1t, p1b = map(int, input().split())
# p2t, p2b = map(int, input().split())

# if (p1t * 3 + p1b) == (p2t * 3 + p2b):
#     print("NO SCORE")
# else:
#     if (p1t * 3 + p1b) > (p2t * 3 + p2b):
#         print(1, (p1t * 3 + p1b) - (p2t * 3 + p2b))
#     else:
#         print(2, (p2t * 3 + p2b) - (p1t * 3 + p1b))

# ----------------------------------------------------------------------

# sum = 0
# for i in range(5):
#     num = int(input())
#     sum += num if num > 40 else 40
# print(sum//5)

# ----------------------------------------------------------------------

# S = input()
# lis = [0]*26

# for i in S:
#     lis[ord(i)-97] += 1

# print(*lis)

# ----------------------------------------------------------------------

