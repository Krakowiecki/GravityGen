g=-9.81
k=5
h=1.8
start=-3
end=3
for x in range (start,end+1):
    y=-g*x**2+k*x+h
    y=round(y,2)
    print("("+str(x)+","+str(y)+")")
