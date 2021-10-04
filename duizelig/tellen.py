import time
x = 50  
i = x + 1
while x <= 1000:
    time.sleep(0.5)
    o = i + x
    print(str(i) + ' + ' + str(x) +  ' = ' + str(o) )
    x = x + i
    i = i + 1
    
