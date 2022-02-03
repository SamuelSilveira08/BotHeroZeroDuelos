import pyautogui
import time
from itertools import repeat


def click_btn(img, timeout=6):
    start = time.time()
    while True:
        pos = pyautogui.locateCenterOnScreen(img, confidence=0.7)
        if pos is not None:
            pyautogui.moveTo(pos, duration=0.6)
            pyautogui.click()
            time.sleep(2)
            break
        else:
            if time.time() - start < timeout:
                continue
            else:
                x = -1
                y = -1
                return pos


def attack(players):
    count = 1
    aux = []
    for i in players:
        aux.extend(repeat(i, 3))
    for player in aux:
        print('running {0}'.format(player))
        click_btn('img/ranking.png')
        click_btn('img/search-bar.png')
        pyautogui.moveRel(50, 0)
        pyautogui.keyDown('backspace')
        time.sleep(2)
        pyautogui.keyUp('backspace')
        pyautogui.write(player)
        pyautogui.moveRel(0, 50)
        click_btn('img/search-btn.png')
        click_btn('img/show-hero-btn.png')
        click_btn('img/attack-btn.png')
        click_btn('img/ok-btn.png')
        click_btn('img/discount.png')
        pyautogui.click()
        count += 1
        if count == 3:
            count = 0
        time.sleep(465)


def load_players(file):
    with open(file) as file:
        players = file.readlines()
    return players


players = load_players('players.txt')
players = map(lambda player: player.rstrip('\n'), players)
attack(players)
