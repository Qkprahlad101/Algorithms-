def heapify_bottomup(a,n):
        for i in range((int(n/2))-1,-1,-1):
                p = i
                item = a[p]
                c = 2*p +1

                while c<=n-1:
                        if c+1<= n-1 and a[c]<a[c+1]:
                            c=c+1
                        if item<a[c]:
                            a[p]=a[c]
                            p=c
                            c=2*p +1
                        else:
                            break

                a[p]=item
        return a

a=[]
inp=input().split()
for i in inp:
    a.append(int(i))

print(a)
n = len(a)
print(n)
a=heapify_bottomup(a,n)
print(a)
