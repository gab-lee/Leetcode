# Strings list

Indexing of strings

- [Start:stop:step]

Methods

- split(): Breaks a string into a list of substrings based on a delimiter (or whitespace by default). Useful for parsing input or processing words in a sentence.
- strip()
- Join
- replace(old, new): replace all occurrences of a substring with another.
- pop(index)

use append instead of list += [x].
using += creates a new list every time.
if adding a list append will create a nested list, so use extend instead

for loops half open (start,stop,step)
does not touch stop. to go backwards you do (len -1,-1,-1)
