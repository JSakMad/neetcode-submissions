class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use a hashset to store elements as the cols and rows are looped through, if an entry already in the set is seen, invalid board

        # To check the validity of the sqaures, use a seperate map

        rowset = defaultdict(set)
        colset = defaultdict(set)
        squareset = defaultdict(set)

        for row in range(9):
            for col in range(9):
                element = board[row][col]

                if element == ".":
                    continue

                # Check if the element is already in the set of rows, cols, or squares
                if (element in rowset[row] 
                    or element in colset[col] 
                    or element in squareset[(row // 3, col // 3)]):
                    return False
                
                colset[col].add(element)
                rowset[row].add(element)
                squareset[(row // 3, col // 3)].add(element)

        return True