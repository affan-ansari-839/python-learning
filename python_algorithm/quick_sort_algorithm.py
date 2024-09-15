# -*- coding: utf-8 -*-
import random

def partition(A, p, r):
    # Set the pivot element to be the first element in the range
    x = A[p]
    q = p

    # Iterate from the element after the pivot to the end of the range
    for s in range(p + 1, r + 1):
        print("s and x", A[s], x, f"---------> s={s}, q={q}" )
        if A[s] < x:
            q += 1
            # Swap A[q] with A[s]
            print("Before SWAP ---- s={s}, q={q}", (A[s], A[q]))
            swap(A, q, s)
            print("After SWAP new A---->", A)
            

    # Finally, swap the pivot element with the element at index q
    print("After loop Swap ------>")
    swap(A, p, q)

    # Return the index of the pivot element after partitioning
    return q

def swap(A, q, s):
    # Swaps elements at indices q and s in the array
    print(A[s], A[q], " SWap to ---->", A[q], A[s], A)
    A[q], A[s] = A[s], A[q]

def quick_sort(A, p, r):
    if p < r:
        # Select a random index from the range [p..r] as the pivot
        
        i = random.randint(p, r)
        print("pivot point ----->", A[i])

        # Swap the randomly chosen pivot with the first element
        swap(A, i, p)

        # Partition the array and get the pivot position
        q = partition(A, p, r)

        # Recursively sort the elements before and after the partition
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

# Example usage
arr = [7,6,12,3]
print("Original array:", arr)

A = arr
    
quick_sort(A, 0, len(arr) - 1)

print("Sorted array:", A)
    


