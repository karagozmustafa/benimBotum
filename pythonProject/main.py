import keyboard
import pyautogui
import time
import cv2
import numpy as np
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

bosumuz = os.path.join(project_dir, 'boss.png')
cube = os.path.join(project_dir, 'cube.png')
book = os.path.join(project_dir, 'book.png')
kylis = os.path.join(project_dir, 'kylis.png')
a5mapi=os.path.join(project_dir, 'map.png')
kopekPeti=os.path.join(project_dir, 'kopekPeti.png')
kardanAdamPeti=os.path.join(project_dir, 'kardanAdamPeti.png')
envanter = os.path.join(project_dir, 'envanter.png')
siradisi=os.path.join(project_dir, 'siradisi.png')
efso=os.path.join(project_dir, 'efso.png')
buyulu=os.path.join(project_dir, 'buyulu.png')
essiz=os.path.join(project_dir,'essiz.png')
essiz2=os.path.join(project_dir,'essiz2.png')
giris=os.path.join(project_dir,'giris.png')
buyuluItem=os.path.join(project_dir,'buyuluItem.png')
efsoItem=os.path.join(project_dir,'efsoItem.png')
sdItem=os.path.join(project_dir,'sdItem.png')
a5yuzuk=os.path.join(project_dir,'a5yuzuk.png')
kalkan=os.path.join(project_dir,'kalkan.png')


threshold = 0.60

def solTik(x):
    resim = cv2.imread(x)
    ekran_goruntusu_pil = pyautogui.screenshot()
    ekran_goruntusu_np = np.array(ekran_goruntusu_pil)
    ekran_goruntusu_bgr = cv2.cvtColor(ekran_goruntusu_np, cv2.COLOR_RGB2BGR)
    sonuc = cv2.matchTemplate(ekran_goruntusu_bgr, resim, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(sonuc)
    if max_val >= threshold:
        x = max_loc[0]
        y = max_loc[1]
        pyautogui.leftClick(x + 25, y + 8)
        return True
    else:
        return False
tmp=0
def sagTik(x):
    resim = cv2.imread(x)
    ekran_goruntusu_pil = pyautogui.screenshot()
    ekran_goruntusu_np = np.array(ekran_goruntusu_pil)
    ekran_goruntusu_bgr = cv2.cvtColor(ekran_goruntusu_np, cv2.COLOR_RGB2BGR)
    sonuc = cv2.matchTemplate(ekran_goruntusu_bgr, resim, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(sonuc)
    if max_val >= threshold:
        x = max_loc[0]
        y = max_loc[1]
        global tmp
        if((x+y)==tmp):
            y+=20
        else :
            tmp=x+y
        pyautogui.rightClick(x + 20, y + 10)
        return True
    else:
        return False
def satisKontrol():
    while True:
        if (buldum(envanter)):
            satis()
        else:
            break
def buldum(x):
    resim = cv2.imread(x)
    ekran_goruntusu_pil = pyautogui.screenshot()
    ekran_goruntusu_np = np.array(ekran_goruntusu_pil)
    ekran_goruntusu_bgr = cv2.cvtColor(ekran_goruntusu_np, cv2.COLOR_RGB2BGR)
    sonuc = cv2.matchTemplate(ekran_goruntusu_bgr, resim, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(sonuc)
    if max_val >= threshold:
        return True
    else:
        return False
def sat(x):
    while(True):
        if(sagTik(x)==False):
            break
        else:
            time.sleep(0.2)
def topla(x):
    while True:
        if (solTik(x)):
            satisKontrol()
        else:
            break
def satis():
    pyautogui.press("w")
    time.sleep(0.3)
    sagTik(kopekPeti)
    time.sleep(0.3)
    pyautogui.press("r")
    time.sleep(0.3)
    pyautogui.press("s")
    time.sleep(0.3)
    pyautogui.leftClick(486, 125)
    time.sleep(0.3)
    pyautogui.leftClick(725, 608)
    time.sleep(0.3)
    pyautogui.leftClick(991, 407)
    time.sleep(0.3)

    sat(buyulu)
    sat(efso)
    sat(siradisi)
    sat(essiz)
    sat(essiz2)

    pyautogui.leftClick(1024, 407)
    time.sleep(0.2)


    sat(buyulu)
    sat(efso)
    sat(siradisi)
    sat(essiz)
    sat(essiz2)

    pyautogui.leftClick(1090, 407)
    time.sleep(0.2)

    sat(buyulu)
    sat(efso)
    sat(siradisi)
    sat(essiz)
    sat(essiz2)

    pyautogui.leftClick(950, 407)
    time.sleep(0.3)
    pyautogui.keyUp("ctrl")
    time.sleep(0.3)
    pyautogui.press("esc")
    time.sleep(0.3)
    pyautogui.press("w")
    time.sleep(0.3)
    sagTik(kardanAdamPeti)
    time.sleep(0.3)
    pyautogui.press("w")
    time.sleep(0.3)
    pyautogui.keyDown("ctrl")
    time.sleep(0.3)

time.sleep(5)
while True:
    pyautogui.press('r')
    time.sleep(0.2)
    sagTik(giris)
    #time.sleep(0.2)
    pyautogui.leftClick(969, 580)
    time.sleep(5)
    while True:
        if(buldum(a5mapi)):
            break
        else:
            time.sleep(0.2)
    pyautogui.leftClick(1246, 1)
    time.sleep(1.6)
    pyautogui.leftClick(800, 230)
    time.sleep(0.6)
    pyautogui.leftClick(765, 284)
    time.sleep(0.3)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    time.sleep(0.3)
    pyautogui.mouseDown(button="right")
    while True:
        if (buldum(kalkan)):
            break
        else:
            time.sleep(0.2)
    pyautogui.press("2")
    pyautogui.press("2")
    pyautogui.press("2")
    time.sleep(0.3)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    while(buldum(bosumuz)):
        time.sleep(0.2)

    pyautogui.mouseUp(button="right")
    pyautogui.keyDown('ctrl')
    time.sleep(1)

    topla(a5yuzuk)
    topla(efsoItem)
    topla(sdItem)
    topla(buyuluItem)
    topla(cube)
    topla(kylis)
    topla(book)

    pyautogui.keyUp("ctrl")

    if (keyboard.is_pressed("1")):
        break

