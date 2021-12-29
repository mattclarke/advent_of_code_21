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

## Day 9
- Part 1: loop over all the positions to find lows.
- Part 2: from each low effectively do a BFS until we reach all points reachable that are less than 9, count the points.
Sort to find the three biggests counts then multiple.

## Day 10
- Part 1: use a stack, for opening brackets push and for closing brackets pop. If the popped value doesn't pair with the
closing bracket then it is illegal.
- Part 2: Remove the illegal ones. Repeat the stack building for the others, anything left in the stack at the end is
unpaired, so do the maths bit.

## Day 11
- Part 1: didn't read the instructions very well. Loop through all positions and add 1, queue up if greater than 9.
Go through the queue and add 1 to all the neighbours, if the neighbour exceeds 9 then add to queue (only if it hasn't
been added before - can only flash once). Finally set all the ones that flashed to zero.
- Part 2: Extend part 1 slightly to find the point where they all flash at once.

## Day 12
- Part 1: DFS but stop if we visit a small cave twice.
- Part 2: same but allowed to visit one and only one small cave twice. Just needed an extra flag to indicate that we
have visited a small cave twice.

## Day 13
- Part 1: simple maths to calculate the reflection. Used a set to save worrying about overlapping points.
- Part 2: run until done, then read the answer formed by the points.

## Day 14
- Part 1: simple enough, can be done via brute force by building up the polymer.
- Part 2: takes forever to do via brute force. First attempt was to change to a linked list but that still took forever.
A couple of hours later it occurred to me that we only need to keep count of the number of pairs, so it basically works
like this: if we have 10 ABs then that gives us 10 more ACs and CBs (assuming formula is AB -> C), but gives us 10 fewer
ABs and so on.

## Day 15:
- Part 1: used Dijkstra's algorithm (or is it A*?) but took me ages to get something quick.
- Part 2: just extended it to be five times the size and added a helper method to calculate the risk. Initial version
took 10 minutes to complete with pypy, but re-write takes a couple of seconds. The mistake I initially made was to use
the distance from the target as the heap priority, much better to use the distance so far.

## Day 16:
- Part 1: took me a while to fully understand what was meant by "total length in bits" and what to do with it. Otherwise,
it is just parsing the packet.
- Part 2: just add in the maths parts, pretty straightforward once part 1 is done.

## Day 17:
- Part 1: over complicated it at first; can be done quickly via brute force.
- Part 2: small modification to track unique velocities.

## Day 18:
- Part 1: turn the string into a tree and then use various different recursions to explode and split then do the
calculation.
- Part 2: just some extra loops to check all the combinations to find the maximum.
TODO: perhaps revisit to see if can be tidied up. E.g. the explode function is a bit complicated.

## Day 19:
- Part 1: assume scanner 0 is at (0, 0, 0), go through the other scanners one at a time and for each beacon align it with
one of scanner 0's beacons and then see if 12 or more, now offset, beacons overlap and if so add the non-overlapping
beacons to the beacons in scanner 0, if not then try a different orientation. Repeat until all scanners have overlapped.
Takes ~45 seconds with pypy - the orientation changes could be sped up for some gain, but at the moment cannot think of
a quicker solution.
- Part 2: simple. Keep the scanner offsets from part 1 and use them to calculate the Manhattan distances.

## Day 20:
- Part 1: like Conway's GoL with 8 neighbours but every other turn the squares outside our puzzle input switch from all
on to all off. This means we need to treat the edges differently each turn.
```
? = our puzzle surrounded by infinity
# = light on
. = light off

Odd turn             Even turn
#########            .........
##?????##            ..?????..
##?????##            ..?????..
##?????##            ..?????..
##?????##            ..?????..
#########            .........
```
- Part 2: simple once part 1 is done.

## Day 21:
- Part 1: simple looping just to get an idea of the game for part 2.
- Part 2: dynamic programming with recursion on each dice roll. Use caching to avoid it taking the rest of time to finish
(only takes a few seconds to complete).

UPDATED: no longer recurse on each roll as it is only necessary to recurse on the third roll.

## Day 22:
- Part 1: brute force looping
- Part 2: got stuck, so looked on the web - turns out to be relatively simple. Solution is to construct a list of "ons"
and "offs". For each cube in the input (A), compare it to the cubes already in the list if they overlap then add the overlap
to the list and mark it as "off" if the cube in the list was "on" and vice versa. If A was "on" then add it to the list.
Finally tally up the volume by adding the "on" cubes and subtracting for the "off" cubes.

## Day 23:
- Part 1: recursion to try all the possible moves (~100 seconds with pypy)
- Part 2: same but extended for extra "home" spaces and more "pieces" (~22s with pypy)

First part is slow - is there a way to prune the possible moves or is there a more optimal approach generally?
According to the internet DP makes a lot of difference.

Update: Not in the position to do proper DP without a major rewrite but by caching (board, score) we can avoid repeating
the same positions which brings the whole thing down to ~10s with pypy.

## Day 24:
- Part 1: brute force recursion with DP for a significant speed-up but still very very slow (~15-20 minutes).
- Part 2: same but as it starts closer to the value it doesn't take so long.

How difficult is it to change each sub-program into code? E.g. first program is effectively `z = w + 7`

## Day 25:
- Part 1: simple looping over positions to do moves. Sets make it simple, just need to process the east facing ones first.
- Part 2: no part 2 as usual!
