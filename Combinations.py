"""
This file is designed to do the combinatorics for discrete approval voting. 
"""
import math
from itertools import combinations

def possibleVotingPatterns(k, c):
    # This gives us the possible voting patterns given a degree and number of candididates
    # For example in (2, 3) - we can have (AB), (AC), and (BC) - this returns this in integer format
    candidates = list(range(c))
    patterns = list(combinations(candidates, k))
    return patterns

def numPossibleVotingPatterns(k, c):
    return int(math.factorial(c) / (math.factorial(k) * math.factorial(c - k)))

def possibleVoters(patterns, v):
    # This gives us the possible edge combinations given a number of voters
    # For example with a degree of 2 and 3 candidates we have (AB), (AC), and (BC) possible votes
    # But if we have two voters we could have (AB, AC), (AB, BC), or (AC, BC). This function returns these combinations. 
    voter_patterns = list(combinations(patterns, v))
    return voter_patterns

def numPossibleVoters(k, c, v):
    numPatterns = numPossibleVotingPatterns(k, c)
    return int(math.factorial(numPatterns) / (math.factorial(v) * math.factorial(numPatterns - v)))