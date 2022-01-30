from random import randint


print("PIMAD + WOMBLE - ROCK PAPER SCISSORS - PYTHON")

print ("What do you choose????")
choose = input().lower()
chosencpuID = randint(1, 3)
chosencpuNAME = None
if chosencpuID == 1:
	chosencpuNAME = "rock"
if chosencpuID == 2:
	chosencpuNAME = "paper"
if chosencpuID == 3:
	chosencpuNAME = "scissors"
# ROCK PAPER **
# PAPER SCISSORS **
# SCISSORS ROCK
# SAME ** 
print("Computer chooses " + chosencpuNAME)
if choose == "rock" and chosencpuNAME == "paper": 
	print("CPU wins")
elif choose == "paper" and chosencpuNAME == "rock":
	print("YOU WIN")
elif choose == "scissors" and chosencpuNAME == "paper":
	print("YOU WIN")
elif choose == chosencpuNAME:
	print("DRAW")
elif choose == "paper" and chosencpuNAME == "scissors":
	print("YOU LOOSE")
elif choose == "scissors" and chosencpuNAME == "rock":
	print("CPU WINS")
elif choose == "rock" and chosencpuNAME == "scissors":
	print("You WINNERED")
else:
  print("ERROR UNCAUGHT EXEPTION: UNDEFIENED \"" + choose + "\"")

