def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    
    def search_direction(x, y, dx, dy):
        """This function is meant to help us search through all possibilities in the grid."""
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1), (1, 0), (1, 1), (-1, -1),  # Check all directions. right, up down left and all diagonals.
        (0, -1), (-1, 0), (-1, 1), (1, -1) 
    ]

    for x in range(rows):   # Loop through all the rows and columns
        for y in range(cols):
            if grid[x][y] == word[0]:   # If the letter matches first letter. Then we need to see if any direction has the word
                for dx, dy in directions:
                    if search_direction(x, y, dx, dy):
                        return (x, y), (x + (len(word) - 1) * dx, y + (len(word) - 1) * dy) # If we get a valid returned answer we will get the grid location

    return None  # If the word is not present. Might need to look at grid to see if we put it in right.


# Grid that we get
grid = [
    ['C', 'A', 'T', 'D'],
    ['B', 'G', 'O', 'G'],
    ['I', 'R', 'D', 'X'],
    ['N', 'A', 'T', 'S']
]

word = "CAT"
result = find_word(grid, word)

if result:
    print(f"Word '{word}' found from {result[0]} to {result[1]}")
else:
    print(f"Word '{word}' not found")
