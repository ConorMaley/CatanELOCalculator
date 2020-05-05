import csv
import sys
import math

def Probability(rating1, rating2):
	return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def CalcEloChange(PlayerELO, OppELO, ScoreConstant, Status):
	# Pb = Probability(PlayerELO, OppELO)
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
	Elos = {}
	
	playersArray = []
	highestELO = {}
	highestELO['score'] = 1200
	lowestELO = {}
	lowestELO['score'] = 1200

	for line_count, row in enumerate(csv_reader):
		if line_count == 0:
			for name in row[1:]:
				Elos[name] = 1200
				playersArray.append(name)
			# print(f'Column names are {", ".join(row)}')
		else:
			Gamescore = {}
			OldElos = {}
			for index, score in enumerate(row[1:]):
				if int(score) >= 2:
					Gamescore[playersArray[index]] = score
					OldElos[playersArray[index]] = Elos[playersArray[index]]
			for index, (player, score) in enumerate(Gamescore.items()):
				scoreChange = 0
				for jindex, (opp, oppScore) in enumerate(Gamescore.items()):
					if index != jindex:
						if int(score) > int(oppScore):
							status = 1
						elif int(score) == int(oppScore):
							status = 0.5
						else:
							status = 0
						# print(f'{status} = status')
						# K is constant for now
						tempSC = CalcEloChange(Elos[player], OldElos[opp], 30, status)
						# print(f'{player} {Elos[player]} scored {score}, Opponent {opp} {OldElos[opp]} scored {oppScore}, change to player {tempSC}')
						scoreChange += tempSC
				# print(f'{player} scoreChange = {scoreChange}')
				Elos[player] += round(scoreChange, 2)

		# print(f'=============ELO after {line_count} games=============')
		for name in sorted(Elos, key=Elos.get, reverse=True):
			# not very efficient
			if Elos[name] > highestELO['score']:
				highestELO['score'] = Elos[name]
				highestELO['player'] = name
				highestELO['game'] = line_count
			elif Elos[name] < lowestELO['score']:
				lowestELO['score'] = Elos[name]
				lowestELO['player'] = name
				lowestELO['game'] = line_count
			# print(f'{name}: {Elos[name]}')
		# print(f'{sorted( ((name, score) for score, name in Elos.items()), reverse=True)}')
		# newScore = '{} : {}'.format(name, score) for score, name in Elos.items() }
		# print(f'{newScore}')
		# print(f'Game {line_count} {repr(Elos.items())}')
	
	#todo: write to rankings in google sheet
	
	# for avg, val in enumerate(Elos):
	# 	avg += Elos[val]
	# 	print(f'{val}: {Elos[val]}')
	# avg = avg/len(Elos)
	# print(f'Avg Elo: {avg}')

	# Final rankings
	print('=============Final ELO count=============')

	print(f'Highest ELO: {highestELO}')
	print(f'Lowest ELO: {lowestELO}')

	for name in sorted(Elos, key=Elos.get, reverse=True):
		print(f'{name}: {Elos[name]}')