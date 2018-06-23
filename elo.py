import random
from random import shuffle
import operator
import os

def expected_score(rating_A, rating_B):
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

philosophers = {
	"Hume" : 1600,
	"Kant" : 1600,
	"Nietzsche" : 1600,
	"Hobbes" : 1600,
	"Rousseau" : 1600,
	"Adam Smith" : 1600,
	"Cicero" : 1600,
	"Deleuze" : 1600,
	"John Stuart Mill" : 1600,
	"Karl Popper" : 1600,
	"Bertrand Russell" : 1600,
	"Schopenhauer" : 1600,
	"Marx" : 1600,
	"Descartes" : 1600,
	"Wittgenstein" : 1600,
	"Kierkegaard" : 1600,
	"Confucius" : 1600,
	"Spinoza" : 1600,
	"John Rawls" : 1600,
	"Sartre" : 1600,
	"Heidegger" : 1600,
	"Frege" : 1600,
	"Derrida" : 1600,
	"Foucault" : 1600,
	"Simone de Beauvoir" : 1600,
	"Machiavelli" : 1600,
	"Bacon" : 1600,
	"Bentham" : 1600,
	"Buddha" : 1600,
	"Noam Chomsky" : 1600,
	"Voltaire" : 1600,
	"Leibniz" : 1600,
	"Hegel" : 1600
}

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
		philosophers[phil_1] = new_score(philosophers[phil_1], 1, expected_score(philosophers[phil_1], philosophers[phil_2]))
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