import time, sys

maandag   = "maandag"
dinsdag   = """
maandag 
dinsadg"""
woensdag  = """
maandag
dinsdag
woensdag"""
donderdag = """
maandag
dinsdag
woensdag
donderdag"""
vrijdag   =  """
maandag
dinsdag
woensdag
donderdag
vrijdag"""
zaterdag  =  """
maandag
dinsdag
woensdag
donderdag
vrijdag
zaterdag"""
zondag    =  """
maandag
dinsdag
woensdag
donderdag
vrijdag
zaterdag
zondag"""

x = input('vul hier één dag van de week in: ') 
while x == 'maandag':
 print(maandag)
 break

while x == 'dinsdag':
 print(dinsdag)
 break
    

while x == 'woensdag':
 print(woensdag)
 break
while x == 'donderdag':
    print(donderdag)
    break
 
while x == 'vrijdag':
    print(vrijdag)
    break

while x == 'zaterdag':
    print(zaterdag)
    break

while x == 'zondag':
    print(zondag)
    break