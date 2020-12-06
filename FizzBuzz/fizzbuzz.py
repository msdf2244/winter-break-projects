def fizzbuzz(num, x, y):
    result = ''

    if num % x == 0:
        result += "Fizz"

    if num % y == 0:
        result += "Buzz"

    if num % x != 0 and num % y != 0:
        result = num
    
    return result

def solver(x, y , n):

    for i in range(1, n + 1):
        print(fizzbuzz(i, x, y))

n, x, y = input("").split()

solver(int(n), int(x), int(y))
