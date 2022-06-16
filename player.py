'''
player.py

Description: wordle player

Author: Matthew Avallone
'''

from enum import Enum 
import numpy as np

# Enum for letter verdicts
class LetterVerdict(Enum):
	GREEN = 1
	YELLOW = 2
	GRAY = 3

def computeGuess(wordDict, attempt, guesses, verdict):
	guess = ""
	words = np.array(list(wordDict.keys()))


	match attempt:
		case 1:
			guess = words[0] # grab the top scoring word as the first guess
		case 2:
			# possibleWords = np.where()
			guess = ""
		case 3:
			guess = ""
		case 4:
			guess = ""
		case 5:
			guess = ""
		case 6:
			guess = ""

	return guess

def solve(answer, guess):
	result = {
		"win": False,
		"verdict": [LetterVerdict.GRAY,LetterVerdict.GRAY,LetterVerdict.GRAY,LetterVerdict.GRAY,LetterVerdict.GRAY]
	}

	if guess == answer:
		result["win"] = True
		result["verdict"] = [LetterVerdict.GREEN,LetterVerdict.GREEN,LetterVerdict.GREEN,LetterVerdict.GREEN,LetterVerdict.GREEN]
	else:
		verdict = []
		for i, letter in enumerate(guess):
			if letter == answer[i]:
				verdict.append(LetterVerdict.GREEN)
			elif letter in answer:
				verdict.append(LetterVerdict.YELLOW)
			else:
				verdict.append(LetterVerdict.GRAY)

		result["verdict"] = verdict

	return result