'''
# INSERTION SORT

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i -1
        while A[j] > A[j+1] and j >=0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
            print(A)

def optimized_insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            #print(A[i], k, curNum)
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                break
        A[k+1] = curNum
        #print(A)
            


A = [8, 4, 9, 2, 6, 1]

insertion_sort(A)

print("optimized: ")

A = [8, 4, 9, 2, 6, 1]
optimized_insertion_sort(A)
'''



'''********************
#SELECTION SORT


def selection_sort(A):
    for i in range(0, len(A)-1):
        lowId = i
        for j in range(i+1, len(A)):
            if A[j] < A[lowId]:
                lowId = j
        if lowId != i:
            A[i], A[lowId] = A[lowId], A[i]
   



A = [8, 4, 9, 2, 6, 1]

selection_sort(A)
print(A)

********************'''


def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                print(A)
    return A



A = [8, 4, 9, 2, 6, 1]

print(bubble_sort(A))






























    













