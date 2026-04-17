import random

def get_conflicts(state, area_map):
    """
    Calculates the number of constraint violations for a given state.
    state: list of 8 integers where state[c] = r (Queen at column c, row r)
    """
    conflicts = 0
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):
            # 1. Row Constraint
            if state[i] == state[j]:
                conflicts += 1
                
            # 2. Area/Color Constraint
            if area_map[state[i]][i] == area_map[state[j]][j]:
                conflicts += 1
                
            # 3. Diagonal Touching Constraint 
            # If they are in adjacent columns and adjacent rows
            if abs(i - j) == 1 and abs(state[i] - state[j]) == 1:
                conflicts += 1
            
    return conflicts

def solve_queens_local_search(area_map, max_restarts=1000):
    n = 8
    
    for restart in range(max_restarts):
        # Generate a random initial state (1 queen per column)
        state = [random.randint(0, n - 1) for _ in range(n)]
        
        while True:
            current_conflicts = get_conflicts(state, area_map)
            
            # Goal state found!
            if current_conflicts == 0:
                print(f"Solution found after {restart} restarts!")
                return state
                
            # Generate all possible neighbor states (move 1 queen in its column)
            best_state = state.copy()
            best_conflicts = current_conflicts
            
            for col in range(n):
                for row in range(n):
                    if state[col] != row:
                        # Try moving queen in 'col' to 'row'
                        neighbor = state.copy()
                        neighbor[col] = row
                        neighbor_conflicts = get_conflicts(neighbor, area_map)
                        
                        if neighbor_conflicts < best_conflicts:
                            best_state = neighbor
                            best_conflicts = neighbor_conflicts
            
            # If no neighbor improves the score, we are stuck in a local minimum
            if best_conflicts >= current_conflicts:
                break # Break inner loop to trigger a random restart
                
            # Move to the better state
            state = best_state
            
    return None # Failed to find a solution within max_restarts

def print_board(state, area_map):
    n = len(state)
    for r in range(n):
        row_str = ""
        for c in range(n):
            if state[c] == r:
                row_str += "[Q]"
            else:
                row_str += f" {area_map[r][c]} "
        print(row_str)

if __name__ == "__main__":
    # Example 8x8 Area Map (0-7 represent the 8 different colors/regions)
    # Give each area a unique integer from 0 to 7
    example_area_map = [
        [0, 0, 0, 0, 1, 1, 2, 2],
        [0, 3, 3, 0, 1, 1, 2, 2],
        [0, 3, 3, 0, 4, 4, 4, 2],
        [0, 3, 3, 4, 4, 5, 4, 2],
        [6, 6, 3, 4, 5, 5, 5, 2],
        [6, 6, 6, 4, 4, 5, 7, 7],
        [6, 6, 6, 6, 5, 5, 5, 7],
        [6, 6, 6, 6, 6, 7, 7, 7]
    ]

    print("Searching for solution...")
    solution = solve_queens_local_search(example_area_map)
    
    if solution:
        print("\nFinal Board (Q = Queen, numbers = region):")
        print_board(solution, example_area_map)
    else:
        print("No solution found. Try increasing max_restarts.")
