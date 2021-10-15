r,g,b = map(int,input().split())

R = r%3
G = g%3
B = b%3

a=r//3 + b//3 + g//3 + min(R,B,G)

if (R == 2 and G == 2 and B == 0 and b != 0 )\
    or( G == 2 and B == 2 and R == 0 and r != 0) \
    or (B == 2 and R == 2 and G == 0 and g != 0):

    a+=1

print(a)

