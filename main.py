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
	answer = solution.today()

	# Have player solve wordle
	state = []
	attempt = 1
	guesses = []
	for attempt in range(5):
		guess = player.computeGuess(solWordScores, attempt, guesses, state)

		guesses.append(guess)

		outcome = player.solve(answer, guess)

		if outcome["win"]:
			print("We have a winner! Wordle is " + guess)
			break
		else:
			attempt += 1
			state = outcome["verdict"]
