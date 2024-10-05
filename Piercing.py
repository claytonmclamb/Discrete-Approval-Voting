"""
This file provides functionality to find the piercing/hitting number of a given bipartite graph. 
This is designed for the discrete approval voting project. 

In the final written project, we should prove the correctness of this greedy algorithm.
"""
import Bipartite
import Combinations

def findPiercing(G):
    voters_satisfied = set()
    degrees = degree(G, voters_satisfied)
    piercing = 0
    while len(voters_satisfied) < len(G.voters):
        candidate = findHighestDegreeCandidate(degrees)
        new_voters_satisfied = findVotersViaCandidate(G, candidate)
        voters_satisfied = voters_satisfied | new_voters_satisfied
        degrees = degree(G, voters_satisfied)
        piercing += 1
    return piercing
    

def degree(G, voters_satisfied):
    degree_mapping = {}
    for voter, candidate in G.edges:
        if voter in voters_satisfied:
            continue
        if candidate in degree_mapping:
            degree_mapping[candidate] += 1
        else:
            degree_mapping[candidate] = 1
    return degree_mapping

def findHighestDegreeCandidate(degree_mapping):
    candidate = -1
    degree = float('-infinity')
    for c in degree_mapping:
        if degree_mapping[c] > degree:
            degree = degree_mapping[c]
            candidate = c
    return candidate

def findVotersViaCandidate(G, chosenCandidate):
    voters = []
    for voter, candidate in G.edges:
        if candidate == chosenCandidate:
            voters.append(voter)
    return set(voters)