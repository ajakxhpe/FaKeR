#!/usr/bin/env python3


import sys
import os 
import time


from asciimatics.effects import  Mirage, Cycle, Matrix, Stars, Print 
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from pyfiglet import Figlet
from asciimatics.exceptions import ResizeScreenError
from rich.panel import Panel
from rich import print,style




colorall = ["BLACK" , "RED", "BLUE" , "WHITE" ,"GREEN" , "YELLOW" , "CYAN"]





def baners(screen):
            

            scenes = []

            effects = [
                
                Mirage(
                    screen,
                    FigletText("faker", font='big'),
                    screen.height // 2 - 3,
                    Screen.COLOUR_GREEN,
                    start_frame=0,
                    # stop_frame=100
                ),

                Cycle(
                    screen,
                    FigletText("faker", font='big',),
                    screen.height // 2 - 3,
                    start_frame=100
                ),
                
                Stars(
                    screen,
                    120,
                    start_frame=100,

                    pattern="..+..  ...x...  ...*... " + " "*100,
                ),

                
                Print(
                    screen,
                    SpeechBubble('Press key "x" to continue',),
                    screen.height // 1-3 ,
                    attr=Screen.A_BOLD,
                    start_frame=150,
                    
                    clear=True                    
                )
                
        
            ]
            scenes.append(Scene(effects, -1))
            
            
            screen.play(scenes, stop_on_resize=True)

def theme():
        



    for color in colorall:
        ban = print(Panel("""      
        
'########::::'###::::'##:::'##:'########:'########::
 ##.....::::'## ##::: ##::'##:: ##.....:: ##.... ##:
 ##::::::::'##:. ##:: ##:'##::: ##::::::: ##:::: ##:
 ######:::'##:::. ##: #####:::: ######::: ########::
 ##...:::: #########: ##. ##::: ##...:::: ##.. ##:::
 ##::::::: ##.... ##: ##:. ##:: ##::::::: ##::. ##::
 ##::::::: ##:::: ##: ##::. ##: ########: ##:::. ##:
..::::::::..:::::..::..::::..::........::..:::::..::
        
        """,style=color))
        time.sleep(0.2)
        os.system("clear")


