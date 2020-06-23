import pyautogui
from time import sleep
import webbrowser
import os
import pickle
import platform
import datetime


def entry(text):
    pf = platform.system()

    if pf == 'Linux':
        os.system(f"echo {text} | xsel --clipboard --input")
        pyautogui.hotkey('ctrl', 'v')

    elif pf == 'Windows':
        os.system(f"echo {text} | clip")
        pyautogui.hotkey('ctrl', 'v')

    elif pf == 'Darwin':
        os.system(f"echo {text} | pbcopy")
        pyautogui.hotkey('command', 'v')


def openfile(filename):
    if os.path.exists(filename):
        f = open(filename, "rb")
        list = pickle.load(f)

    else:
        list = inp()
        list.append(input('出席番号\n例）１組1番 → 2101 :'))
        list.append(input('名前 :'))
        print('名簿を変更する際は.nameを削除してください.\nその他の場合は.nameは削除しないでください.')
        input('Enterで続行')
        f = open(filename, 'wb')
        pickle.dump(list, f)

    return list


def inp():
    list = []
    s = input('講座名を入力してください(2s12,2sx,2sy) :')
    if s == "2s12" or s == "2sx" or s == "2sy":
        list.append(s)

    else:
        inp()

    return list


def main():
    l = openfile(f'{os.path.dirname(os.path.abspath(__file__))}/.name')

    l = [datetime.datetime.now().strftime(
        '%m'), datetime.datetime.now().strftime('%d')] + l
    webbrowser.open(
        "https://docs.google.com/forms/d/e/1FAIpQLSdRGwbiFkDD9G8zRvFZcqoSMfTRbHqqys3AlTk_PbSCvjzx8Q/viewform")
    sleep(5)
    i = 0

    pyautogui.press('tab')

    for s in l:
        if i == 2:
            if s == '2s12':
                pyautogui.press('down')
                sleep(.05)
                pyautogui.press('up')
            elif s == '2sx':
                pyautogui.press('down')
            elif s == '2sy':
                pyautogui.press('down')
                sleep(.05)
                pyautogui.press('down')

            pyautogui.press('tab')
        else:
            entry(s)

            pyautogui.press('tab')
        i += 1
        sleep(.05)

    pyautogui.press('Enter')


if __name__ == '__main__':
    main()
