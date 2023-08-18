def calculate_position(x,v,a,t):
     new_x = x + (v * t) + (1/2)*(a * (t ** 2))
     print("x is now located at: ", new_x)


x = 3
v = 3/2
a = 1.3
t = 5

calculate_position(x, v, a, t)


