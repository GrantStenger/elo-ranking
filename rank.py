import random
from random import shuffle
import operator
import os

# def expected_score(rating_A, rating_B):
# 	return 1 / (1 + 10**((rating_B-rating_A)/400))

def expected_score(phil_1, phil_2):
	return 1 / (1 + 10**((rating_B-rating_A)/400))

def new_score(prev_score, tournament_score, expected_score):
	return prev_score + 32 * (tournament_score - expected_score)

def print_rankings(philosophers):
	print("Current Rankings: ")

	sorted_dict = sorted(philosophers.items(), key=operator.itemgetter(1))
	sorted_dict.reverse()
	for phil in sorted_dict:
		print(phil[0] + ": " + str(phil[1]))
	print()
	print()

def insertionSort(philosophers):
	for i in range(1,len(philosophers)):
		wins = philosophers[list(philosophers)[i]][0]
		losses = philosophers[list(philosophers)[i]][1]
		if wins + losses > 0:
			curr_value = wins / (wins + losses)
		else:
			curr_value = 0.5

		print("current value:", curr_value)

		# if i > 0:
		# 	if philosophers[list(philosophers)[i-1]][0] + philosophers[list(philosophers)[i-1]][1] > 0:
		# 		prev_value = philosophers[list(philosophers)[0]][0]/(philosophers[list(philosophers)[0]][0]+philosophers[list(philosophers)[0]][1])
		# 	else:
		# 		prev_value = 0.5
		
		position = i
		possition_w_l = 0.5
		# possition_w_l = philosophers[list(philosophers)[position-1]][0]/(philosophers[list(philosophers)[position-1]][0]+philosophers[list(philosophers)[position-1]][1])
		while position > 0 and possition_w_l > curr_value:
			philosophers[list(philosophers)[position]] = philosophers[list(philosophers)[position-1]]
			position -= 1
			curr_value = philosophers[list(philosophers)[position]][0]/(philosophers[list(philosophers)[position]][0]+philosophers[list(philosophers)[position]][1])
			possition_w_l = philosophers[list(philosophers)[position-1]][0]/(philosophers[list(philosophers)[position-1]][0]+philosophers[list(philosophers)[position-1]][1])

# "Name": (wins, losses)
philosophers = {
	"Hume" : (0, 0),
	"Kant" : (0, 0),
	"Nietzsche" : (0, 0),
	"Hobbes" : (0, 0),
	"Rousseau" : (0, 0),
	"Adam Smith" : (0, 0),
	"Cicero" : (0, 0),
	"Deleuze" : (0, 0),
	"John Stuart Mill" : (0, 0),
	"Karl Popper" : (0, 0),
	"Bertrand Russell" : (0, 0),
	"Schopenhauer" : (0, 0),
	"Marx" : (0, 0),
	"Descartes" : (0, 0),
	"Wittgenstein" : (0, 0),
	"Kierkegaard" : (0, 0),
	"Confucius" : (0, 0),
	"Spinoza" : (0, 0),
	"John Rawls" : (0, 0),
	"Sartre" : (0, 0),
	"Heidegger" : (0, 0),
	"Frege" : (0, 0),
	"Derrida" : (0, 0),
	"Foucault" : (0, 0),
	"Simone de Beauvoir" : (0, 0),
	"Machiavelli" : (0, 0),
	"Bacon" : (0, 0),
	"Bentham" : (0, 0),
	"Buddha" : (0, 0),
	"Noam Chomsky" : (0, 0),
	"Voltaire" : (0, 0),
	"Leibniz" : (0, 0),
	"Hegel" : (0, 0)
}

insertionSort(philosophers)
print(philosophers)

print(list(philosophers)[0])

pairings = []
count = 0
for i in range(len(philosophers)):
	for j in range(i+1, len(philosophers)):
		if count % 2 == 0:
			count += 1
			pairings.append((list(philosophers)[i], list(philosophers)[j]))
		else:
			count += 1
			pairings.append((list(philosophers)[j], list(philosophers)[i]))
length = int((len(philosophers)*(len(philosophers)-1))/2)
order = random.sample(range(0, length), length)

shuffled_pairings = []
for i in range(length):
	shuffled_pairings.append(pairings[order[i]])

quit = False
count = 0

while quit == False and count < length:
	os.system('clear')
	print_rankings(philosophers)
	phil_1 = shuffled_pairings[count][0]
	phil_2 = shuffled_pairings[count][1]
	print(phil_1, "vs.", phil_2)
	print()
	# print(phil_1, "score:", philosophers[phil_1])
	# print(phil_2, "score:", philosophers[phil_2])
	# print()
	# print(phil_1, "expected score:", expected_score(philosophers[phil_1], philosophers[phil_2]))
	# print(phil_2, "expected score:", expected_score(philosophers[phil_2], philosophers[phil_1]))
	# print()
	winner = input("Who wins: " + phil_1 + " or " + phil_2 + "? ")
	print()
	os.system('clear')
	print("The winner is", winner)
	# print()
	if winner == phil_1:
		philosophers[phil_1] = new_score(philosophers[phil_1], 1, expected_score(phil_1, phil_2))
		philosophers[phil_2] = new_score(philosophers[phil_2], 0, expected_score(philosophers[phil_2], philosophers[phil_1]))
		# print("New", phil_1, "score", philosophers[phil_1])
		# print("New", phil_2, "score", philosophers[phil_2])
	elif winner == phil_2:
		philosophers[phil_1] = new_score(philosophers[phil_1], 0, expected_score(philosophers[phil_1], philosophers[phil_2]))
		philosophers[phil_2] = new_score(philosophers[phil_2], 1, expected_score(philosophers[phil_2], philosophers[phil_1]))
		# print("New", phil_1, "score", philosophers[phil_1])
		# print("New", phil_2, "score", philosophers[phil_2])
	else:
		print("that's not an option u cunt")
	print()

	count += 1

	user_input = input("Quit? ")
	if user_input == "yes" or user_input == "y":
		quit = True
		exit()

print("The Final Ranking Is...")
print()
print_rankings(philosophers)

# Notes:
# How to proceed. I need a much more efficient algorithm.
# The number of games to play currently increases O(x^2)
# 1600 is arbitrary. Figure out the math.
# I feel like this algorithm way overweighs recent comparissons as compared to more distant comparissons