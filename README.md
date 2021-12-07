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
