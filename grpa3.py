def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    for i in range(len(row)):
        if row[i] == elem:
            return i
    return -1

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    
    reversed_row = row[::-1]
    
    # Find first occurrence in reversed list
    first_in_reversed = index_of_first_occurance(reversed_row, elem)  # Fixed function call
    
    if first_in_reversed == -1:
        return -1
    
    # Convert index from reversed list to original list
    return len(row) - 1 - first_in_reversed

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    if x < 0 or y < 0:
        return False
    if x >= len(M) or y >= len(M[0]):
        return False
    return True

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    # return {
    #   (x1,y1)
    #   for x1,y1 in ... # all the possible adjacent coordinates
    #   if is_valid_coordinate(x1,y1, M)
    # }
    result = set()
    for (x1,y1) in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        if is_valid_coordinate(x1,y1, M):
            result.add((x1,y1))
    return result
    

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    x, y = curr_coords
    adjacent_coords = valid_adjacent_coordinates(x, y, M)
    
    if prev_coords:
        adjacent_coords.discard(prev_coords)
    
    for coord in adjacent_coords:
        nx, ny = coord
        if M[nx][ny] == value:
            return (nx, ny)
    
    return None

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    # x_start, x_end = len(M)-1,0
    # y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)
    # ...
     # Find starting position (last row with 1)
    x_start, x_end = len(M)-1, 0
    y_start = index_of_last_occurance(M[-1], 1)
    
    # If no 1 in the last row, return empty path
    if y_start == -1:
        return []
    
    # Start path with the first coordinate
    path = [(x_start, y_start)]
    current = (x_start, y_start)
    previous = None
    
    while current[0] > 0:  # Until we reach the first row
        next_coord = next_coordinate_with_value(current, 1, M, previous)
        if next_coord is None:
            # No valid path found
            break
        
        path.append(next_coord)
        previous = current
        current = next_coord
    
    return path
    
def print_path(M):
    path = get_path_coordinates(M)
    return path

def alternate_path(M):
    path = get_path_coordinates(M)
    
    # Make a deep copy of the matrix to modify
    result_matrix = [row[:] for row in M]
    
    # Flip every alternate 1 (starting from the second)
    for i, (x, y) in enumerate(path):
        if (i + 1) % 2 == 0:  # Change 1 to 2 at every second position
            result_matrix[x][y] = 2
    
    return result_matrix

def count_path(M):
    path = get_path_coordinates(M)
    result_matrix = [row[:] for row in M]
    
    # Replace the value with step count
    for i, (x, y) in enumerate(path):
        result_matrix[x][y] = i + 1
    
    return result_matrix

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    original_path = get_path_coordinates(M)
    
    # Make a deep copy of the matrix to modify
    result_matrix = [row[:] for row in M]
    
    # Get the width of the matrix
    width = len(M[0])
    
    # Add the mirrored path
    for x, y in original_path:
        mirrored_y = width - 1 - y
        result_matrix[x][mirrored_y] = 1
    
    return result_matrix

def mirror_vertically(M):
    path = get_path_coordinates(M)
    original_path = get_path_coordinates(M)
    
    # Make a deep copy of the matrix to modify
    result_matrix = [row[:] for row in M]
    
    # Get the height of the matrix
    height = len(M)
    
    # Add the mirrored path
    for x, y in original_path:
        mirrored_x = height - 1 - x
        result_matrix[mirrored_x][y] = 1
    
    return result_matrix
