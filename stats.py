'''
stats.py

Decription: Functions for computing stats used by player.py

Author: Matthew Avallone
'''

import numpy as np

def getWordList(wordFile):
	words = []
	with open(wordFile) as wordList:
		words = [word[:5] for word in wordList]

	return words

def getLetterDistrubution(words):
	letterDistrubution = {
		"a": [0,0,0,0,0],
		"b": [0,0,0,0,0],
		"c": [0,0,0,0,0],
		"d": [0,0,0,0,0],
		"e": [0,0,0,0,0],
		"f": [0,0,0,0,0],
		"g": [0,0,0,0,0],
		"h": [0,0,0,0,0],
		"i": [0,0,0,0,0],
		"j": [0,0,0,0,0],
		"k": [0,0,0,0,0],
		"l": [0,0,0,0,0],
		"m": [0,0,0,0,0],
		"n": [0,0,0,0,0],
		"o": [0,0,0,0,0],
		"p": [0,0,0,0,0],
		"q": [0,0,0,0,0],
		"r": [0,0,0,0,0],
		"s": [0,0,0,0,0],
		"t": [0,0,0,0,0],
		"u": [0,0,0,0,0],
		"v": [0,0,0,0,0],
		"w": [0,0,0,0,0],
		"x": [0,0,0,0,0],
		"y": [0,0,0,0,0],
		"z": [0,0,0,0,0]
	}

	for word in words:
		for i, letter in enumerate(word):		
			letterDistrubution[letter][i] += 1

	# normalize the vectors between [0,1]
	for letter in letterDistrubution:
		letterDistrubution[letter] = np.divide(letterDistrubution[letter], len(words))

	return letterDistrubution


def getWordScores(words, letterVecs, makeSorted=True):
	wordScores = dict.fromkeys(words)

	for word in words:
		score = (letterVecs[word[0]][0] + letterVecs[word[1]][1] + letterVecs[word[2]][2] + letterVecs[word[3]][3] + letterVecs[word[4]][4]) / 5
		wordScores[word] = score

	if makeSorted:
		return {k: v for k, v in sorted(wordScores.items(), key=lambda item: item[1], reverse=True)}
	else:
		return wordScores

def getWordProbabilities(words, letterVecs, makeSorted=True):
	wordProbs = dict.fromkeys(words)

	for word in words:
		prob = (letterVecs[word[0]][0] * letterVecs[word[1]][1] * letterVecs[word[2]][2] * letterVecs[word[3]][3] * letterVecs[word[4]][4])
		wordProbs[word] = prob

	if makeSorted:
		return {k: v for k, v in sorted(wordProbs.items(), key=lambda item: item[1], reverse=True)}
	else:
		return wordProbs

def getWordMagnitudes(words, letterVecs, makeSorted=True):
	wordMags = dict.fromkeys(words)

	for word in words:
		wordVec = np.array([letterVecs[word[0]][0], letterVecs[word[1]][1], letterVecs[word[2]][2], letterVecs[word[3]][3], letterVecs[word[4]][4]])
		mag = np.linalg.norm(wordVec)
		wordMags[word] = mag

	if makeSorted:
		return {k: v for k, v in sorted(wordMags.items(), key=lambda item: item[1], reverse=True)}
	else:
		return wordMags