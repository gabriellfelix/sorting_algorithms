import math
from insertionSort import insertionSort

def goodPivot(vetor):
    copia_vetor = vetor.copy()

    while(len(copia_vetor) > 1):

        medianas = []
        quant_subvetores = math.ceil(len(copia_vetor)/5)

        for i in range(quant_subvetores):

            subvetor = copia_vetor[i*5:i*5+5]
            insertionSort(subvetor)
            
            mediana = subvetor[math.ceil((len(subvetor))/2) - 1]
            medianas.append(mediana)

        copia_vetor = medianas

    return medianas[0]