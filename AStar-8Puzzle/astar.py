import heapq
from typing import List, Tuple

class PuzzleNode:
    def __init__(self, state: List[List[int]], parent=None, move=0, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan_distance(state: List[List[int]]) -> int:
    goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_position = [(ix, row.index(state[i][j])) for ix, row in enumerate(goal_state) if state[i][j] in row][0]
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance

def generate_neighbors(node: PuzzleNode) -> List[List[List[int]]]:
    neighbors = []
    zero_position = [(ix, row.index(0)) for ix, row in enumerate(node.state) if 0 in row][0]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_row = zero_position[0] + move[0]
        new_col = zero_position[1] + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in node.state]
            new_state[zero_position[0]][zero_position[1]] = node.state[new_row][new_col]
            new_state[new_row][new_col] = 0
            neighbors.append(new_state)
    return neighbors

def solve_8_puzzle(initial_state: List[List[int]], goal_state) -> List[Tuple[int, List[List[int]]]]:
    initial_node = PuzzleNode(state=initial_state)

    priority_queue = [initial_node]
    visited_states = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        zero_position = [(ix, row.index(0)) for ix, row in enumerate(current_node.state) if 0 in row][0]

        if current_node.state == goal_state:
            solution_path = []
            while current_node.parent:
                solution_path.append((current_node.move, current_node.state, current_node.cost, current_node.heuristic))
                current_node = current_node.parent
            solution_path.reverse()
            return solution_path

        visited_states.add(tuple(map(tuple, map(tuple, current_node.state))))

        neighbors = generate_neighbors(current_node)
        for neighbor_state in neighbors:
            if tuple(map(tuple, map(tuple, neighbor_state))) not in visited_states:
                neighbor_node = PuzzleNode(
                    state=neighbor_state,
                    parent=current_node,
                    move=current_node.state[zero_position[0]][zero_position[1]],
                    cost=current_node.cost + 1,
                    heuristic=manhattan_distance(neighbor_state),
                )
                heapq.heappush(priority_queue, neighbor_node)

    return []

def print_solution(initial_state: List[List[int]], solution: List[Tuple[int, List[List[int]], int, int]]):
    print("Initial State:")
    for row in initial_state:
        print(" ".join(map(str, row)))
    print()

    if solution:
        for step, state, cost, heuristic in solution:
            print(f"Cost: {cost}, Heuristic: {heuristic}, Total Cost (f): {cost + heuristic}:\n")
            for row in state:
                print(" ".join(map(str, row)))
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    initial_state = [[1, 3, 2], [6, 4, 5], [8, 0, 7]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solution = solve_8_puzzle(initial_state, goal_state)
    print_solution(initial_state, solution)
