def selectionSort(A):
    for i in range(len(A)):
        minimo = i
        for j in range(i+1, len(A)):
            if A[minimo] > A[j]:
                minimo = j

        A[i], A[minimo] = A[minimo], A[i]

filename=raw_input('Path do arquivo:')
file = open(filename, 'r')

r_selection = [int(i) for i in file]

selectionSort(r_selection)

for i in range(len(r_selection)):
    resultado = open('r_selection.txt', 'a')
    resultado.write(str(r_selection[i])+ '\n') 
    resultado.close()
    
