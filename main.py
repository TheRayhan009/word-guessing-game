import random
import os
from random_word import RandomWords
from pathlib import Path
patth=os.path.dirname(os.path.abspath(__file__))
patth=patth+"/therayhanpywordgussinggame2.0.txt"
patth = patth.replace("\\", "/")
patth=patth[0].upper() + patth[1:]
if os.path.exists(patth) == False:
    f = open(patth,"a")

class color:
    BOLD = '\033[4m'
    END = '\033[0m'
    
class color2:
    BOLD2 = '\033[7m'
    END2 = '\033[0m'
class color3:
    BOLD3 = '\033[1m'
    END3 = '\033[0m'
    
point=0
first_txt=0
def start():
    # this is the welcome text.You will see this text first when you start playing this game.

    start1=f'''
    
____________________________________________________________________________________________________________
|                                              WELCOME!!                                                    |
|                                      This is a word gussing game.                                         |
|                                                                                                           |
|                                      You have random chance to guss.                                      |
|                                                                                                           |
|                                         username is : "{os.getlogin().lower()}"                                           |
|                                                                                                           |
|                                                 --info--                                                  |
|                                        The game made by TheRayhan PY .                                    |
|                                    Bilding programming lenguage is python.                                |
|                                                 ENJOY!!                                                   |
|_____________________________________________Have A Good Day_______________________________________________|
'''
    big_and_bold_text = color.BOLD + start1.upper() + color.END
    print(big_and_bold_text)
    
x=0 
bulchak=False
score=0
prvst=""
start()
def rendomst():
    global c
    global f
    global na
    global x
    global prvst
    global renword
    global undesr_word
    global vv
    na=random.randint(a=2,b=20)
    r = RandomWords()
    renword=r.get_random_word()
    f=renword
    undesr_word=renword
    vv=random.randint(a=1,b=5)
    if vv==1:
        for k in range(len(f)-1):
            if k%2==0:
                undesr_word=undesr_word.replace(undesr_word[k],"_")
    elif vv==2:
        for k in range(len(f)-1):
            if k%3==0 or k%5==0:
                undesr_word=undesr_word.replace(undesr_word[k],"_")
    elif vv==3:
        for k in range(len(f)-1):
            if k%1==0 and k%3!=0:
                undesr_word=undesr_word.replace(undesr_word[k],"_")
    elif vv==4:
        for k in range(len(f)-1):
            if k%5!=0:
                undesr_word=undesr_word.replace(undesr_word[k],"_")
    elif vv==4:
        for k in range(len(f)-1):
            if k%2!=0 or k%3!=0:
                undesr_word=undesr_word.replace(undesr_word[k],"_")
    c = color2.BOLD2 + undesr_word + color2.END2
    chanch = color3.BOLD3 + str(na) + color3.END3
    x=0
    print("\t \t \t \t \t  Your Word Is :",c)
    print("\t \t \t \t \t  Your Gussing Chanch Is :",chanch)

rendomst()

def chak(s):
    global bulchak
    if s==f:
        bulchak=True
    
    
    
    
def play_chak():
    global score
    play=f'''
    
____________________________________________________________________________________________________________
|                                           You Got it !! yooo!                                             |
|                                          You want to play again?                                          |
|                                              To yes press (y)                                             |           
|                                              To no press (n)                                              |
|                                              Your Score is : {score}                                            |
|                                            username is : "{os.getlogin().lower()}"                                        | 
'''
    big_and_bold_text = color.BOLD + play.upper() + color.END
    print(big_and_bold_text)
coc=False
while x<na:
    st=input(f"Guss Number {x+1} : ")
    print("\n")
    chak(st)
    x+=1
    if bulchak==True:
        score+=1
        play_chak()
        pchak=input()
        if pchak=="y" or pchak.lower()=="y":
            bulchak=False
            coc=False
            x=0
            rendomst()
            
        else:
            coc=True
            print("Good Bye Play With Me Litter..!")
            break
    if x==na:
        coc=False
        break
if coc==False:
    print("OPPS!! Try Next Time !..")
    print(f"The Word Was : \" {f} \"")
with open(patth,"r") as sc:
    data1 = sc.read()
    xscore=f"High Score is : {int(score)}"
    if len(data1)==0:
        with open(patth,"w") as sc:
            sc.write(f"High Score is : {int(score)}")
    elif int(xscore[16:])>int(data1[16:]):
        with open(patth,"w") as sc:
            sc.write(f"")
            sc.write(f"High Score is : {int(score)}")
with open(patth,"r") as sc:
    data2 = sc.read()
    print(data2)