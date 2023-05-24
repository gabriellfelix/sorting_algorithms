def insertionSort(vetor):
    for i in range(len(vetor)):
        j = i

        while(j > 0 and vetor[j] < vetor[j-1]):
            vetor[j], vetor[j-1] = vetor[j-1], vetor[j]
            j -= 1