n = int(input("input your n: "))

def print_fancybox(n):
    print("----------------")
    for i in range(n):
        print("|\/\/\/\/\/\/\/|")
    for i in range(n):
       print("|/\/\/\/\/\/\/\|")
    print("----------------")

print("Fancybox")
print_fancybox(4)

def print_pyramid(n):
    for i in range(n):
        space = " " * (n - i - 1)
        star = "*=" * i
        print(space + "/" + star + "\\" + space)
    
    print("-" * (2 * n))

print("Pyramid")
print_pyramid(n)

def tip(n):
  for i in range(n-1):
    row =" "*(n-i-1)+"/"*(i+1)+"**"+"\\"*(i+1)
    print(row) 
  print("+" + n*"=*" +"+")

def bottom(n):
  for i in range(n-1):
    row =" "*(n-i-1)+"/"*(i+1)+"**"+"\\"*(i+1)
    print(row) 

def body(n):
  m = int(n/2)
  for i in range(m):
      print("|"+"."*(m-i-1)+"/\\"*(i+1)+"."*(m-i-1)+"."*(m-i-1)+"/\\"*(i+1)+"."*(m-i-1)+"|")
  for i in range(m):
      print("|"+"."*(i)+"\\/"*(m-i)+"."*(i)+"."*(i)+"\\/"*(m-i)+"."*(i)+"|")

  print("+" + n*"=*" +"+")
  for i in range(m):
    print("|"+"."*(i)+"\\/"*(m-i)+"."*(i)+"."*(i)+"\\/"*(m-i)+"."*(i)+"|")
  for i in range(m):
    print("|"+"."*(m-i-1)+"/\\"*(i+1)+"."*(m-i-1)+"."*(m-i-1)+"/\\"*(i+1)+"."*(m-i-1)+"|")
  

  print("+" + n*"=*" +"+")

def print_rocketship2(n):
   tip(n*2)
   body(n*2)
   bottom(n*2)

def print_rocketship1():
   print_rocketship2(3)
 
print("Rocketship")


print_rocketship1()


print("print_rocketship2")

print_rocketship2(n)



