#큰수의 법칙
import sys
input = sys.stdin.readline
n, m, k =map(int,input().split())
num =sorted(list(map(int,input().split())) ,reverse = True )
print(num)
s1= ( m//(k+1) ) * ( k * num[0] + num[1])

s2=( m % (k+1) ) * num[0]

print(s1 + s2)