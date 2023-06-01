def solve(s):
    line = s.split()
    print(line[0][0])

    for i in range(len(line)):
        temp = str(line[i][0].upper())
        line[i][0] = temp
    return str(line)


if __name__ == "__main__":
    s = input()

    result = solve(s)
    print(result + '\n')