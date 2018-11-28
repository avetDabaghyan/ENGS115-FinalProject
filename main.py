import json

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node

class Team:
    def __init__(self):
        self.name = None
        self.player_list = None #array maybe
        self.coach = None
        self.home_country = None

class Game:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.date = None
        self.score = None
        self.cup = None
        self.location = None

class Player:
    def __init__(self):
        self.name = None
        self.last_name = None
        self.country = None

class Cup:
    def __init__(self):
        self.name = None
        self.date = None
        self.location = None
        self.team_list = None
        self.winner = None


def main():
    print "start"


    print "end"
    #load games
    #load teams
    #print games, teams
    #add game, team
    #save games, teams

    #FOR LATER:
    #graph?


main()