from goodPivot import goodPivot

def particiona(vetor, inicio, fim, pivo):
    i = inicio

    for j in range(inicio, fim+1):
        if vetor[j] < pivo:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1

    for j in range(inicio, fim+1):
        if vetor[j] == pivo:
            vetor[i], vetor[j] = vetor[j], vetor[i]

    return i


def quickSort(vetor, inicio=0, fim=None):
    if fim is None: fim = len(vetor)-1

    if inicio < fim:

        pivo = goodPivot(vetor[inicio:fim+1])
        posicao_pivo = particiona(vetor, inicio, fim, pivo)

        quickSort(vetor, inicio, posicao_pivo-1)
        quickSort(vetor, posicao_pivo+1, fim)
