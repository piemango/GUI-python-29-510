import random
score = 0
strike = 10
spare = 10
for i in range (11):
    pin = random.randint (0,10)
    pinleft = 10
    print("press enter to roll the ball")
    if pin == 10:
        print ("strike !!!!!")
        score += 10
    else:
        print("round 2")
        pinleft -= pin
        print ("pint left",pin)
        print("press enter to roll the ball")
        pin = random.randint (0,10)
        if pin + pinleft == 10:
                            print ("flaree")
                            score +=10
        else:
            print("open flame")
            score + pin + pinleft
print("your score is ",score)