

def Questao21_Lista3(N):

    S = 0

    for i in range(1, 100):

        if i % 2 != 0:

            S += (i /(float(i/2)+1))            

    print "%.2f" % S
