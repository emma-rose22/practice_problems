'''
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
'''

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
                #make a dictionary for each street
        #values are all the valid connecting streets
        
        #loop through the list and if all have a valid dict entry, it passes
        #else, false
        
        paths = {
            1 : [1, 3, 5],
            2 : [5, 6, 3, 4],
            3 : [1, 4, 6, 2, 5],
            4 : [1, 3, 5, 6, 2],
            5 : [1, 2, 3, 4, 6],
            6 : [1, 2, 3, 4, 5]
        }
        
        
        #if there are two lists, they need to be stacked on top of each other
        #to see if it passes 
        if len(grid) == 2:
            c1 = 0
            c2 = 0
            for pair in range(len(grid) - 1):
                c1_values = paths[grid[0][c1]]
                if grid[1][c2] in c1_values:
                    c1 += 1
                    c2 += 2
                else:
                    return False
            return True
        
        #else we just go through one by one
        else:
            counter = 0
            for lists in grid:
                for street in lists:
                    current_values = paths[street]
                    try:
                        if grid[counter + 1] not in current_values:
                            return False
                    except:
                        if grid[counter] not in current_values:
                            return False
                    counter += 1
            return True