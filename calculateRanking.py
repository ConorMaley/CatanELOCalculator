import csv
import sys
import math

def Probability(rating1, rating2):
	return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def CalcElo(PlayerELO, OppELO, ScoreConstant, Status):
	Pb = Probability(PlayerELO, OppELO)
	Pa = Probability(OppELO, PlayerELO)

	# # Player Wins
	# if (Status == 1) : 
	# 	PlayerELO = PlayerELO + ScoreConstant * (1 - Pa) 
	# 	OppELO = OppELO + ScoreConstant * (0 - Pb)

	# # Tie
	# elif (Status == 0.5) :
	# 	PlayerELO = PlayerELO + ScoreConstant * (0.5 - Pa) 
	# 	OppELO = OppELO + ScoreConstant * (0.5 - Pb)

	# # Opp wins
	# else : 
	# 	PlayerELO = PlayerELO + ScoreConstant * (0 - Pa) 
	# 	OppELO = OppELO + ScoreConstant * (1 - Pb)

	# return round(PlayerELO, 2)


	if (Status == 1) : 
		return ScoreConstant * (1 - Pa) 

	# Tie
	elif (Status == 0.5) :
		return ScoreConstant * (0.5 - Pa) 

	# Opp wins
	else : 
		return ScoreConstant * (0 - Pa) 

with open(sys.argv[1]) as input_file:
	csv_reader = csv.reader(input_file, delimiter=',')
	line_count = 0
	Elos = {}
	playersArray = []

	for row in csv_reader:
		if line_count == 0:
			for name in row[1:]:
				Elos[name] = 1200
				playersArray.append(name)
			# print(f'Column names are {", ".join(row)}')
		else:
			index = 0
			Gamescore = {}
			OldElos = {}
			for score in row[1:]:
				if int(score) >= 2:
					Gamescore[playersArray[index]] = score
					OldElos[playersArray[index]] = Elos[playersArray[index]]
				index += 1
			#someone pls tell me if there's a better way to do this
			index = 0
			# print(f'{Gamescore}')
			for player, score in Gamescore.items():
				jindex = 0 #lol thank u pbr
				scoreChange = 0
				for opp, oppScore in Gamescore.items():
					if index != jindex:
						if int(score) > int(oppScore):
							status = 1
						elif int(score) == int(oppScore):
							status = 0.5
						else:
							status = 0
						# print(f'{status} = status')
						# K is constant for now
						tempSC = CalcElo(Elos[player], OldElos[opp], 30, status)
						# print(f'{player} {Elos[player]} scored {score}, Opponent {opp} {OldElos[opp]} scored {oppScore}, change to player {tempSC}')
						scoreChange += tempSC
					jindex += 1
				# print(f'{player} scoreChange = {scoreChange}')
				Elos[player] += round(scoreChange, 2)
				index += 1

		print(f'=============ELO after {line_count} games=============')
		for val in Elos:
			print(f'{val}: {Elos[val]}')

		line_count += 1

	#todo: write to rankings in google sheet
	
	# avg = 0
	# for val in Elos:
	# 	avg += Elos[val]
	# 	print(f'{val}: {Elos[val]}')
	# avg = avg/len(Elos)
	# print(f'Avg Elo: {avg}')