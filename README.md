# Golf Horse Submissions
These are submissions I have made to [golf.horse](http://golf.horse/), challenges to write javascript programs that use as few bytes as possible to output the given text. Currently, I've only done the Pokemon one.
## Pokemon
### Approach
The required output here is a list of pokemon of varying lengths, separated by newlines. It's mostly lowercase letters, but there a few unusual characters thrown in. My approach was to encode the characters as a string of bits, using fewer bits for the more frequent characters. I was inspired by watching [Nicer Trees Spend Fewer Bytes](https://www.youtube.com/watch?v=JYN25TeM5kI) and used their method to encode binary data in a template literal in base-125.

Since the output is allowed to be in any order, I re-arrange the list to be sorted first by length, then alphabetically. This lets me store all the names back-to-back with no delimiting character between, except for the times the name length increases. I also put one bit at the start of each name to indicate whether or not it has the same first letter as the previous name. There's a tradeoff to sorting this way because it prevents making use of repeated starting letters between pokemon of different lengths, but I think it may have turned out to be worth the cost.

There's probably much more room for optimization with this approach, but I think this works well for a first submission.

### Files
**pokemon.txt** - Original file specifying the required output  
**PokemonLetterFrequency.csv** - Calculations on letter frequencies and planning an efficient way to distribute the number of bits each character can use  
**encode.py, decode.py** - I used Python scripts to encode the data and to test decoding it.  
**data.bin** - The output and input for the Python scripts, which I copied into the final Javascript program  
**decode.js** - Slightly more readable version of the submission file. Does the same thing as decode.py.  
**submission.js** - Submission to [golf.horse](http://golf.horse/).  
