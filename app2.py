import random

palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():

    palavra = random.choice(palavras)

    letras_corretas = ['_'] * len(palavra)

    letras_erradas = []

    tentativas = 6 

    print("Bem-vindo ao jogo da forca!")
    print("Voce tem 6 tentativas para adivinhar a palavra.")

    while tentativas > 0 and '_' in letras_corretas:

        print(' '. join(letras_corretas))

        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_corretas[1] = letra

        else:

            letras_erradas.append(letra)

            tentativas -= 1 
            print(f"Tentativas restantes: {tentativas}")
            print(f"Letras erradas: {', '.join(letras_erradas)}")

    if '_' not in letras_corretas:
        print("Parabéns! Voce ganhou!")
    else:
        print(f"voce perdeu! a palavra era {palavra}.")

    jogo_da_forca()   
