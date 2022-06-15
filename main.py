'''
Wordle Bot

Author: Matthew Avallone
'''

import stats
import player

if __name__ == '__main__':
	# 1. Get list of possible solutions
	allWordsFile = 'all-words.txt'
	solWordsFile = 'words.txt'

	allWords = stats.getWordList(allWordsFile)
	solWords = stats.getWordList(solWordsFile)

	# 2. Compute embedding vectors for each letter and word
	allLetters = stats.getLetterDistrubution(allWords)
	solLetters = stats.getLetterDistrubution(solWords)

	allWordsScores = stats.getWordScores(allWords, allLetters)
	solWordScores = stats.getWordScores(solWords, solLetters)

	# print(allWordsScores)

	# 3. Have player solve wordle
	player.solve(solWordScores)