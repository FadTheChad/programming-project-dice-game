import random

i=0
User1Score = 0
User2Score = 0
User1Draws = 0
User2Draws = 0
WinnersScore = 0
Username1Access=False
Username2Access=False

Username1confirm = input("P1: What is your chosen name?   ")
Password1confirm = input("P1:What is your chosen password?    ")

while Username1Access == False:
	Username1 = input("P1: Enter your name: ")
	Password1 = input("P1:Enter your password: ")
	if Username1 == Username1confirm:
		if Password1 == Password1confirm:
			print("Hello,",Username1,"You are now allowed into the game.")
			Username1Access = True
			User1 = Username1
		else:
			print("Wrong password,try again!")
	else:
		print("Wrong username,try again!")

Username2confirm = input("P2: What is your chosen name?   ")
Password2confirm = input("P2:What is your chosen password?    ")

while Username2Access == False:
	Username2 = input("P2: Enter your name: ")
	Password2 = input("P2:Enter your password: ")
	if Username2 == Username2confirm:
		if Password2 == Password2confirm:
			print("Hello,",Username2,"You are now allowed into the game.")
			Username2Access = True
			User2 = Username2
		else:
			print("Wrong passowrd,try again!")
	else:
		print("Wrong username,try again!")

def roll(User):
	score=0
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	dicetotalscore = dice1+dice2
	score = score+dicetotalscore

    scoredOrLost = " scored "

	additional = ""
	
	if dicetotalscore %2 == 0:
		score = score+10
	else:
		score = score-5
        if (score < 0) score = 0
        scoredOrlost = " lost "
	if dice1 == dice2:
		dice3 = random.randint(1,6)
		score = score+dice3
	
	print(User + scoredOrLost + str(dice1) + " + " str(dice2) + " points with a score of now: " + str(score))
    print ("\n==========\n")    

	return(score)

for i in range(1,6):
	decision = input ("Roll dice? y/n?   ").lower()
	print ("\n")
	if decision == "y":
		print (f"ROUND {i}")
		print ("\n==========\n")
		User1Score += roll(User1)		
		User2Score += roll(User2)
	else: 
		print ("Program Terminated")
		quit()

if User1Score == User2Score:
	while User1Draws == User2Draws:
		User1Draws = random.randint(1,6)
		User2Draws = random.randint(1,6)
	if User1Draws > User2Draws:
		User1Score=0
	elif User2Draws > User1Draws:
		User2Score=0
if User1Score>User2Score:
  LeaderScore = User1Score
  LeaderUsername = Username1
  Leader = (LeaderScore, Username1)
elif User2Score>User1Score:
  LeaderScore = User2Score
  Leader = (LeaderScore, Username2)
  LeaderUsername = Username2
print('Well done, ', LeaderUsername,' you won with ',LeaderScore,' Points')

Leader = (str(LeaderScore),',',LeaderUsername)
f = open('Leaderboard.csv', 'a')
f.write(''.join(Leader))
f.write('\n')
f.close()
f = open('Leaderboard.csv', 'r')
leaderboard = [line.replace('\n','') for line in f.readlines()]
f.close()



