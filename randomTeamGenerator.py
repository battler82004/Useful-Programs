from random import randint

def main():
    print("This is a random team generator created by James Taddei.\n\n")

    numOfTeams = input_num_of_teams()
    teams = []

    blankList = []
    for _ in range(numOfTeams):
        teams.append(list(blankList))

    print("\nEnter all of the players you wish to sort.")
    print("When you're finished, enter 'stop' or 'end'")
    
    inputtedName = ""
    names = []

    while ((inputtedName.lower() != "stop") and (inputtedName.lower() != "end")):
        inputtedName = input_name()
        names.append(inputtedName)

    names = names[0:len(names) - 1]
    print("\n")

    teams = pick_teams(teams, names)

    print_teams(teams)

def input_num_of_teams():
    num = 0
    while (num == 0):
        try:
            num = int(raw_input("Enter the number of teams: "))
        except:
            num = 0

    return num

def input_name():
    name = ""
    while (name == ""):
        try:
            name = raw_input("Enter a name: ")
        except:
            name = ""

    return name

def pick_teams(teams, names):
    while (len(names) > 0):
        for team in range(len(teams)):
            currSorted = names.pop(randint(0, len(names) - 1))
            teams[team].append(currSorted)
            if (len(names) == 0):
                break

    return teams

def print_teams(teams):
    for team in range(len(teams)):
        print("Team " + str(team + 1) + " is -")
        
        for member in range(len(teams[team])):
            print("Member: " + teams[team][member])

        print("\n")

main()
