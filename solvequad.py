def solvequad(a, b, c):
    sol1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    sol2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print("the first solution is: ", sol1)
    print("the second solution is: ", sol2)

a = int(input("what is the value of a: "))
b = int(input("what is the value of b: "))
c = int(input("what is the value of c: "))

print("there are two possib solutions: ")
solvequad (a, b, c)










