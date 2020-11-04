"""
euclids algorithm to find gcd

"""
def gcd(a,b):
    print(a,b)
    if b==0:
        return a
    return gcd(b,a%b)
