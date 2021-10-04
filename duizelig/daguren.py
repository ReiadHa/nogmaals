import time
nummer = 1
am = ':00 am'
pm = ':00 pm'
while nummer <= 12:
    time.sleep(0.2)
    print(str(nummer) + str(am))
    nummer = nummer + 1
else :
    for x in range(1,13):
        time.sleep(0.2)
        print(str(x) + str(pm))
        nummer = nummer + 1