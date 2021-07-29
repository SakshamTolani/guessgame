import random
def g(a,b):
    x=random.randint(a,b)
    y=int(input("Guess a number:"))
    t=0
    while True:
        if x != y:
            if y<x:
                print("Too low. Guess a bit high") #DRY- Dont Repeat Yourself
            else:
                print("Too High. Guess a bit low")
            y=int(input("Guess again:"))
            t+=1
            continue
        else:
            print(f"You guessed correctly in {t+1} times \n")
            return t+1
            break 
if __name__=='__main__'   :
    a=int(input('Enter lower limit: '))
    b=int(input('Enter upper limit: '))
    print('Player 1, please start! \n')
    p1=g(a,b)
    print('Player 2, please start! \n')
    p2=g(a,b)
    if p1<p2:
        print('Congrats! Player 1 wins')
    elif p1>p2:
        print('Congrats! Player 2 wins')
    else:
        print('Ohh!, Its a Tie')



