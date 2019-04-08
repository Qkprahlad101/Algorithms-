def heapify_bottomup(a, n):
    for i in range((int(n / 2)) - 1, -1, -1):
        p = i
        item = a[p]
        c = 2 * p + 1

        while c <= n - 1:
            if c + 1 <= n - 1 and a[c] < a[c + 1]:
                c = c + 1
            if item < a[c]:
                a[p] = a[c]
                p = c
                c = 2 * p + 1
            else:
                break

        a[p] = item
    return a

def swap(a,l,m):
    t = a[l]
    a[l] =a[m]
    a[m] = t


a = []
inp = input().split()
for i in inp:
    a.append(int(i))
print(a)
n = len(a)
print("Length of Heap is ", n)
a = heapify_bottomup(a, n)
print("Heap is ",a)

for k in range(n-1,-1,-1):
    swap(a,0,k)
    heapify_bottomup(a,k)

print("Elements of Heap in Ascending Order is: ",end="\n")
for i in a:
    print(int(i),end=" ")
