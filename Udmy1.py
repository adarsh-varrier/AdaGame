def game_list(l):
    print("This is current option:",l)

def getposition():
    pos="Wrong"
    while pos not in ['0','1','2']:
        pos=input("Enter any position:")
        if pos not in ['0','1','2']:
            print("Enter option from given list!")
    return int(pos)
def replace(l,n):
    userch=input("Enter a String:")
    l[n]=userch
    return l
def gamechoice():
    choise='Wrong'
    while choise not in ['Y','N']:
        choise=input("Keep playing ?(Y/N):-")
        if choise not in ['Y','N']:
            print("Wrong Input!")
    if choise == 'Y':
        return True
    else:
        return False

l=[0,1,2]
game_on=True
while game_on:
    game_list(l)
    n=getposition()
    li=replace(l,n)
    game_list(li)
    game_on=gamechoice()
print("The Updated List:",li)
