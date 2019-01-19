sprite = """
000000000001100000000000
000000000001100000000000
000000000001100000000000
000000000001100000000000
000000000111111000000000
000000011111111100000000
000000110000000110000000
000001101100011001100000
000001100000000001100000
000001100000000001100000
000001100111110001100000
000001100000000001100000
000000011111111110000000
000000001111111100000000
000000000000110000000000
000000000001100000000000
000000000001100000000000
000000000001100000000000
000001111111111111100000
001111111111111111111100
000000000000000000000000
"""

print(sprite)
print(len(sprite))
cleanSprite= sprite.replace("\n","")  #strips the \n new line off the sprite so it has
print(len(cleanSprite)) ## you can check the lenght so make sure they have created a real sprite
print(cleanSprite)

"""
split every 8 character into a list
then use int('11111111',2) to get the decimal
"""

binaryList = []
while cleanSprite:       
    binaryList.append(cleanSprite[:8])   # appends the first 8 characterss    
    cleanSprite = cleanSprite[8:] #re- asigns the string removing the fist 8 characters

print(binaryList, len(binaryList))  

decList=[]
for bnum in binaryList:
    decList.append(int(bnum,2))

print(decList, len(decList))    


