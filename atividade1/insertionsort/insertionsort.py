def insertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

filename=raw_input('Path do arquivo:')
file = open(filename, 'r')

r_insertion = [int(i) for i in file]

insertionSort(r_insertion)

for i in range(len(r_insertion)):
    resultado = open('r_insertion.txt', 'a')
    resultado.write(str(r_insertion[i])+ '\n') 
    resultado.close()
    
    



