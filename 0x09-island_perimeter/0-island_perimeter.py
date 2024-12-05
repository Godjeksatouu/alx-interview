#!/usr/bin/python3
"""
0-island_perimeter
"""

#!/usr/bin/python3
"""

"""

def island_perimeter(grid):
    """
 
    """
    perimeter = 0  

    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:  
                
                perimeter += 4

                
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  

                
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2 
    return perimeter
