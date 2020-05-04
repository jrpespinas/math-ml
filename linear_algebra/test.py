import matrix_methods as mm


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while key < A[j] and j >= 0:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    print(A)

def main():
    insertion_sort([8,3,5,7,24,56,4,32,21])
    
if __name__ == '__main__':
    main()