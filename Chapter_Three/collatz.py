def collatz(n):
    while n != 1:
        if n % 2 == 0:
            print(str(n//2))
            n = n//2
        elif n % 2 == 1:
            print(str((n*3)+1))
            n = (n*3) + 1
            
print('Enter a number to view its progression through the Collatz sequence.')

n = int(input())

collatz(n)
