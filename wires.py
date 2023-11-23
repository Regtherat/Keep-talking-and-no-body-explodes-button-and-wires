
print("Hello what section of the bomb are you on?")
print("""
       Wires=1
       Button=2
       When asked questions in this only answer with yes or no
       \n""")
whichone =  input()


if whichone == ("1"):




    print("ok then how many wires are there?")
    howmany = input()
    if howmany == ("3"):
        print("are there any red wires?")
        redw = input()
        if redw.upper() == "YES":
            print("is the last wire white?")
            whitewire = input()
            if whitewire.upper() == "YES":
                print("cut the last wire")
            elif whitewire.upper() == "NO":
                print("is there more than one blue wire?")
                blue = input()
                if blue.upper() == "YES":
                    print("cut the last blue wire")
                elif blue.upper() == "NO":
                    print("cut the last wire")
        
        
                
        elif redw.upper() == "NO":
            print("cut second wire")

    elif howmany == ("4"):
            print("is there more than one red wire and is the last digit of the serial number on the bomb odd?")
            redp = input()
            if redp.upper() == "YES":
                print("cut the last wire")
            elif redp.upper() == "NO":
                print("is the last wire yellow and there are no red wires?")
                yellow = input()
                if yellow.upper() == "YES":
                    print("cut the first wire")
                elif yellow.upper() == ("NO"):
                    print("is there exactly one blue wire?")
                    exactblue = input()
                    if exactblue.upper() == "YES":
                        print("cut first wire")
                    elif exactblue.upper() == "NO":
                        print("is there more than one yellow wire?")
                        yellow1 = input()
                        if yellow1 == "YES":
                            print("cut the last wire")
                        elif yellow1 == "NO":
                            print("cut the second wire")
                            
    elif howmany == "5":
            print("is the last wire black and the last digit of the serial number odd")
            redq = input()
            if redq.upper() == "YES":
                print("cut the 4th wire")
            elif redq.upper() == "NO":
                    print("is the there exactly one red wire and more than one yellow wire")
                    yellow2 = input()
                    if yellow2.upper() == "YES":
                        print("cut the first wire")
                    elif yellow2.upper() == ("NO"):
                        print("is there no black wires?")
                        exactblue2 = input()
                        if exactblue2.upper() == "YES":
                            print("cut 2nd wire")
                        elif exactblue2.upper() == "NO":
                            print("cut the 1st wire")
                        
    elif howmany == "6":
            print("are there no yellow wires and the last digit of the serial number odd?")
            redf = input()
            if redf.upper() == "YES":
                print("cut the 3th wire")
            elif redf.upper() == "NO":
                print("is there exactly one yellow wire and more than one white wire?")
                yellowf = input()
                if yellowf.upper() == "YES":
                    print("cut the fourth wire")
                elif yellowf.upper() == ("NO"):
                    print("are there are no red wires?")
                    exactbluef = input()
                    if exactbluef.upper() == "YES":
                        print("cut last wire")
                    elif exactbluef.upper() == "NO":
                        print("cut the 4th wire")


if whichone ==("2"):
    print("Is the button blue and says abort?")
    button = input()
    if button.upper() == "YES":
        print("what color is the strip?")
        strip = input()
        if strip.upper() == "BLUE":
            print("release when the countdown timer has a 4 in any position.")
        elif strip.upper() == "WHITE":
            print("release when the countdown timer has a 1 in any position.")
        elif strip.upper == ("YELLOW"):
            print("release when the countdown timer has a 5 in any position.")
        elif strip.upper == ("OTHER"):
            print("release when there is a 1 in any position")
        else:
            print("that is not a color")
    elif button.upper() == "NO":
        print("is there more than one battery on the bomb and the button says detonate?")
        bomb = input()
        if bomb.upper() == "YES":
            print("press and release the button")
        elif bomb.upper() == "NO":
            print("is the botton white and is there a lit indicator labeled CAR?")
            car = input()
            if car.upper() == "YES":
                print("what color is the strip?")
                strip1 = input()
                if strip1.upper() == "BLUE":
                    print("release when the countdown timer has a 4 in any position.")
                elif strip1.upper() == "WHITE":
                    print("release when the countdown timer has a 1 in any position.")
                elif strip1.upper() == ("YELLOW"):
                    print("release when the countdown timer has a 5 in any position.")
                elif strip1.upper() == ("OTHER"):
                    print("release when there is a 1 in any position")
                else:
                    print("that is not a color")
            
            elif car.upper() == "NO":
                print("is there more than 2 batterys on the bomb and there is a lit indicator with label FRK")
                FRK = input() 
                if FRK.upper() == "YES":
                    print("press and release the button")
                elif FRK.upper() == "NO":
                    print("is the button yellow?")
                    yell=input()
                    if yell.upper() == "YES":
                        print("what color is the strip?")
                        strip2 = input()
                        if strip2.upper() == "BLUE":
                            print("release when the countdown timer has a 4 in any position.")
                        elif strip2.upper() == "WHITE":
                            print("release when the countdown timer has a 1 in any position.")
                        elif strip2.upper() == ("YELLOW"):
                            print("release when the countdown timer has a 5 in any position.")
                        elif strip2.upper() == ("OTHER"):
                            print("release when there is a 1 in any position")
                        else:
                            print("that is not a color")
                    elif yell.upper() == "NO":
                        print("is the button red and says hold?")
                        red = input()
                        if red.upper() == "YES":
                            print("press and release the button")
                        elif red.upper() == "NO":
                            print("hold the button")
                            print("""    
    Blue strip: release when the countdown timer has a 4 in any position.
    White strip: release when the countdown timer has a 1 in any position.
    Yellow strip: release when the countdown timer has a 5 in any position.
    Any other color strip: release when the countdown timer has a 1 in any position.
\n""")                
            
     
else:
    print("u are uhh penis next module")
