'''
Wordle Bot

Author: Matthew Avallone
'''

import stats
import player
import solution

if __name__ == '__main__':
	# Get list of possible solutions
	allWordsFile = 'all-words.txt'
	solWordsFile = 'words.txt'

	allWords = stats.getWordList(allWordsFile)
	solWords = stats.getWordList(solWordsFile)

	# Compute embedding vectors for each letter and word
	allLetters = stats.getLetterDistrubution(allWords)
	solLetters = stats.getLetterDistrubution(solWords)

	allWordsScores = stats.getWordScores(allWords, allLetters)
	solWordScores = stats.getWordScores(solWords, solLetters)

	# print(allWordsScores)

	# Get today's wordle
	answer, gameId = solution.today()
	
	# Have player solve wordle
	states = []
	guesses = []
	for attempt in range(1, 7):
		guess = player.computeGuess(solWordScores, attempt, guesses, states)
		print("Guess is " + guess + ", Score is " + str(solWordScores[guess]))

		guesses.append(guess)

		outcome = player.solve(answer, guess)
		
		states.append(outcome["verdict"])

		if outcome["win"]:
			print("We have a winner! Wordle is " + guess + ", Number of Attempts: " + str(attempt))
			break

	player.postResults(states, gameId)