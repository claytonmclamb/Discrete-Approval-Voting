"""
This file is designed to create a class for a bipartite graph to use later.
Specficially, this is designed for discrete approval voting. 
"""

class Bipartite:
    def __init__(self, v, c):
        self.voters = list(range(v))
        self.candidates = (list(range(c)))
        self.edges = []
    
    def add_edge(self, edge):
        self.edges.append(edge)