from utils.data_structure import PriorityQueue
from collections import defaultdict

"""
Notes : 
- Diagonal are unique by i - j
Algorithm :
1. Use hash map to store sorted array of diagonal
2. Iterate over matrix and add value to sorted (ascending or descending) array in hash map 
3. Iterate over matrix and override value according to last element of array  
"""
def sortMatrix(grid) :
    hashMap = {

    }

    for row in range(len(grid)) : 
        
        for col in range(len(grid[row])) : 
            if (hashMap.get(row - col, None)) :
                hashMap[row - col].add(grid[row][col])
            else :
                queue = PriorityQueue()
                queue.add(grid[row][col])
                hashMap[row - col] = queue
        
    for row in range(len(grid)) : 
        for col in range(len(grid[row])) :  
            hashMap[row - col].print()

            if(row - col < 0) :
                grid[row][col] = hashMap[row - col].dequeue_first_element()
            else : 
                grid[row][col] = hashMap[row - col].dequeue()
        
    return grid


def diagonalSort(mat) :
    hash_map = defaultdict(list)
    length = len(mat)

    for i in range(length) :
        for j in range(len(mat[i])) :
            hash_map[i - j].append(mat[i][j])
    

    for value in hash_map.values() :
        value.sort(reverse=True)

    for i in range(length) :
        for j in range(len(mat[i])) :
            mat[i][j] = hash_map[i - j].pop()
    
    return mat
