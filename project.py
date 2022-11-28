
def isPrime(n):
    if n==2:
        return True
    else:
        for i in range(2,n):
            if n%i!=0:
                if i==(n-1):
                    return True
            else:
                return False
def inrange(n):
    for i in range(2,n+1):
        if isPrime(i):
            a=str(i)
            if a[::-1]==a:
                print(a,end=" ")
        else:
            continue         
n=int(input("n:   "))
inrange(n) 