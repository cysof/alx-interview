#!/usr/bin/python3
""" island_perimeter module that return the perimeter of an island

"""



def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a given grid.

    Parameters:
        grid (List[List[int]]): A 2D matrix representing the grid, where 1s represent land and 0s represent water.

    Returns:
        int: The perimeter of the island.

    The function first defines an inner function called `edges` that calculates the number of edges in a given matrix. It iterates over each row in the matrix and counts the number of times the value of a cell is different from the value of its adjacent cell. The count is then returned.

    The function then transposes the input grid by creating a new grid called `tggrid`, where the rows and columns are swapped. This is done by iterating over each row in the input grid and appending the corresponding elements to the appropriate row in `tggrid`.

    Finally, the function calls the `edges` function twice: once on the input grid and once on the transposed grid. The results are added together and returned as the perimeter of the island.

    Note: The grid is assumed to be a square matrix, and the edges are counted only between adjacent land cells. Water cells are not counted as part of the perimeter.
    """
    def edges(matrix):
        """
        Calculates the number of edges in a given matrix.

        Parameters:
            matrix (List[List[int]]): A 2D matrix representing the grid, where 1s represent land and 0s represent water.

        Returns:
            int: The number of edges in the matrix.

        This function iterates over each row in the matrix and counts the number of times the value of a cell is different from the value of its adjacent cell. The count is then returned as the number of edges.

        Note: The matrix is assumed to be a square matrix, and the edges are counted only between adjacent land cells. Water cells are not counted as part of the edges.
        """


        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i-1]
        return count

    tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            tgrid[i].append(item)

    return edges(grid) + edges(tgrid)