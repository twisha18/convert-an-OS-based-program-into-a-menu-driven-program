import os
print("Welcome user")
print("What would you like to do?", end='')
while True:
	p = input()

	# print(p)
	# os.system(p)

	if ("run" in p)  and ("chrome" in p) or ("browser" in p):
	  os.system("start chrome")

	elif (("run" in p) or  ("execute" in p ) or ("launch")) and  (("notepad" in p) or ("editor" in p) ):
	  os.system("notepad")

	elif ("run" in p)  and ("player" in p) or ("media" in p):
	  os.system("start wmplayer")  

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("PLease try again.")