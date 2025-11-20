import random
print("Enter range in which you want to play:")
a=int(input("Upper limit:"))
b=int(input("Lower limit:"))
random_int=random.randint(b,a)

print("You can start the game!!")
cnt=0
while cnt<=7:
    input_val=int(input("Enter your guess:"))
    
    if input_val>random_int:
            print("Try Lower number")
    elif input_val<random_int:
            print("Try Higher number")
    else:
            print("You GUESSED it right!!")
            print(random_int)
            break
    cnt+=1

if cnt==7:
    print("Try again next time!!")