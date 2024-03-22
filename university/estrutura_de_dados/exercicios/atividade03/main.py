def merge_sort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(vetor, inicio, meio)
        merge_sort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)


def merge(vetor, inicio, meio, fim):
    left = vetor[inicio:meio]
    right = vetor[meio:fim]
    topo_left, topo_right = 0, 0
    for k in range(inicio, fim):
        if topo_left >= len(left):
            vetor[k] = right[topo_right]
            topo_right += 1
        elif topo_right >= len(right):
            vetor[k] = left[topo_left]
            topo_left += 1
        elif left[topo_left] < right [topo_right]:
            vetor[k] = left[topo_left]
            topo_left += 1
        else:
            vetor[k] = right[topo_right]
            topo_right += 1

def pares_impares(arr):
    arrPar = list()
    arrImpar = list()
    
    # ordena o array
    merge_sort(arr)
    
    # divide em dois novos arrays um para Impares e outro para Pares
    for item in arr:
        arrPar.append(item) if item % 2 == 0 else arrImpar.append(item)
            
    # inverte o array ordenado dos Impares
    fim = len(arrImpar) -1
    for i in range(len(arrImpar)//2):
        arrImpar[i], arrImpar[fim] = arrImpar[fim], arrImpar[i]
        fim -= 1
        
    # junta o array dos Impares ao dos Pares
    arrPar.extend(arrImpar)
    
    return arrPar

def main():
    arr = list()
    n = int(input())

    for i in range(n):
        arr.append(int(input())) 
    
    sorted_arr = pares_impares(arr)
        
    for item in sorted_arr:
        print(item)

if __name__=='__main__':
    main()