print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
	print('Correct!')
	score += 1
else:
	print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer == "read only memory":
	print('Correct!')
	score += 1
else:
	print("Incorrect!")

answer = input("What does RAM stand for?")
if answer == "read access memory":
	print('Correct!')
	score += 1
else:
	print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " questions correct!")
quit()