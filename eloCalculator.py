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