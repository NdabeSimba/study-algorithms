K, D, A = map(int, input().split("/"))
if D != 0:
    if K + A >= D:
        print("gosu")
    else:
        print("hasu")
else:
    print("hasu")