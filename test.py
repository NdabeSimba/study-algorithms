# baekjoon 10988 https://www.acmicpc.net/problem/10988
# 31256	kb 40 ms
word = list(input())
result = True
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        result = False
        break
if result == True:
    print(1)
else:
    print(0)

