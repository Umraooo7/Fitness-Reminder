import os, sys
import pygame
from pygame.locals import*
import time
it = time.time()
pygame.mixer.init()

def getdate():
    import datetime
    return datetime.datetime.now()

def mint():
    fi = int(time.asctime(time.localtime(time.time()))[14:16])
    return fi
mint()

def hr():
    ti = int(time.asctime(time.localtime(time.time()))[11:13])
    return ti
print(hr())
# print(mint())
def log_eye():
    """To set 45 minute timer for"""
    return((hr() == 9 and mint() == 45)
       or (hr() == 10 and mint() == 30)
       or (hr() == 11 and mint() == 15)
       or (hr() == 12 and mint() == 0)
       or (hr() == 12 and mint() == 45)
       or (hr() == 1 and mint() == 30)
       or (hr() == 2 and mint() == 15)
       or (hr() == 3 and mint() == 0)
       or (hr() == 3 and mint() == 45)
       or (hr() == 4 and mint() == 30)
       or (hr() == 5 and mint() == 15)
#        or (hr() == 23 and mint() == 30) #for testing
      )

# log_eye()

c=0
# while((hr() >= 16) and (hr() <= 24)):
while((hr() == 0)):
    log_eye()
    print("hour: ",hr()," minute: ", mint())
    l = 3500
#     print(l-c)

    if ((mint() == 30)
        or (mint() == 15)
        or (mint() == 5)
        or (mint() == 45)):
        """for drinking water"""

        pygame.mixer.music.load('water.mp3')
        pygame.mixer.music.play(-1)

        print("________Time to drink Water_____")
        usr = (input("Type drank:")).lower()

        if usr == "drank":
            a = input("How much you drank in ml: ")
            c = c + int(a)
            if int(a) > 0:
                print(l-c)
                with open ("LogFile.txt",'a+') as f:
                    f.write(str(getdate()) + ': Water drank: ' + a +' ml and '
                            + str(l - int(c))  + " ml water left\n")
                with open ("LogFile.txt") as f:
                    print(f.readlines())
                pygame.mixer.music.stop()
                break

        else:
            print("just type drank")

    if ((mint() == 30)
          or (mint() == 0)):
        """For pyhsical workout"""

        pygame.mixer.music.load('pyhsical.mp3')
        pygame.mixer.music.play(-1)

        print("________Time to do Physical Workout_____")
        usr = (input("Type done:")).lower()

        if usr == "done":
            a = input("Press 1: After Completing Workout-")
            with open ("LogFile.txt",'a+') as f:
                f.write(str(getdate()) + ': Workout done\n')
            with open ("LogFile.txt") as f:
                print(f.readlines())
            if (int(a) > 0):
                pygame.mixer.music.stop()
                break
        else:
            print("just type done")

    if (log_eye()):
        """For eye workout"""

        pygame.mixer.music.load('eyes.mp3')
        pygame.mixer.music.play(-1)

        print("________Time to do Eye excercise_____")
        usr = (input("Type done:")).lower()

        if usr == "done":
            a = input("Press 1: For Completing Workout")
            with open ("LogFile.txt",'a+') as f:
                f.write(str(getdate()) + ': Eye excercise done\n')
            with open ("LogFile.txt") as f:
                print(f.readlines())
            if (int(a) > 0):
                pygame.mixer.music.stop()
                break
        else:
            print("just type done")

    else:
        print("Breakkk...")
        break
#To remove all the break function, loop will run endlessly
#Challenge is to do with recurssive loop.
