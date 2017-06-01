#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: nba.py

winteam = list()
loseteam = list()

sources = ['Warriors 102:87 Sixers', 'Boston 100:101 Rockets', 'Spurs 80:100 Cleavers', 'Warriors 112:108 Cleavers']
for match in sources:
    a = match.split(':')[0].split(' ')
    b = match.split(':')[1].split(' ')
    b[0], b[1] = b[1], b[0]
    if int(a[1]) > int(b[1]):
        winteam.append(a[0])
        loseteam.append(b[0])
    else:
        winteam.append(b[0])
        loseteam.append(a[0])


class NBATeam(object):
    league_team = list()

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0

    def regteam(self):
        self.league_team.append(self.name)


class WestTeam(NBATeam):
    league_wins = 0
    league_loses = 0
    league_name = 'West'
    league_team = list()

    def __init__(self, name):
        NBATeam.__init__(self, name)
        self.check()
        self.regteam()

    def check(self):
        for i in winteam:
            if self.name == i:
                self.wins += 1
                WestTeam.league_wins += 1


class EastTeam(NBATeam):
    league_wins = 0
    league_loses = 0
    league_name = 'East'
    league_team = list()

    def __init__(self, name):
        NBATeam.__init__(self, name)
        self.check()
        self.regteam()

    def check(self):
        for i in winteam:
            if self.name == i:
                self.wins += 1
                EastTeam.league_wins += 1

warriors = WestTeam('Warriors')
spurs = WestTeam('Spurs')
rockets = WestTeam('Rockets')

cleavers = EastTeam('Cleavers')
boston = EastTeam('Boston')
sixers = EastTeam('Sixers')


print winteam
print warriors.league_wins
print warriors.league_name
print sixers.league_wins
print sixers.league_name
print warriors.wins
print sixers.wins
print EastTeam.league_team
print warriors.league_team
