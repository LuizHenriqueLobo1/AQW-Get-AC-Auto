import pyautogui
import time
import os

def main():
	option = ""
	while True:
		menu()
		option = input("\n- ")
		if option == "1":
			run()
		elif option == "2":
			help()
		elif option == "3":
			quit()

def run():
	if openGame():
		join()
		getCoins()
	else:
		isClosed()

def openGame():
	status = True
	icon = pyautogui.locateOnScreen('targets/aqw_icon.PNG')
	if icon != None:
		pyautogui.click(icon)
	else:
		status = False
	return status

def join():
	pyautogui.press(['enter'])
	pyautogui.keyUp('enter')
	pyautogui.write('/join ballyhoo')
	pyautogui.press(['enter'])
	pyautogui.keyUp('enter')
	time.sleep(2)

def getCoins():
	for i in range(3):
		time.sleep(1)
		if openExclamation():
			time.sleep(1)
			if openAd():
				time.sleep(1)
				pyautogui.click('targets/aqw_get_reward.PNG')
				time.sleep(1)
				pyautogui.click('targets/aqw_confirm.PNG')
			else:
				todayOver()
				break
		else:
			exclamationNotFound()
			break

def openExclamation():
	status = True
	exclamation = pyautogui.locateOnScreen('targets/aqw_exclamation.PNG')
	if exclamation != None:
		pyautogui.click(exclamation)
	else:
		status = False
	return status

def openAd():
	status = True
	ad = pyautogui.locateOnScreen('targets/aqw_view_ad.PNG')
	if ad != None:
		pyautogui.click(ad)
	else:
		status = False
	return status

def loop(string):
	while True:
		option = input(string)

		if option != None:
			break

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def help():
	while True:
		clear()
		print("-----------------------------------")
		print("| TO RUN THIS AUTOMATION,         |")
		print("| YOU MUST BE LOGGED IN TO AQW,   |")
		print("| YOUR AQW MUST BE IN FULL SCREEN |")
		print("| AND YOU MUST BE USING FULL HD   |")
		print("-----------------------------------")
		loop("PRESS ENTER TO BACK...")
		break

def quit():
	print("\nSEE YOU LATER :)\n")
	exit()

def isClosed():
	print("\n-----------")
	print("| ERROR 1 |")
	print("-----------")
	print("(YOUR AQW IS CLOSED)")
	loop("PRESS ENTER TO TRY AGAIN...")

def todayOver():
	print("\n-----------")
	print("| ERROR 2 |")
	print("-----------")
	print("(YOU CAN'T DO MORE TODAY)")
	loop("PRESS ENTER TO TRY AGAIN...")

def exclamationNotFound():
	print("\n-----------")
	print("| ERROR 3 |")
	print("-----------")
	print("(THE EXCLAMATION WAS NOT FOUND)")
	loop("PRESS ENTER TO TRY AGAIN...")

def wolf():
	clear()
	print("                    .")
	print("                   / V\\") 
	print("                 / `  /")
	print("                <<   |")
	print("                /    |")
	print("              /      |")
	print("            /        |")
	print("          /    \  \ /")
	print("         (      ) | |")
	print("  _______|   _/_  | |")
	print("<_________\______)\__)")

def menu():
	wolf()
	print("------------------------")
	print("|  GET AC AUTO IN AQW  |")
	print("------------------------")
	print("(1). RUN")
	print("(2). HELP")
	print("(3). QUIT")


main()
