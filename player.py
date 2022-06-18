'''
player.py

Description: wordle player

Author: Matthew Avallone
'''

from enum import Enum 
import numpy as np
import requests

# Enum for letter verdicts
class LetterVerdict(Enum):
	GREEN = 1
	YELLOW = 2
	GRAY = 3

def computeGuess(wordDict, attempt, guesses, verdicts):
	guess = ""
	words = np.array(list(wordDict.keys()))

	if attempt == 1:
		guess = words[0] # grab the top scoring word as the first guess
	else:
		guess = ""

		grays = []
		greens = []
		yellows = []
		latestGuess = guesses[-1]
		for j, verdict in enumerate(verdicts):
			for i, v in enumerate(verdict):
				if v == LetterVerdict.GRAY:
					if guesses[j][i] not in grays:
						grays.append(guesses[j][i])
				if v == LetterVerdict.GREEN:
					if (i, guesses[j][i]) not in greens:
						greens.append((i, guesses[j][i]))
				if v == LetterVerdict.YELLOW:
					if (i, guesses[j][i]) not in yellows:
						yellows.append((i, guesses[j][i]))

		for word in words:
			if word in guesses:
				continue

			validLetters = 0 # counter to denote when we've found our guess
			for greenIndex, greenLetter in greens:
				if word[greenIndex] != greenLetter:
					break
				else:
					validLetters += 1

			for yellowIndex, yellowLetter in yellows:
				if yellowLetter not in word:
					break
				elif yellowIndex != word.find(yellowLetter):
					validLetters += 1

			for grayLetter in grays:
				if(grayLetter in word):
					validLetters -= 1

			# check if word contains all known letters to be in word
			expectedLetters = len(greens) + len(yellows)
			if validLetters == expectedLetters:
				guess = word
				break

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

def postResults(states, gameId):
	'''
	post results to a Discord server
	'''
	numAttempts = len(states)
	message = "Wordle " + str(gameId) + " " + str(numAttempts) + "/6\n\n"
	for row in states:
		for i in row:
			if i == LetterVerdict.GRAY:
				message += ":black_large_square:"
			if i == LetterVerdict.GREEN:
				message += ":green_square:"
			if i == LetterVerdict.YELLOW:
				message += ":yellow_square:"
		message += "\n"

	payload = {
		"content": message
	}

	requests.post("https://discord.com/api/webhooks/987568689001951252/BGny6ZSGMAR8o_ueA9wSS_NHJe_CMnkNVlSnr-iiqArUzYg7NjyEAVsTtZ3Nj3W075I1", data=payload)