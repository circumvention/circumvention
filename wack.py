# Simulation game of traveling out west in 1800's

import random
import time
import sys

welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck, and see you in Oregon!"

# Model -- variables that collectively represent the state
# of the game
sick = 2
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
player_name = None
sickness_event = ['You have gotten bit my a snake.. Ouch, You lost 1 health.', 'A bee has stung you.. You have lost 1 health', 'You have contracted an illness and have lost 1 health.']

# Constants -- parameters that define the rules of the game,
# but which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7
days = random.randint(3, 7)

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5
MilesRemain = 2000
time1 = 0

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]


# Converts are numeric date into a string.
# input: m - a month in the range 1-12
# input: d - a day in the range 1-31
# output: a string like "December 24".
# Note: this function does not enforce calendar rules. It's happy to output
# impossible strings like "June 95" or "February 31"
def date_as_string(m, d):
	m = month
	d = day
def date_report():
	print(str(Date))

def miles_remaining():
  global MilesRemain
  MilesRemain = MilesRemain - int(travel)

def date_update():
  global NAME_OF_MONTH
  global month
  global months
  global day
  global days
  
  for num in MONTHS_WITH_31_DAYS:
    if month == num and day >= 28:
     month += 1
     day = 0
  for num2 in MONTHS_WITH_30_DAYS:
    if month == num2 and day >= 27:
     month += 1
     day = 0
  for num3 in MONTHS_WITH_28_DAYS:
    if month == num3 and day >= 26:
     month += 1
     day = 0
  
        
def randomsickness():
  global health_level
  if sick == 3:
    print(sickness_event[random.randint(0,2)])
    health_level =  health_level - 1



def consume_food():
	print('eat food')

# Repairs problematic values in the global (month, day) model where the day is
# larger than the number of days in the month. If this happens, advances to the next
# month and knocks the day value down accordingly. Knows that different months have
# different numbers of days. Doesn't handle cases where the day is more than 28
# days in excess of the limit for that month -- could still end up with an
# impossible date after this function is called.
#
# Returns True if the global month/day values were altered, else False.

# Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness. The sickness rules are quirky: player
# is guaranteed to fall ill a certain number of times each month, so illness
# needs to keep track of month changes.
#
# input: num_days - an integer number of days that elapse.


def handle_travel():
  global miles_traveled
  global day
  global travel
  global sick
  global days
  global time2
  date_update()
  travel = random.randint(30,60)
  days = random.randint(3, 7)
  print('You have traveled ' + str(travel) + ' miles, And it took a total of ' + str(days) + ' days')
  miles_traveled = miles_traveled + int(travel)
  day = day + int(days)
  sick = random.randint(0,5)
  miles_remaining()
  randomsickness()
  time2 = 0

	 

def handle_rest():
  global health_level
  global day
  global time2
  if health_level == 5:
    print('You already have the maximum amount of health.')
  else:
    print('You have decided to rest')
    for remaining in range(5, 0, -1):
      sys.stdout.write("\r")
      sys.stdout.write("Resting... {:2d} seconds remaining.".format(remaining))
      sys.stdout.flush()
      time.sleep(1)
  print('\nYou have finished resting and earned 1 health point ')
  health_level += 1
  day += random.randint(1, 5)
  
  


def handle_hunt():
  global day
  global food_remaining
  days = int(random.randint(2, 5))
	
  print('You have hunted and gained 100lbs, It took a total of ' + str(days) + ' days.')
  day += days
  food_remaining += 100

def handle_status():
	print('Status: ' + '\t\nFood: ' + str(food_remaining) + 'lbs'+'\t\nHealth: ' + str(health_level) + '\t\nDistance Traveled: ' + str(miles_traveled) + '\t\nDay: ' + str(day) + '\t\nMonth: ' + str(month) + '\nMiles Remaining: ' + str(MilesRemain))

def handle_help():
  print(help_text)

def handle_quit():
	global playing
	playing = False


def handle_invalid_input(response):
	print("'{0}' is not a valid command. Try again.".format(response))


def game_is_over():
	print('You have died.')

def player_wins():
  print("\n\nCongratulations you made it to Oregon alive!")
  exit()
  
def loss_report():
	print('You have lost')

print(welcome_text + help_text + good_luck_text)
player_name = input("\nWhat is your name, player?: ")

playing = True
while playing:
  
  if miles_traveled >= 2000:
    player_wins()
  print()
  action = input("Choose an action, {0}-->".format(player_name))
  if action == "travel" or action == "t":
    handle_travel()
  elif action == "rest" or action == "r":
	  handle_rest()
  elif action == "hunt" or action == "h":
	  handle_hunt()
  elif action == "quit" or action == "q":
    handle_quit()
  elif action == "help" or action == "?":
	  handle_help()
  elif action == "status" or action == "s":
	  handle_status()
  else:
	  handle_invalid_input(action)

  if health_level <= 0:
    playing = False
    
  if month == 12 and day == 31:
    print('You ran out of time..')
    playing = False

else:
  print("\n\nAlas! You lose.")
  print('\nYou died with:')
  handle_status()
