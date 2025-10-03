def factorial(n):
    if n==0:
        return 1;
    else:
        return n*factorial(n-1)
    pass

def fibonacii(n):
    if n<2:
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)

def HanoiTower(n, s, d, m):
    if n<1:
        return
    if n==1:
        print(f"Move disk {n} from {s} to {d}")
    else:
        HanoiTower(n-1, s, m, d)
        print(f"Move disk {n} from {s} to {d}")
        HanoiTower(n-1, m, d, s)
        
n = int(input("Input n = "))
print(f"{n}! = {factorial(n)}")
for i in range (n):
    print(fibonacii(i),end=' ')
print("\n----")
n = int(input("Input number of disk n = "))
HanoiTower(n, 'A', 'C', 'B')