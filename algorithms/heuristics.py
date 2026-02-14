import math as m
from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    total_distance=  abs(state[0]-problem.goal[0]) + abs(state[1]-problem.goal[1])
    return total_distance


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    total_distance= m.sqrt((problem.goal[0]-state[0])**2+ (problem.goal[1]-state[1])**2)
    return total_distance


def manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    position, survivors = state
    
    if survivors in problem.heuristicInfo:
        return problem.heuristicInfo[survivors]
    
    if survivors.count() == 0:
        return 0

    survivor_positions = []
    for x in range(survivors.width):
        for y in range(survivors.height):
            if survivors[x][y]:
                survivor_positions.append((x, y))
    
    nodes = [position] + survivor_positions
    n = len(nodes)
    
    if n <= 1:
        return 0
    
    visited = [False] * n
    visited[0] = True
    mst_cost = 0
    
    for _ in range(n - 1):
        min_edge = float('inf')
        min_node = -1
        
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j]:
                        dist = manhattan_dist(nodes[i], nodes[j])
                        if dist < min_edge:
                            min_edge = dist
                            min_node = j
        
        visited[min_node] = True
        mst_cost += min_edge
    
    problem.heuristicInfo[survivors] = mst_cost
    return mst_cost
