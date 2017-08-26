def imprime_retangulo(largura, altura, cheio):
    a = 1
    
    while a <= altura:
        l = 1

        while l <= largura:
            if cheio:
                print ("#", sep = "", end = "")
            else:
                if l != 1 and l != largura and a != 1 and a != altura:
                    print (" ", sep = "", end = "")
                else:
                    print ("#", sep = "", end = "")

            l += 1
        print("")
        a += 1

def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))

    imprime_retangulo(largura, altura, True)

main()
