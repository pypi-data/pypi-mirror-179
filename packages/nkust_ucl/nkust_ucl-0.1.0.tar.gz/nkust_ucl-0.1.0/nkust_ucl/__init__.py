def addition(a,b):
    h=b-a+1
    s=(a+b)*h/2
    return int(s)

def addition_odd(a,b,c):
    s = 0
    for i in range(a,b+1,c):
        s+=i
        print(i)
    return s

def addition_prime(a,b):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    s = 0
    for i in prime:
        if a <= i and i <= b:
            s+=i
    return s

