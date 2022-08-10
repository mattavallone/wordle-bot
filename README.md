# Wordle Bot

A bot that plays wordle and posts the results to Discord

## Version 1.0
### Strategy
The bot computes the frequency of each alphabet letter appearing at a specific position in a word (using the list of solution words) and stores the frequencies inside a vector for each letter. Then it uses the letter vectors to compute an overall score for each solution word. A score describes the likelihood of that word being the true solution.

### Performance
Winning Percentage: 97.62%

Avg. Attempts Per Win: 3.899

Avg. Attempts Total: 3.949

## Version 2.0
### Strategy
Same strategy as v1.0, except:

* Filtering out previous solution words from the set of possible answers
* Using the letter vectors to compute the probability for each remaining solution word

### Performance
Winning Percentage: 97.97%

Avg. Attempts Per Win: 3.875

Avg. Attempts Total: 3.918

## Version 3.0
### Strategy
Same strategy as v2.0, except:

* Using the letter vectors to compute the magnitude for each remaining solution word

### Performance
Winning Percentage: 97.53%

Avg. Attempts Per Win: 3.930

Avg. Attempts Total: 3.981
