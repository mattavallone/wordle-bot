'''
words.py

Description: Gets the solution word for today or previous days

Author: Matthew Avallone
'''

import requests
from bs4 import BeautifulSoup

url = "https://wordfinder.yourdictionary.com/wordle/answers/"

def today():
	'''
	returns today's solution
	'''
	answer = ""
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	spans = soup.find_all('span', {'class' : 'answer'})
	answer = spans[0].get_text().strip().lower()

	h2 = soup.find_all('h2', {'class': 'subheading subheading--top'})
	x, y = h2[0].get_text().strip().lower().split('#')
	gameId, _ = y.split(')')

	return answer, gameId

def past(gameId):
	'''
	input: gameId (int)
	returns the solution for a specific day specified by game ID
	'''
	answer = ""
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	spans = soup.find_all('td')
	for i in range(0, len(spans)):
		if spans[i].get_text().strip() == str(gameId):
			answer = spans[i+1].get_text().strip().lower()
	return answer

def updatePastWords(pastWords):
	answer = ""
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	spans = soup.find_all('td')
	file = open("word_lists/previous-answers.txt", 'a')
	for i in range(0, len(spans)-1):
		answer = spans[i+1].get_text().strip().lower()
		if len(answer) == 5 and answer not in pastWords:
			print('New solution word missing from past answers list:', answer)
			file.write(answer)
			file.write("\n")

	file.close()

def removePastWords(solWords, pastWords):
	'''
	input: list of solution words, list of past solution words
	removes any old solutions from the solution set
	'''
	for pastWord in pastWords:
		solWords.remove(pastWord)

	return solWords