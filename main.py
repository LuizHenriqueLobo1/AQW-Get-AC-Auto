import pyautogui
import time
import os

paths = {
	"icon":        "targets/aqw_icon.PNG",
	"exclamation": "targets/aqw_exclamation.PNG",
	"viewAd":      "targets/aqw_view_ad.PNG",
	"getReward":   "targets/aqw_get_reward.PNG",
	"confirm":     "targets/aqw_confirm.PNG"
}

errors = [
	"(YOUR AQW IS CLOSED)",
	"(THE EXCLAMATION WAS NOT FOUND)",
	"(YOU CAN'T DO MORE TODAY)"
]

def main():
	option = ""
	while True:
		clear()
		print(menu)
		option = input("\n- ")
		if option == "1":
			run()
		elif option == "2":
			help()
		elif option == "3":
			quit()

def run():
	if clickTarget(paths["icon"]):
		join()
		getCoins()
	else:
		error(errors[0])

def join():
	pyautogui.press(['enter'])
	pyautogui.write('/join ballyhoo')
	pyautogui.press(['enter'])
	time.sleep(2)

def getCoins():
	for i in range(3):
		time.sleep(1)
		if clickTarget(paths["exclamation"]):
			time.sleep(1)
			if clickTarget(paths["viewAd"]):
				time.sleep(1)
				pyautogui.click(paths["getReward"])
				time.sleep(1)
				pyautogui.click(paths["confirm"])
			else:
				error(errors[2])
				break
		else:
			error(errors[1])
			break

def clickTarget(path):
	status = True
	target = pyautogui.locateOnScreen(path)
	if target != None:
		pyautogui.click(target)
	else:
		status = False
	return status

def loop(string):
	while True:
		option = input(string)
		if option != None:
			break

def help():
	while True:
		clear()
		print(helpBoard)
		loop("PRESS ENTER TO BACK...")
		break

def quit():
	print("\nSEE YOU LATER :)\n")
	exit()

def error(message):
	print(errorBoard + message)
	loop("PRESS ENTER TO TRY AGAIN...")

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

menu = """
                    .
                   / V\\
                 / `  /
                <<   |
                /    |
              /      |
            /        |
          /    \  \ /
         (      ) | |		  
  _______|   _/_  | |
<_________\______)\__)
------------------------
|  GET AC AUTO IN AQW  |
------------------------
(1). RUN
(2). HELP
(3). QUIT
"""

helpBoard = """
-----------------------------------
| TO RUN THIS AUTOMATION,         |
| YOU MUST BE LOGGED IN TO AQW,   |
| YOUR AQW MUST BE IN FULL SCREEN |
| AND YOU MUST BE USING FULL HD   |
-----------------------------------
"""

errorBoard = """
---------
| ERROR |
---------
"""

main()