import random
from random import shuffle
import operator
import os

# def expected_score(rating_A, rating_B):
# 	return 1 / (1 + 10**((rating_B-rating_A)/400))
def get_win_loss(phil):
	philosophers[phil][0] / (philosophers[phil][0] + philosophers[phil][1])

def expected_score(phil_1, phil_2):
	if philosophers[phil_1][0] + philosophers[phil_1][1] > 0:
		w_l_score_1 = get_win_loss(phil_1)
	else:
		w_l_score_1 = 0.5

	if philosophers[phil_2][0] + philosophers[phil_2][1]:
		w_l_score_2 = get_win_loss(phil_2)
	else:
		w_l_score_2 = 0.5

	return 1 / (1 + 10**((w_l_score_1-w_l_score_2)/400))

def new_score(prev_score, tournament_score, expected_score):
	return prev_score + 32 * (tournament_score - expected_score)

def sort_and_print(philosophers):
	sorted_list = sorted(philosophers, key=lambda phil: philosophers[phil][2])
	print("Rankings: ")
	for i in range(len(sorted_list)):
		phil = sorted_list[len(sorted_list) - i - 1]
		print(phil + ": " + str(philosophers[phil][0]) + " wins, " + str(philosophers[phil][1]) + " losses")
	print()
	print()
	return True

# "Name": (wins, losses)
philosophers = {
	"Hume" : (0, 0, 0),
	"Kant" : (0, 0, 0),
	"Nietzsche" : (0, 0, 0),
	"Hobbes" : (0, 0, 0),
	"Rousseau" : (0, 0, 0),
	"Adam Smith" : (0, 0, 0),
	"Cicero" : (0, 0, 0),
	"Deleuze" : (0, 0, 0),
	"John Stuart Mill" : (0, 0, 0),
	"Karl Popper" : (0, 0, 0),
	"Bertrand Russell" : (0, 0, 0),
	"Schopenhauer" : (0, 0, 0),
	"Marx" : (0, 0, 0),
	"Descartes" : (0, 0, 0),
	"Wittgenstein" : (0, 0, 0),
	"Kierkegaard" : (0, 0, 0),
	"Confucius" : (0, 0, 0),
	"Spinoza" : (0, 0, 0),
	"John Rawls" : (0, 0, 0),
	"Sartre" : (0, 0, 0),
	"Heidegger" : (0, 0, 0),
	"Frege" : (0, 0, 0),
	"Derrida" : (0, 0, 0),
	"Foucault" : (0, 0, 0),
	"Simone de Beauvoir" : (0, 0, 0),
	"Machiavelli" : (0, 0, 0),
	"Bacon" : (0, 0, 0),
	"Bentham" : (0, 0, 0),
	"Buddha" : (0, 0, 0),
	"Noam Chomsky" : (0, 0, 0),
	"Voltaire" : (0, 0, 0),
	"Leibniz" : (0, 0, 0),
	"Hegel" : (0, 0, 0)
}

# sort(philosophers)
# print(philosophers)

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
	sort_and_print(philosophers)
	# print_rankings(philosophers)

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
		phil_1_wins = philosophers[phil_1][0] + 1
		phil_1_losses = philosophers[phil_1][1]
		phil_1_w_l = (philosophers[phil_1][2] + 1) * 1.00001
		philosophers[phil_1] = (phil_1_wins, phil_1_losses, phil_1_w_l)

		phil_2_wins = philosophers[phil_2][0]
		phil_2_losses = philosophers[phil_2][1] + 1
		phil_2_w_l = (philosophers[phil_2][2] - 1) * 1.00001
		philosophers[phil_2] = (phil_2_wins, phil_2_losses, phil_2_w_l)

	elif winner == phil_2:
		phil_1_wins = philosophers[phil_1][0]
		phil_1_losses = philosophers[phil_1][1] + 1
		phil_1_w_l = (philosophers[phil_1][2] - 1) * 1.00001
		philosophers[phil_1] = (phil_1_wins, phil_1_losses, phil_1_w_l)

		phil_2_wins = philosophers[phil_2][0] + 1
		phil_2_losses = philosophers[phil_2][1]
		phil_2_w_l = (philosophers[phil_2][2] + 1) * 1.00001
		philosophers[phil_2] = (phil_2_wins, phil_2_losses, phil_2_w_l)

	else:
		print("that's not an option u cunt")
	print()

	count += 1

	user_input = input("Quit? ")
	if user_input == "yes" or user_input == "y":
		quit = True
		exit()

os.system('clear')
print("The Final Ranking Is...")
print()
sort_and_print(philosophers)

# Notes:
# How to proceed. I need a much more efficient algorithm.
# The number of games to play currently increases O(x^2)
# 1600 is arbitrary. Figure out the math.
# I feel like this algorithm way overweighs recent comparissons as compared to more distant comparissons