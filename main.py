'''
Wordle Bot

Author: Matthew Avallone
'''

import stats
import player
import words

if __name__ == '__main__':
	# Get list of possible solutions
	allWordsFile = 'word_lists/all-words.txt'
	solWordsFile = 'word_lists/words.txt'
	pastWordsFile = 'word_lists/previous-answers.txt'

	allWords = stats.getWordList(allWordsFile)
	solWords = stats.getWordList(solWordsFile)
	pastWords = stats.getWordList(pastWordsFile)

	# Add any missing previous solutions to list
	words.updatePastWords(pastWords)
	pastWords = stats.getWordList(pastWordsFile)

	# Remove previously used words from solution set
	solWords = words.removePastWords(solWords, pastWords)
	
	# Compute vectors for each letter
	allLetters = stats.getLetterDistrubution(allWords)
	solLetters = stats.getLetterDistrubution(solWords)

	# Compute word scores
	allWordsScores = stats.getWordScores(allWords, allLetters)
	solWordScores = stats.getWordScores(solWords, solLetters)

	# Compute word probabilities
	allWordsProbs = stats.getWordProbabilities(allWords, allLetters)
	solWordProbs = stats.getWordProbabilities(solWords, solLetters)

	# Get today's wordle
	answer, gameId = words.today()
	
	# Have player solve wordle
	states = []
	guesses = []
	for attempt in range(1, 7):
		guess = player.computeGuess(solWordProbs, attempt, guesses, states)
		print("Guess is " + guess + ", Score is " + str(solWordProbs[guess]))

		guesses.append(guess)

		outcome = player.solve(answer, guess)
		
		states.append(outcome["verdict"])

		if outcome["win"]:
			print("We have a winner! Wordle is " + guess + ", Number of Attempts: " + str(attempt))
			break

	player.postResults(states, gameId)