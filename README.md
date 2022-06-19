# Wordle Bot

A bot that plays wordle and posts the results to Discord

## Version 1.0
### Strategy
The bot computes the frequency of each alphabet letter appearing at a specific position in a word (using the list of solution words) and stores the frequencies inside a vector for each letter. Then it uses the letter vectors to compute an overall score for each solution word. A score describes the likelihood of that word being the true solution.

### Performance
Winning Percentage: 97.62%

Avg. Attempts Per Win: 3.899

Avg. Attempts Total: 3.949
