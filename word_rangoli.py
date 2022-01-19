n = int(input())
s = ""
for i in range(1,27):
    s = s+chr(i+96)
s = "-".join(list(s))
s1 = ""
for i in range(2*n-2):
    s1 = s1 + "-"
a = len(s1)
b = 2*n-3
c = 2*n-1
for i in range(1,n+1):
    if i==n:
        print(s1[0:a]+s[2*n-2::-1]+s[c:2*n-1])
    else:
        print(s1[0:a]+s[2*n-2:b:-1]+s[c:2*n-1]+s1[0:a])
    a -= 2
    b -= 2
    c -= 2
a = 2
b = 2
c = 4
for i in range(1,n): 
    print(s1[0:a]+s[2*n-2:b-1:-1]+s[c-1:2*n-1]+s1[0:a])
    a += 2
    b += 2
    c += 2