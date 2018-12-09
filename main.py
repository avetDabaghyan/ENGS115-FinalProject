import json

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class GameList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def printGames(self):
        temp = self.head
        print "      Printing games... "
        while temp is not None:
            print temp.team1 + " - " + temp.team2 + " - " + temp.date
            temp = temp.next
        print "      Done printing. "

class TeamList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def printTeams(self):
        temp = self.head
        print "      Printing teams... "
        while temp is not None:
            print temp.name + " - " + temp.home_country + temp.printPlayers() + "\n"
            temp = temp.next
        print "      Done printing."

    def uniqueAppend(self, new_team): #Appends only new teams.
        temp = self.head
        while temp is not None:
            if temp.name.lower() == new_team.name.lower():
                print new_team.name + " is already registered. "
                return temp
            temp = temp.next
        self.append(new_team)
        print "Registered new team: " + new_team.name
        return new_team


class Team(Node):
    def __init__(self, name=None, player_list = None, manager=None, home_country = None):
        Node.__init__(self)
        self.name = name
        self.player_list = player_list
        self.manager = manager
        self.home_country = home_country

    def printPlayers(self):
        text = ""
        for i in range(len(self.player_list)):
            text += "\n" + self.player_list[i]
        return text

class Game(Node):
    def __init__(self, team1=None, team2=None, date=None, score=None, location=None):
        Node.__init__(self)
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.score = score
        self.location = location

class Player(Node):
    def __init__(self, name=None, last_name=None, country=None):
        Node.__init__(self)
        self.name = name
        self.last_name = last_name
        self.country = country


# class Cup(Node): #Unused, not really necessary.
#     def __init__(self, name=None, date=None, location=None, team_list = None, winner=None, game_list=None):
#         Node.__init__(self)
#         self.name = name
#         self.date = date
#         self.location = location
#         self.team_list = team_list
#         self.winner = winner
#         self.game_list = game_list

def loadData():
    with open('data.json') as data_file:
        json_data = json.load(data_file)

    json_data = json_data["data1"]
    return json_data

def loadGames(json_data):
    all_games = GameList()
    json_games = json_data["allgames"]
    for key in json_games:
        all_games.append(Game(json_games[key]["side1"]["name"].encode("ascii", "replace"), json_games[key]["side2"]["name"].encode("ascii", "replace"), json_games[key]["date"].encode("ascii", "replace"), None, None))
    return all_games

def loadTeams(json_data):
    all_teams = TeamList()
    json_teams = json_data["allteams"]
    for key in json_teams:
        all_teams.append(Team(json_teams[key]["name"].encode("ascii", "replace"), dictToArray(json_teams[key]["players"]), json_teams[key]["manager"].encode("ascii", "replace"), json_teams[key]["country"].encode("ascii", "replace")))
    return all_teams

def dictToArray(data): #Transforms dictionary of unicodes into list of strings. If initial is not unicode, then leaves it as is.
    new_data = []
    for key in data:
        try: new_data.append(data[key].encode("ascii", "replace"))
        except: new_data.append(data[key])
    return new_data

# def saveData(new_json): #Unused.
#     file = open("data1.json", "w")
#     file.write(json.dumps(new_json))
#     file.close()

def main():
    print "start"

    json_data = loadData()
    all_games = loadGames(json_data)
    all_teams = loadTeams(json_data)
    all_games.printGames()
    all_teams.printTeams()

    newteam1 = Team("Chelsea")
    all_teams.uniqueAppend(newteam1)
    newteam2 = Team("Real Madrid")
    all_games.append(Game(all_teams.uniqueAppend(newteam1), all_teams.uniqueAppend(newteam2)))

    print "end"



main()