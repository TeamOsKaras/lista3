

#Essa e a lista 3.


def Questao01_Lista3(N):

    for i in range(1, N+1):

        print N
        

def Questao02_Lista3(N):

    for i in range(1, N+1):
        if i%2==0:
            print N




def Questao03_Lista3(A0, Limite, R):

    while Limite > A0 ** R:

        print A0 ** R
        R += 1
        



def Questao04_Lista3(A0, Limite, R):

    while Limite > A0 ** R:

        print A0 ** R
        R += 1





def Questao05_Lista3(Numero):

    total = 1
    for i in range(1, Numero+1):

        total *= i
    if total != 0:
        print "O fatorial de %d e igual a %d" % (Numero, total)



def Questao06_Lista3(Numero):

    total = 0
    
    for i in range(1, 11):

        total += i

    print "A soma dos numeros de 1 a 10 na tabuada e igual a %d. " % total



def Questao07_Lista3(Numero):

    total = 0
    
    for i in range(2, Numero):

        total += i

    print "O total da soma de todos os elementos inteiros entre 1 e %d foi igual a %d." % (Numero, total)



def Questao08_Lista3(N, Lim_Superior, Lim_Inferior):

    if Lim_Superior>Lim_Inferior:

        maior, menor = Lim_Superior, Lim_Inferior

    else:

        menor, maior = Lim_Superior, Lim_Inferior

    for i in range(menor+1, maior):

        if N%i == 0:

            print i,



def Questao09_Lista3(Lim_Superior, Lim_Inferior):

    if Lim_Superior>Lim_Inferior:

        maior, menor = Lim_Superior, Lim_Inferior

    else:

        menor, maior = Lim_Superior, Lim_Inferior

    for i in range(menor+1, maior):

        if i%2==0:

            print i,
    


            
def Questao10_Lista3(Lim_Superior, Lim_Inferior):

    if Lim_Superior>Lim_Inferior:

        maior, menor = Lim_Superior, Lim_Inferior

    else:

        menor, maior = Lim_Superior, Lim_Inferior

    for i in range(menor+1, maior):

        if i%2!=0:

            print i,



def Questao11_Lista3(Lim_Superior, Lim_Inferior):
    
    cont = 0
    
    if num%i==0:

        cont += 1
        
        if cont==2:

            print i#



def Questao12_Lista3(N, Lista_N = 0):

    soma = 0
    cont = 0
    while cont<N:

        valor = input("Digite o valor:\n ")
        soma += valor
        cont += 1
    
    print "A soma e %d, e a media foi igual a %.2f." % (soma, soma/float(N))

 
    


def Questao13_Lista3(N, Lista_N):

    
    if N == len(Lista_N):

        print "O maior elemento da lista foi igual a %d." % max(Lista_N)





def Questao14_Lista3(N):

    variavel = 0

    while variavel**2 <= N:

        variavel += 1
        if variavel**2 > N:
            
            print "O maior valor quadrado menor que %d e %d, que e o quadrado de %d." % (N, (variavel-1)**2, (variavel-1))

    


def Questao15_Lista3(N_termos):

     acrescimo = 0
     num = 1
     cont = 0

     while True:
         
         numero = num+acrescimo
         print numero
         numero += 1
         cont += 1
         acrescimo += 2
         
         
         if cont == N_termos:
             print "Fim!"
             break
         
         


def Questao16_Lista3(Numero):

    a = 0; b = 1
    cont = 0
    
    while cont<Numero:

        print a,
        a = b
        b += a
        cont += 1#



def Questao17_Lista3(N):

    S = 0

    for i in range(1, N+1):

        S += 1.0 / i
        print "1.0 / %d + " % i,

    print "%.2f" % S





def Questao18_Lista3(N):

    S = 0
    O = 0  

    for i in range(1, N+1):

        
        S += float(i) / (N-O)
        O += 1

    print "%.2f" % S




def Questao19_Lista3(N):

    S = 0
    cont = 0
    cont2 = 1

    for i in range(1, N+1):

        if i % 2 != 0:

            S += i /(float(N) - cont)
            print "%d / (%d - %d) -" % (i, N, cont)
            cont += 2

        else:

            S -= (N-cont2)/float(i)
            print "(%d - %d) / %d +" % (N, cont2, i)
            cont2 += 1
            

    print "%.2f" % S




    
def Questao20_Lista3(N):

    S = 0

    for i in range(1, N+1):

        if i % 2 != 0:

            S += 1.0 / i

        else:

            S -= 1.0 / i

    print "%.2f" % S
    

    
def Questao21_Lista3(N):

    S = 0

    for i in range(1, 100):

        if i % 2 != 0:

            S += (i /(float(i/2)+1))            

    print "%.2f" % S




def Questao22_Lista3(N_fichas):

    cont = 0
    regP = 0
    
    while N_fichas > 0:

        n_identificacao = input("Digite o numero de identificacao do boi:\n ")
        peso = input("Digite o peso do boi:\n ")

        if cont == 0:

            boi_gordo = peso
            boi_magro = peso
            

        if peso > boi_gordo:

            boi_gordo = peso
            regG = n_identificacao

        elif peso < boi_magro:

            boi_magro = peso
            regP = n_identificacao
        

        N_fichas -= 1
        cont += 1

    print " O boi mais pesado foi o de registro %d, cujo peso foi igual a %.2f." % (regG, boi_gordo)
    print " O boi mais leve foi o de registro %d, cujo peso foi igual a %.2f." % (regP, boi_magro)

Questao22_Lista3(3)



def Questao23_Lista3(codigo, numero_horas, numero_dependentes, N_funcionarios):

    salario = (numero_horas * 12) + (40 * numero_dependentes)
    salario_final = salario - ((salario * 8.5/100) + (salario * 5.0/100))
    print "Salario Bruto = %.2f" % salario
    print "Descontados %.2f de INSS e %.2f de IR." % (salario * 8.5/100, salario * 5.0/100)
    print "Salario liquido = %.2f." % salario_final
    salario_final = 0
    N_funcionarios -= 1

    while N_funcionarios>0:

        codigo = input("Diga o codigo:\n ")
        numero_horas = input("Diga a quantidade de horas trabalhadas:\n ")
        numero_dependentes = input("Diga o numero de dependentes:\n ")
        
        salario = (numero_horas * 12) + (40 * numero_dependentes)
        salario_final = salario - ((salario * 8.5/100) + (salario * 5.0/100))
        print "Salario Bruto = %.2f" % salario
        print "Descontados %.2f de INSS e %.2f de IR." % (salario * 8.5/100, salario * 5.0/100)
        print "Salario liquido = %.2f." % salario_final
        salario_final = 0
        N_funcionarios -= 1



def Questao24_Lista3(Salario, N_Filhos, N_habitantes):

    mediaSalario = 0
    MediaFilhos = 0
    Cont_Salario_Baixo = 0
    Cont_Total = 0

    Cont_Total += 1
    MediaSalario += Salario
    MediaFilhos += N_Filhos

    if Salario <= 1000:

        cont_Salario_Baixo += 1

    while N_habitantes > 0:

        Salario = input("Digite o salario do trabalhador:\n ")
        N_filhos = input("Digite o numero de filhos dele:\n ")
        
        Cont_Total += 1
        MediaSalario += Salario
        MediaFilhos += N_Filhos

        if Salario <= 1000:

            cont_Salario_Baixo += 1

    print "A media salarial foi igual a %.2f." % mediaSalario/float(Cont_Total)
    print "A media de filhos foi igual a %.2f." % MediaFilhos/float(Cont_Total)
    print "O percentual de pessoas com salario menor ou igual a 1000 foi igual a %.2f. %%" % cont_Salario_Baixo/float(Cont_Total)


def Questao25_Lista3(N_eleitores):

    Candidato_1, Candidato_2, Candidato_3, voto_nulo, voto_branco = 0, 0, 0, 0, 0

    while N_eleitores>0:

        voto = input("Digite seu voto:\n ")
        
        if voto == 1:

            Candidato_1 += 1

        if voto == 2:

            Candidato_2 += 1

        if voto == 3:

            Candidato_3 += 1

            
        if voto == 9:

            voto_nulo += 1

        if voto == 0:

            voto_branco += 1

        N_eleitores -= 1

    print "O candidato 1 recebeu %d votos." % Candidato_1
    print "O candidato 2 recebeu %d votos." % Candidato_2
    print "O candidato 3 recebeu %d votos." % Candidato_3
    print "O total de votos nulos foi igual a %d." % voto_nulo
    print "O total de votos brancos foi igual a %d." % voto_branco

    if Candidato_1 > Candidato_2 and Candidato_1 > Candidato_3:

        print "Candidato 1 venceu!"

    elif Candidato_2 > Candidato_1 and Candidato_2 > Candidato_3:

        print "Candidato 2 venceu!"

    elif Candidato_3 > Candidato_2 and Candidato_3 > Candidato_1:

        print "Candidato 3 venceu!"

































    
    























