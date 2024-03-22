def bubble_sort(lista):
    tamanho = len(lista)
    for j in range(tamanho-1):
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]


def main():
    vetor = ["casa", "bola", "arvore", "dado", "janela", "cortina"]

    bubble_sort(vetor)

    print("Vetor ordenado: ")
    print(vetor)


if __name__=='__main__':
    main()
