

def Questao10_Lista3(Lim_Superior, Lim_Inferior):

    if Lim_Superior>Lim_Inferior:

        maior, menor = Lim_Superior, Lim_Inferior

    else:

        menor, maior = Lim_Superior, Lim_Inferior

    for i in range(menor+1, maior):

        if i%2!=0:

            print i,
