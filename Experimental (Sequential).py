"""
This file brute forces values of v, k, c to find piercing numbers.
These are the bounds: 1 <= v <= c
                      1 <= k <= c 
"""
import Bipartite
import Combinations
import Piercing
import pandas as pd

df = pd.DataFrame(columns = ("Number of Voters", "Degree of Voters", "Number of Candidates", "Piercing Number Found"))
min_c = 1
max_c = 5
values_of_c = list(range(min_c, max_c + 1))

for c in values_of_c:
    values_of_v = list(range(1, c + 1))
    values_of_k = list(range(1, c + 1))
    for v in values_of_v:
        for k in values_of_k:
            print("Working on:", c, "Candidates,", v, "Voters", k, "Votes")
            voter_patterns = Combinations.possibleVotingPatterns(k, c)
            possible_voter = Combinations.possibleVoters(voter_patterns, v)
            # go through each possibility
            for possibility in possible_voter:
                G = Bipartite.Bipartite(v, c)
                for i in range(len(possibility)):
                    for candidate in possibility[i]:
                        G.add_edge((i, candidate))
                piercing_number = Piercing.findPiercing(G)
                new_row = {'Number of Voters': v, 'Degree of Voters': k, "Number of Candidates": c, "Piercing Number Found": piercing_number}
                df.loc[len(df)] = new_row
df.to_csv(f'data-{min_c}-through-{max_c}.csv', index=False)


