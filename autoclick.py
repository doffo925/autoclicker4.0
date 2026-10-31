import random
import time
import keyboard
import pyautogui
point=0
count_restart=0
MouseCor=[]
delay_on=False
delay_onfix=False
help=True
fix_delay=1
fir_dlay=0.1
sec_dlay=0.2
pyautogui.FAILSAFE = True
run=False
n=0
setMouse_on=False
click_move=False

def toggle():
    global run
    global help
    global setMouse_on
    global click_move
    if setMouse_on == True:
        setMouse_on=False
        help=True

    if run==True:
        run=False
        help=True
    if click_move==True:
        click_move=False
        help=True
def setMouse_cor():
    x, y = pyautogui.position()
    print("Координаты:", x, y)
    MouseCor.append(pyautogui.position())
    print(MouseCor)
    


# Обработчик работает независимо от цикла и sleep
keyboard.add_hotkey("0", toggle)
keyboard.add_hotkey("m", setMouse_cor)

while True:
    if run == True:
        pyautogui.click()
        n=n+1
        print("кол во кликов ",n)
        if delay_on:
            delay=random.uniform(fir_dlay,sec_dlay) 
            time.sleep(delay)
        elif delay_onfix:
            fix_delay=float(fix_delay)
            time.sleep(fix_delay)
        
    if setMouse_on == True:
        pass
    if click_move == True:
        pyautogui.moveTo(MouseCor[point].x, MouseCor[point].y, duration=fix_delay)   
        pyautogui.click()
        print("включен режим клики с перемещением")  
        point=point+1
        long=len(MouseCor)
        if point >= long:
            if count_restart > 0: 
                point=0
                count_restart-=1  

            elif count_movement =="0":
                point=0
            else:
                click_move=False
                help=True
            
    
    
    
    
    
    
    if help:
        help=False
        print("Здраствуйте вы находитесь в программе автокликер ")
        print("0 - запуск и окончание программы ")
        print("d - настройки задержки")
        print("z - режим записи мыши ")
        print("p - режим кликов с перемещением")
        print("d,2,2-изменение скорости перемещения")
        print("ex - выход из программы")
        param_0=input(":")
        if param_0 == "0":
            run = True
            help=False
        elif param_0 == "d":
            
            param_0 = input("1 - чтобы включить задержку с параметрами по умолчанию,\n2 - чтобы настроить\n:")
            if param_0 =="1":
                delay_on = True
                delay_onfix=False
            elif param_0 =="2":
                param_0=input("1 - рандомная задержка,\n2 - фиксированная задержка \n:")
                print(param_0)
                if param_0 == "1":
                    delay_on=True
                    delay_onfix=False
                    fir_dlay=input("минимальная задержка:")
                    sec_dlay=input("максимальная задержка:")
                    fir_dlay=float(fir_dlay)
                    sec_dlay=float(sec_dlay)
                elif param_0 == "2":
                    fix_delay=input("введите задержку:")
                    if fix_delay =="0":
                        delay_onfix=False
                        delay_on=False
                    else:
                        delay_onfix=True
                        delay_on=False
                else:
                    print("вы ввели неправильную команду")
                    help=True
            else:
                print("вы ввели неправильную команду")
                help=True
            run=True
        elif param_0 == "ex":
            break 
        elif param_0 == "z":
            setMouse_on=True
            print("нажмите m - чтобы сделать запись текущих координат")
            print("нажмите 0 - для остановки")
        elif param_0=="p":
            count_movement=input("введите кол-во повторений перемещений\n"\
                "0-бесконечность :")  
            click_move=True
            count_restart=int(count_movement)-1
        else:
            print("вы ввели неправильную команду")
            help=True
        