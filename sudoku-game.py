from sudoku import Sudoku
import queue
from copy import copy, deepcopy
import time
start_time = time.time()


q = queue.Queue()
s = queue.LifoQueue()
list = []

'''
Parameters: Takes as input the curr_board state and the puzzle
Returns: True if the current board state is the goal and False if not
Note: Existing version solves the puzzle everytime you test for goal
      feel free to change the implementation to save time
'''
def test_goal(curr_board,puzzle):
    puzzle_solution=puzzle.solve()
    try:
        solution_board=puzzle_solution.board
        for i in range(len(solution_board)):
            for j in range(len(solution_board[i])):
                assert(curr_board[i][j]==solution_board[i][j])
        return True
    except Exception as e:
        return False

'''
Parameters: Takes as input a puzzle board and puzzle size
Returns: True if the puzzle board is valid and False if not
'''    
def valid_puzzle(puzzle_size,puzzle_board):
    puzzle=Sudoku(puzzle_size,board=puzzle_board)
    return puzzle.validate()

'''
Parameters: Takes as input a puzzle board
Returns: Returns all the cells in the grid that are empty
'''
def empty_cells(puzzle_board):
    empty_cell_list=[]
    for i in range(len(puzzle_board)):
        for j in range(len(puzzle_board[i])):
            if puzzle_board[i][j] is None:
                empty_cell_list.append([i,j])
    return empty_cell_list

'''
params: Takes the current puzzle as input
Return: The puzzle board corresponding to the goal
Note: You can modify the function definition as you see fit
'''





def bfs(puzzle):

    q.put(deepcopy(puzzle)) #put first element in queue
    miss = 0

    while not q.empty():

        for x in range(q.qsize()):
            state = q.get()

            for i in range(4):
                for j in range(4):  # searches matrix of sudoku board to find none slots
                    if state.board[i][j] is None: # if not a possible solution yet, create instances

                        for count in range(4):
                            state.board[i][j] = count + 1
                            # place number on board from 1-4 where there is a none slot
                            # test each instance, if solved return, if not solved yet add to queue
                            if test_goal(state.board, state):
                                print("solved")
                                print(state.show())
                                return
                            else:
                                miss+=1
                                print("instances:", miss)
                                q.put(deepcopy(state))

                        state.board[i][j] = None

'''
params: Takes the current puzzle as input
Return: The puzzle board corresponding to the goal
Note: You can modify the function definition as you see fit
'''
miss = 0
def dfs(puzzle):
    new_queue = queue.LifoQueue()
    miss = 0
    new_queue.put(puzzle) #make new stack set solution to not found and

    while not new_queue.empty() :

        testSudoku = new_queue.get()

        if test_goal(testSudoku.board, testSudoku):
            print("solved")
            print(testSudoku.show())
            return testSudoku

        miss+=1

        print("instances: ", miss)
        for i in range(4):
            for j in range(4):  # searches matrix of sudoku board to find none slots
                if testSudoku.board[i][j] is None:
                    for count in range(4):
                        temp = deepcopy(testSudoku)
                        temp.board[i][j] = count + 1
                        new_queue.put(temp)

'''
params: Takes the current puzzle as input
Return: The puzzle board corresponding to the goal
Note: You can modify the function definition as you see fit
'''
def bfs_with_prunning(puzzle):

    q.put(deepcopy(puzzle)) #put first element in queue
    miss = 0

    while not q.empty():

        for x in range(q.qsize()):
            state = q.get()

            for i in range(4):
                for j in range(4):  # searches matrix of sudoku board to find none slots
                    if state.board[i][j] is None: # if not a possible solution yet, create instances

                        for count in range(4):
                            state.board[i][j] = count + 1
                            # place number on board from 1-4 where there is a none slot
                            # test each instance, if solved return, if not solved yet add to queue
                            if test_goal(state.board, state):
                                print("solved")
                                print(state.show())
                                return
                            else:
                                miss+=1
                                print("instances:", miss)

                                if valid_puzzle(2, state.board): #add to queue if valid
                                    q.put(deepcopy(state))


                        state.board[i][j] = None


'''
params: Takes the current puzzle as input
Return: The puzzle board corresponding to the goal
Note: You can modify the function definition as you see fit
'''
def dfs_with_prunning(puzzle):

    # Write Code here
    new_queue = queue.LifoQueue()
    miss = 0
    new_queue.put(puzzle)  # make new stack set solution to not found and

    while not new_queue.empty():

        testSudoku = new_queue.get()

        if test_goal(testSudoku.board, testSudoku):
            print("solved")
            print(testSudoku.show())
            return testSudoku

        miss += 1

        print("instances: ", miss)
        for i in range(4):
            for j in range(4):  # searches matrix of sudoku board to find none slots
                if testSudoku.board[i][j] is None:
                    for count in range(4):
                        temp = deepcopy(testSudoku)
                        temp.board[i][j] = count + 1
                        if valid_puzzle(2, temp.board):
                            new_queue.put(temp)


if __name__ == "__main__":

    
    puzzle=Sudoku(2,2).difficulty(0.2) # Constructs a 2 x 2 puzzle
    puzzle.show() # Pretty prints the puzzle


    print(valid_puzzle(2,puzzle.board)) # Checks if the puzzle is valid
    print(test_goal(puzzle.board,puzzle)) # Checks if the given puzzle board is the goal for the puzzle
    print(empty_cells(puzzle.board)) # Prints the empty cells as row and column values in a list for the current puzzle board

    # test algorithms
    #bfs(puzzle)
    #dfs(puzzle)
    #bfs_with_prunning(puzzle)
    dfs_with_prunning(puzzle)

    print("%s" % (time.time() - start_time))





