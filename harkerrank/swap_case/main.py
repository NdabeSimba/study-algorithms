def swap_case(s):
    line = list(input())
    for i in range(len(line)):
        if line[i].isupper() == True:
            line[i] = line[i].lower()
        else:
            line[i] = line[i].upper()
        print(*line,sep='')
        return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)