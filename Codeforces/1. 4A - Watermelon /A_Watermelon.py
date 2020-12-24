val=int(input())
def watermelon(val):
    if(val==2):
        return 'NO'
    elif(val % 2 !=0):
        return 'NO'
    else:
        return 'YES'
print(watermelon(val))
