# advent_of_code_21
https://adventofcode.com/2021

## Day 1
- Part 1: looping, comparing and counting.
- Part 2: loop once to collect the group of threes and then do the counting in a separate loop.
Can we do it in one loop? Yes - keep 3 in the list and do the maths.
Can we do it without popping and appending? Yes - using a sliding score.

## Day 2
- Part 1 & 2: basic string parsing and maths.

## Day 3
- Part 1 & 2: binary and looping.

## Day 4
- Part 1 & 2: creating the bingo boards then looping over the numbers called then checking for a winner.
Could we reduce the amount of looping? Perhaps a 1D array? Yes, better but still pretty ugly.

## Day 5
- Part 1: simple.
- Part 2: Took me a bit of time to get the diagonals correct.

## Day 6
- Part 1: as the number of days is low, we can just add a fish to the list for each one born.
- Part 2: because the number of fish increases exponentially we need to be a bit cleverer: we track the number of fish
born on a day rather than each individual fish.

## Day 7
- Part 1: loop over all the possible positions and find the best one.
- Part 2: need to find the sigma of the difference, first version used recursion and memoisation to find sigma. While
looking up the name "sigma" found the formula for it: (x*x + x)/2 which is a bit simpler!

## Day 8
- Part 1: count the number of inputs with a segment lengths corresponding to the digits 1, 4, 7, 8 as they are unique.
- Part 2: Started going down the wrong path of trying to work out what a to g were individually then realised that was
not required. Instead we only need to know the "ab" is 1, we don't need to know what "a" is. It is trivial to work
out 1, 4, 7, 8 because they each have a unique number of segments. The others can be determined by their segment count
and the number of intersection they have with 1 and 4. E.g. "6" has 6 segments but only has one intersection with "1"
while "0" and "9" have two intersections with "1" but "9" has more intersections with "4" than "0" does.
