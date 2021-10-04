 
 
x = input('type een woord hier: ')
i = 0
while x != 'quit':
    x = input('type hier nogmaals een woord: ')
    i = i + 1
    if x == 'quit' :
        print(('je hebt ') + str(i) + (' keer geprobeerd tot at je aan de goede woord komt. ') )
        break


        
