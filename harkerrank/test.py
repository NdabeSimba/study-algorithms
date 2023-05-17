# print("Hello, World!")

# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2 == 1:
#         print("Weird")
#     if 2 <= n <= 5 and n%2 == 0:
#         print("Not Weird")
#     elif 6 <= n <= 20 and n%2 == 0:
#         print("Weird")
#     elif 20 < n and n%2 == 0:
#         print("Not Weird")

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i**2)

# def is_leap(year):
#     leap = False
    
#     if year % 4 == 0:
#         leap = True
#         if year %100 == 0:
#             leap = False
#             if year % 400 == 0:
#                 leap = True
    
#     return leap

# year = int(input())
# print(is_leap(year))

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end='')