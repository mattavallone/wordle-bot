'''
solution.py

Description: Get the solution word

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

	return answer

def past(gameId):
	'''
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