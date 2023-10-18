'''
Pseudocode

function find_max(arr)                     
    max = arr[0]
    for i = 1 to length(arr) - 1
        if arr[i] > max
            max = arr[i]
    return max
'''

def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

print(find_max([5, 2, 9, 1, 5, 6]))
print(find_max([1])) 
print(find_max([]))  

