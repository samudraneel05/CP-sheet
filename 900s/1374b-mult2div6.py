t = int(input())
for _ in range(t):
    n = int(input())
    ncopy = n
    flag = False
    a,b = 0,0
    while ncopy>1:
        if ncopy%2==0:
            ncopy = ncopy//2
            a += 1
        elif ncopy%3==0:
            ncopy = ncopy//3
            b +=1
        else:
            flag = True
            break
    if flag or a>b:
        print(-1)
    else:
        print(2*b-a)

    