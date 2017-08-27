N = int(input())

for i in range(1,N+1):
    a=input()
    e=''
    o=''
    for j in range(0,len(a)):
        if (j%2==0):
            e=e+a[j]
        else:
            o=o+a[j]
    print('{0} {1}'.format(e,o))
