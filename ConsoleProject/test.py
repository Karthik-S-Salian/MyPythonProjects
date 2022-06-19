from math import log

x=-0.9
value_i=log(x+1) -(2*x)/(2+x)
while True:
    value_f=log(x+1) -(2*x)/(2+x)
    if value_f <value_i:
        status="decreasing"
    else:
        status="increasing"
    value_i=value_f
    x=x+0.1
    if x>10:
        break
    print(f"{x =:.2f}{     value_f = :.2f}{    status = }")



