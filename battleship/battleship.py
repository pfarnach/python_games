import random, sys, os

# Define blank list
board = []
board_length = 4  # starting at zero
letters = ["A", "B", "C", "D", "E"]


#Generate rows with length of 5
for row, letter in zip(range(5), letters):
	# Append a blank list to each row cell
	board.append([])
	for column in range(5):
		# Assign x to each row
		board[row].append("[ " + letter + str(column) + " ]")

def clear():
	os.system('clear')

# Function will print board like an actual board
def print_board(board):
	for row in board:
		print "".join(row)

# takes boat coordinates and "encodes" them based on alpha-numeric code
def boat_loc_int(random_col, random_row):

	if random_col == 0:
		boat_loc = "A" + str(random_row)
	elif random_col == 1:
		boat_loc = "B" + str(random_row)
	elif random_col == 2:
		boat_loc = "C" + str(random_row)
	elif random_col == 3:
		boat_loc = "D" + str(random_row)
	elif random_col == 4:
		boat_loc = "E" + str(random_row)
	
	return boat_loc

# finds adjacent squares for single axis at a time
def generate_adjacent(coordinate):
	if coordinate == 0:
		return 1
	elif coordinate == board_length:
		return board_length -1
	else:
		return coordinate - random.choice([-1,1])

# generates boat coordinates and makes sure they're adjacent
def gen_boat():

	# coordinates for part 1 of 2 for the boat
	random_col1 = random.randint(0,board_length)
	random_row1 = random.randint(0,board_length)

	# coordinates for the second, adjacent part of the boat
	random_col2 = generate_adjacent(random_col1)
	random_row2 = generate_adjacent(random_row1)

	# makes sure that if the two coordinates are diagonal, one axis will randomly align itself with boat
	if random_col2 != random_col1 and random_row2 != random_row1:
		change = random.choice(['random_col2','random_row2'])
		if change == 'random_col2':
			random_col2 = random_col1
		else:
			random_row2 = random_row1

	# encodes the boat coordinates
	boat_loc1 = boat_loc_int(random_col1, random_row1)
	boat_loc2 = boat_loc_int(random_col2, random_row2)

	print boat_loc1, boat_loc2

	return boat_loc1, boat_loc2

# updates the map after a guess, mark depends on if it was a hit or miss
def update_map(mark, guess):
	for indexR, row in enumerate(board):
		for indexC, col in enumerate(board):
			if board[indexR][indexC] == "[ " + guess + " ]":
				board[indexR][indexC] = "[ " + mark + " ]"

# checks user guess and returns if there was a hit or not (for next loop)
def check_guess(guess, boat_loc1, boat_loc2, guesses_left, hit):

	# takes away one guess before 
	guesses_left -= 1

	# checks to see if boat was previously hit and if this guess is a hit = win
	if (guess == boat_loc1 or guess == boat_loc2) and hit > 0:
		clear()
		print "Nice, you DESTROYED the boat! Good going, sport.\n"
		update_map("X ", guess)
		print_board(board)
		print
		sys.exit(0)
	# checks to see if guess = hit on either part of the boat
	elif guess == boat_loc1 or guess == boat_loc2:
		clear()
		print "Nice, you HIT the boat once. Where's the rest of it?\n"
		update_map("X ", guess)
		print "You have %d shots left!\n" % guesses_left
		hit = True
	# then checks to see if out of ammo and exits game
	elif guesses_left <= 0:
		clear()
		print
		print "You're out of ammo, bro.\n"
		update_map("--", guess)
		print_board(board)
		print
		sys.exit(0)
	# then can just assume a miss if still has ammo and guess != hit
	else:
		clear()
		print "Miss. Keep shooting, Tex.\n"
		print "You have %d shots left!\n" % guesses_left
		update_map("--", guess)

	return hit, guesses_left


def main():

	clear()
	alive = True
	guesses_left = 10
	hit = False

	# generates two adjacent boat coordinates
	boat_loc1, boat_loc2 = gen_boat()

	print "You have %d shots to find the hidden boat! (hint, it's 2 spaces long)\n" % guesses_left

	while alive:
		print_board(board)
		guess = raw_input("\n>> Guess a square: ").upper()
		hit, guesses_left = check_guess(guess, boat_loc1, boat_loc2, guesses_left, hit)
		

main()