#==========================================================
from banner import  baner
from method import method
import os
#=========================main===============================






if __name__ == "__main__":
    while True:
        try:
            baner.Screen.wrapper(baner.baners)
            baner.theme()
            methods = method.fake()
            break
        except baner.ResizeScreenError:
            pass
