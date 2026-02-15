from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    # TODO: Add your code here
    #Stack
    
    frontier=utils.Stack()
    frontier.push(problem.getStartState())
    visited=[]
    actions = {}
    initial_state = problem.getStartState()
    actions[initial_state]=[]
    while not frontier.isEmpty():
        node=frontier.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions[node]
            for structure in problem.getSuccessors(node):
                successor=structure[0]
                action=structure[1]
                if successor not in visited:
                    frontier.push(successor)
                    actions[successor] = actions[node] + [action]



def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    #TODO: Add your code here
    frontera=utils.Queue()
    frontera.push(problem.getStartState())
    visitados=[]
    actions = {}
    initial_state = problem.getStartState()
    actions[initial_state]=[]
    while not frontera.isEmpty():
        node=frontera.pop()
        if node not in visitados:
            visitados.append(node)
            if problem.isGoalState(node):
                return actions[node]
            for structure in problem.getSuccessors(node):
                successor=structure[0]
                action=structure[1]
                if successor not in visitados:
                    frontera.push(successor)
                    actions[successor] = actions[node] + [action]
    


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    heap= utils.PriorityQueue()
    visited=set()
    cost={problem.getStartState():0}
    actions={problem.getStartState():[]}
    heap.push((problem.getStartState(), [], 0), 0)
    while not heap.isEmpty():
        vertex, actions,costV=heap.pop()
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        if problem.isGoalState(vertex):
            return actions
        for newVertex,newAction,newCost in problem.getSuccessors(vertex):
            newCost=newCost+costV
            if newVertex not in cost or newCost<cost[newVertex]:
                cost[newVertex]=newCost
                newActions=actions+[newAction]
                heap.push((newVertex,newActions,newCost), newCost)
            
    return []      

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    frontier = utils.PriorityQueue()
    visited = set()
    cost={problem.getStartState():0}
    actions={problem.getStartState():[]}
    initial_state = problem.getStartState()

    eval_function  = cost[initial_state] + heuristic(initial_state, problem)
    frontier.push(initial_state, eval_function)
    
    while not frontier.isEmpty():
        current_state = frontier.pop()
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        if problem.isGoalState(current_state):
            return actions[current_state]

        for successor, action, step_cost in problem.getSuccessors(current_state):
            new_g = cost[current_state] + step_cost
            
            if successor not in cost or new_g < cost[successor]:
                cost[successor] = new_g
                actions[successor] = actions[current_state] + [action]
                
                f_successor = new_g + heuristic(successor, problem)
                

                frontier.push(successor, f_successor)

    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
