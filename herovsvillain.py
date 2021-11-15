import os
import sys
import re

global cwd
cwd = os.getcwd()

start = "Hand"
flop =  "FLOP"
turn =  "TURN"
river = "RIVER"
end =   "SUMMARY"
dealt = "Dealt"
collected = "collected"
seat = "Seat"
seat1 = "Seat 1"
seat2 = "Seat 2"

checks = "checks"
posts =  "posts"
calls =  "calls"
bets =   "bets"
raises = "raises"
folds =  "folds"
small_blind = "small"
big_blind = "big"

suit_club = '\u2663'
suit_diamond = '\u2666'
suit_heart = '\u2665'
suit_spade = '\u2660'

actions = []
actions.append(start)
actions.append(flop)
actions.append(turn)
actions.append(river)
actions.append(posts)
actions.append(calls)
actions.append(bets)
actions.append(raises)
actions.append(folds)
actions.append(checks)
actions.append(dealt)
actions.append(collected)

flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""

def print_table(hand_title, hand_action):
    if skip_print:
        pass
    clearscreen()
    print(hand_title)
    print(villain_nickname + " "+ villain_button + " " + villain_hand)
    print("-----------------------------")
    print("     " + str(vilbet))
    print("")
    print("     " + flop_table.rstrip() + turn_table.rstrip() + river_table)
    print(" pot: " + str(pot))
    print("")
    print("     " + str(herobet))
    print("-----------------------------")
    print(hero + " " + hero_button + " " + hero_hand)
    print("")
    print(hand_action)
    dumb = input("]")

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

if os.name == 'posix':
    pass

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

pl = 0
history = []
index = 0

incognito = 0
if len(sys.argv) > 1:
    if sys.argv[1] == 'i':
        #incognito mode
        incognito = 1

#incognito = 1

if incognito:
    print("0-17")
else:
    print("chapter 0")
    print("chapter 1")
    print("chapter 2")
    print("chapter 3")
    print("chapter 4")
    print("chapter 5")
    print("chapter 6")
    print("chapter 7")
    print("chapter 8")
    print("chapter 9")
    print("chapter 10")
    print("chapter 11")
    print("chapter 12")
    print("chapter 13")
    print("chapter 14")
    print("chapter 15")
    print("chapter 16")
    print("chapter 17")
try:
    pl = int(input("choose number: "))
except:
    print("enter number 0-17")

if pl >= 0 and pl < 17:
    pass
else:
    print("error file number")
    sys.exit()
hero = "Hero"
villain = "Villain"
villain_nickname = ""
hero_nickname = ""
seat1_nickname = ""
seat2_nickname = ""

if pl == 0:
    f = open(cwd + '\\chapter0.txt',"r")
elif pl == 1:
    f = open(cwd + '\\chapter1.txt',"r")
elif pl == 2:
    f = open(cwd + '\\chapter2.txt',"r")
elif pl == 3:
    f = open(cwd + '\\chapter3.txt',"r")
elif pl == 4:
    f = open(cwd + '\\chapter4.txt',"r")
elif pl == 5:
    f = open(cwd + '\\chapter5.txt',"r")
elif pl == 6:
    f = open(cwd + '\\chapter6.txt',"r")
elif pl == 7:
    f = open(cwd + '\\chapter7.txt',"r")
elif pl == 8:
    f = open(cwd + '\\chapter8.txt',"r")
elif pl == 9:
    f = open(cwd + '\\chapter9.txt',"r")
elif pl == 10:
    f = open(cwd + '\\chapter10.txt',"r")
elif pl == 11:
    f = open(cwd + '\\chapter11.txt',"r")
elif pl == 12:
    f = open(cwd + '\\chapter12.txt',"r")
elif pl == 13:
    f = open(cwd + '\\chapter13.txt',"r")
elif pl == 14:
    f = open(cwd + '\\chapter14.txt',"r")
elif pl == 15:
    f = open(cwd + '\\chapter15.txt',"r")
elif pl == 16:
    f = open(cwd + '\\chapter16.txt',"r")
elif pl == 17:
    f = open(cwd + '\\chapter17.txt',"r")
else:
    pass

hand_lines = []
counter_lines = 0   
for line in f:
    history.append(line)
f.close()

line_counter = 0
counter_hands = 0
action_points = []
for current_line in history:
    if start in current_line:
        counter_hands += 1
    tokens = current_line.split()
    for act in actions:
        if act in tokens and seat not in tokens:
            action_points.append(current_line)
    line_counter += 1
            
print("number of hands: " + str(counter_hands))
dumb = input("]")
marker = 0
current = action_points[marker]
clear_it = 0
pot = 0
back = 0
herobet = 0
vilbet = 0
pot_offset = 0
hand_title = ""
hand_action = ""
hero_hand = ""
villain_hand = ""
hand_title = ""
hand_action = ""
flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""
skip_print = 0
current_hand_number = 0
seat1_nickname = ""
seat2_nickname = ""

while(True):
    but_press = "z"
    if clear_it:
        clear_it = 0
        pot = 0
        herobet = 0
        vilbet = 0
        pot_offset = 0
        hand_title = ""
        hero_hand = ""
        villain_hand = ""
        hand_title = ""
        hand_action = ""
        flop_table = ""
        turn_table = ""
        river_table = ""
        hero_button = ""
        villain_button = ""
        skip_print = 0
        seat1_nickname = ""
        seat2_nickname = ""
        clearscreen()
    else:
        pass
    if but_press == "b" and marker > 0:
        marker -= 1
        back = 1
        current = action_points[marker]
    elif marker <= len(action_points):
        marker += 1
        back = 0
        current = action_points[marker]
    else:
        pass


    if seat1 in current and villain in current:
        seat1_nickname = "villain"
        seat2_nickname = "hero"
    if seat2 in current and hero in current:
        seat2_nickname = "villain"
        seat1_nickname = "hero"
    if start in current:
        current_hand_number += 1
    if posts in current and villain in current and small_blind in current:
        villain_button = "D"
    if posts in current and hero in current and small_blind in current:
        hero_button = "D"
    if flop in current or turn in current or river in current:
        pot_offset = pot
        herobet = 0
        vilbet = 0
        skip_print = 1
    if "Dealt" in current and hero in current:
        hero_hand = current[-8:]
        hero_hand = hero_hand.replace("s", suit_spade)
        hero_hand = hero_hand.replace("h", suit_heart)
        hero_hand = hero_hand.replace("d", suit_diamond)
        hero_hand = hero_hand.replace("c", suit_club)
        skip_print = 1
    if "Dealt" in current and villain in current:
        villain_hand = current[-8:]
        villain_hand_raw = current[-8:]
        villain_hand = villain_hand.replace("s", suit_spade)
        villain_hand = villain_hand.replace("h", suit_heart)
        villain_hand = villain_hand.replace("d", suit_diamond)
        villain_hand = villain_hand.replace("c", suit_club)
        skip_print = 1
    if flop in current:
        flop_table = current[-11:]
        flop_table = flop_table.replace("s", suit_spade)
        flop_table = flop_table.replace("h", suit_heart)
        flop_table = flop_table.replace("d", suit_diamond)
        flop_table = flop_table.replace("c", suit_club)
        skip_print = 1
    if turn in current:
        turn_table = current[-5:]
        turn_table = turn_table.replace("s", suit_spade)
        turn_table = turn_table.replace("h", suit_heart)
        turn_table = turn_table.replace("d", suit_diamond)
        turn_table = turn_table.replace("c", suit_club)
        skip_print = 1
    if river in current:
        river_table = current[-5:]
        river_table = river_table.replace("s", suit_spade)
        river_table = river_table.replace("h", suit_heart)
        river_table = river_table.replace("d", suit_diamond)
        river_table = river_table.replace("c", suit_club)
    if checks in current and villain in current:
        vilbet = 0
        print_table("Hand #" + str(current_hand_number), current)
    if checks in current and hero in current:
        herobet = 0
        print_table("Hand #" + str(current_hand_number), current)
    if folds in current and villain in current:
        vilbet = 0
        clear_it = 1
        print_table("Hand #" + str(current_hand_number), current)
    if folds in current and hero in current:
        herobet = 0
        clear_it = 1
        print_table("Hand #" + str(current_hand_number), current)

    if  raises in current or bets in current:
        tokens = current.split()
        potential_bet = 0
        found_bet = 0

        for t in tokens[::-1]:
            if found_bet:
                break
            isthis_bet = re.findall('\d+', t)
            for potential_bet in isthis_bet:
                if potential_bet.isdigit():
                    if back:
                        pot -= int(potential_bet)
                    else:
                        pot += int(potential_bet)
                        if "DeepStack" in current:
                            vilbet = int(potential_bet)
                        else:
                            herobet = int(potential_bet)
                        pot = pot_offset + herobet + vilbet
                    found_bet = 1
                    print_table("Hand #" + str(current_hand_number), current)
    elif  posts in current or calls in current:
        tokens = current.split()
        potential_bet = 0
        found_bet = 0
        for t in tokens[::-1]:
            if found_bet:
                break
            isthis_bet = re.findall('\d+', t)
            for potential_bet in isthis_bet:
                if potential_bet.isdigit():
                    if back:
                        pot -= int(potential_bet)
                    else:
                        pot += int(potential_bet)
                        if "DeepStack" in current:
                            vilbet += int(potential_bet)
                        else:
                            herobet += int(potential_bet)
                        pot = pot_offset + herobet + vilbet
                    found_bet = 1
                    print_table("Hand #" + str(current_hand_number), current)
    if start in current:
        clear_it = 1


