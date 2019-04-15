def heapify_topdown(a, n):
    for i in range(n-1, -1,-1):
        c = i
        p = int((c - 1) / 2)
        item = a[i]

        while item > a[p] and c> 0:
            a[c] = a[p]
            c = p
            p = int((c - 1) / 2)
        a[c] = item
    return a


a = []
f = 1
while f == 1:
    print("1-Insert \n2-Display \n3-No of nodes\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        inp = int(input("Enter the Value: "))
        a.append(inp)
        n = len(a)
        if n>1:
                print(a)
                a = heapify_topdown(a, n)

    elif choice == 2:
        for i in a:
            print(i, end=" ")
        print('\n')

    elif n == 3:
        print(n)

    else:
        f = 0


