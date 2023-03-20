#przykład 1

def fy(k):
    return k**5

n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c+n+fy(b)
    return n

print(policz(3,4,8,6))
print(n)

