# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    print "Start", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    ActualState=0
    ActualChoice=0
    ActualStateList=0
    i=0
    dontpush=0
    counter=0
    PreviousState=problem.getStartState()
    ActualState=PreviousState
#    print "PreviousState", PreviousState
    path = util.Stack()
    actions=util.Stack()
 #   print "Path",path.list
    closed=util.Stack()
    path.push(PreviousState)
    while not problem.isGoalState(ActualState):
	ActualStateList=problem.getSuccessors(PreviousState)
	print "----------------------------------------"
	print "Length",len(ActualStateList)
	print "Successors",ActualStateList
	print "ActualState", ActualState
	print "Iterateuravant",i
	print "Je verifie la condition", ActualStateList[i][0]
	print "----------------------------------------"
	ActualChoice=ActualStateList[i][0]
	while ActualChoice in path.list or path.list in closed.list :
		print "Je change de choix****************************************"
		i=i+1
		if i+1>len(ActualStateList):
			print "Je remonte d'un noeuds*******************************"
			#Je prends la derniere position enregistrer dans le path et j'analyse les successor possible
#			closed.pop()
#			closed.push(ActualState[0])
			closed.push(path.list)
			PreviousState=path.list[len(path.list)-2]
			ActualStateList=problem.getSuccessors(PreviousState)
			path.pop()
			actions.pop()
			print "PATH LOOP:",path.list
        		print "CLOSED LOOP", closed.list
			print "ActualList", ActualStateList
#			print "ActualChoice", ActualChoice
			print "PreviousState", PreviousState
			allo=raw_input("Press Enter to continue...")
			i=0
		ActualChoice=ActualStateList[i][0]
	ActualState=ActualStateList[i]
	if dontpush ==0:
		#Je ferme la possibiliter de retourner au noeauds precedent
#		closed.push(PreviousState)
		#Jenregistre letat actuel dans le path
		path.push(ActualState[0])
		actions.push(ActualState[1])
		PreviousState=ActualState[0]
		i=0
		print "PATH:",path.list
		print "CLOSED", closed.list
	allo=raw_input("Press Enter to continue...")
    return actions.list


"""
	while ActualStateList[i][0] in path.list or ActualStateList[i][0] in closed.list:
		#change de choix
		print "Je ne reviens pas sur mes pas"
		if not ActualStateList[i][0] in closed.list:
                        closed.push(ActualStateList[i][0])
#		print "Length",len(ActualStateList)
#		print "Iterateur",i
#		print "Liste", ActualStateList
		i=i+1

		if len(ActualStateList)<i+2:
                        print "Jenleve un noeuds"
                        ActualStateList=problem.getSuccessors(path.list[counter-1])
                        print "Nouvelle decision a prendre", ActualStateList
                        print "ActualState", path.list[counter-1]
                        print "CLOSED", closed.list
                        path.pop()
                        actions.pop()
                        i=0
                        counter-=1
			if counter<=1:
				counter=1
                        print "Path = ", path.list

		print "Length",len(ActualStateList)
		print "Iterateurrrrrrrrrrr",i
		print "Je verifie la conditionnnnnnnnnn", ActualStateList[i][0]

	ActualState=ActualStateList[i]
#	print "ActualState", ActualState[0]
#	print "CLOSED", closed.list
	path.push(ActualState[0])
	actions.push(ActualState[1])
	i=0
	counter+=1
	PreviousState=ActualState[0]
#	print "Path = ", path.list


#    util.raiseNotDefined()


    return actions.list
"""
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
