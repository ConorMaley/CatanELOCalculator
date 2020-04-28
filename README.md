# Catan ELO Calculator
This is a Python script that takes a csv file of Settlers of Catan games and produces an [ELO ranking](https://en.wikipedia.org/wiki/Elo_rating_system) of the participants.

My friends and I have been playing **a lot** of Catan online against each other during the ~~covid-19 pandamic~~ rona stay at home order of 2020 via the [Catan Classic App](https://www.catan.com/game/catan-ios) doing tournaments and keeping track of various expedition matches.

[Here's the spreadsheet we've been using to keep track of our games.](https://docs.google.com/spreadsheets/d/11Z12T3DNaf1KPdOxYTRTKXOdDyQGmcn8VXA--y3EnnI/edit?usp=sharing)

## Getting Started

You need [Python 3.6+](https://www.python.org/downloads/) installed.

Open your favorite command line and run

```bash
calculateRanking.py mastersheet.csv
```

I've provided a sample csv namely `mastersheet.csv`, but you can use whatever file you want as long as it follows the pattern of `mastersheet.csv`:

- row 0 : `Date,Player 1 name,Player 2 name,Player 3 name...`
- row `n>0` : `<dateOfMatch>,P1 Victory Points,P2 Victory Points,P3 Victory Points...`
- For every player that didn't play in the match, give them 0 victory points.

## Calculation Details

For each match, each player's new ELO is calculated by summing up the ELO change as if the player was playing a 1v1 match against each of their opponents.

The ELO change is calculated by taking the sum of the following against each of their opponents:

A win status (1 if they have more VPs, 0 if they have less, 0.5 for a tie) minus the [ELO probability function](https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details) (the big funtion with the 10^(ELOdiff/400)) multiplied by a "game importance factor" named K, which is always 30... *for now*. 

```
K * (winStatus - ELOProbability) 
```

Example: Player 1 scores 10 VPs, Player 2 scores 8 VPs, Player 3 scores 8 VPs, Player 4 scores 6 VPs.

Player 1's new ELO = 
```
Player 1's old ELO
+ 30 * (1 - ELOProbability(Player 1, Player 2))
+ 30 * ( 1 - ELOProbability(Player 1, Player 3)) 
+ 30 * (1 - ELOProbability(Player 1, Player 4))
```
Player 2's new ELO = 
```
P2's Old ELO
+ 30 * (0 - ELOProbability(P2, P1))
+ 30 * (0.5 - ELOProbability(P2, P3)) 
+ 30 * (1 - ELOProbability(P2, P4))
```
Player 3's new ELO = 
```
P3's Old ELO
+ 30 * (0 - ELOProbability(P3, P1))
+ 30 * (0.5 - ELOProbability(P3, P2)) 
+ 30 * (1 - ELOProbability(P3, P4))
```
Player 4's new ELO = 
```
P4's Old ELO
+ 30 * (0 - ELOProbability(P4, P1))
+ 30 * (0 - ELOProbability(P4, P2)) 
+ 30 * (0 - ELOProbability(P4, P3))
```

All players begin with a score of 1200 at their first game.

## Future improvements
_There's a lot of them..._
- ~~Sort after completing~~
- Provide different options
- Variable K constant: weight by date
- Hook up google sheets API for easy updates
- UI for different calculation types