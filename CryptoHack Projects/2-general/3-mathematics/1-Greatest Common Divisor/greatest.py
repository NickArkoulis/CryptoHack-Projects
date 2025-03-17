def euclid_gcd(x, y):
    if x < y:
        return euclid_gcd(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    print("\n[+] GCD: {}".format(x))
    return x
# we set the numbers given
a = 66528
b = 52920

euclid_gcd(a, b) 
