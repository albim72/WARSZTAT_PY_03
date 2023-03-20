#przykład 1
import math

def fy(k):
    return k**5

n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c+n+fy(b)
    return n

print(policz(3,4,8,6))
print(n)

#przykład 2

def gx(n,m=1,k=2,h=2):
    return math.sqrt(n+m)*k-h

print(gx(5,8,2,5))
print(gx(7,8))
print(gx(7))
print(gx(11,11,11))

print(gx(10,h=46))

#przykład 3
def rank(*lang,nrrank):
    print(f'ranking nr {nrrank} języków programowania:  1->{lang[0]}, 2->{lang[1]}, 3-> {lang[2]}')

rank("Go","Ruby","Java",nrrank=67)
rank("Python","Go","C#","Ruby","Java",nrrank=69)


