g=-9.81
    #Gravity. The gravity displayed is the gravity on earth
k=5
    #Initial Velocity
h=1.8
    #Hight
start=-3
    #Starting Time
end=3
    #Ending Time
for x in range (start,end+1):
    y=-g*x**2+k*x+h
    y=round(y,2)
    print("("+str(x)+","+str(y)+")")
