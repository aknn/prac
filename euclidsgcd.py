"""
euclids algorithm for gcd

"""
def gcd(a,b):
    print(a,b)
    if b==0:
        return a
    return gcd(b,a%b)
