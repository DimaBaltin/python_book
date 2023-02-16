digits = (1, 2, 3, 4)
rightplace=0
guessed=0
while rightplace<4 and guessed<4:

    user=input(f"Enter four digits: ")
    num1=int(user[0])
    num2=int(user[1])
    num3=int(user[2])
    num4=int(user[3])
    list=(num1, num2, num3, num4) 

    number=0
    guessed=0
    rightplace=0

    quantity=0
    
    while number<4:
    
        while quantity<4:
            if list[number]==digits[quantity]:
                guessed=guessed+1
                if quantity == number:
                    rightplace=rightplace+1
                break
            else:     
                quantity=quantity+1
        number=number+1
    print("You guessed: ",guessed)
    print("On the right place: ",rightplace)
        
print ("You win!", user)

