def metodo_lagrange():
    import scipy
    import matplotlib.pyplot as plt
    import numpy as np
    ## Peso corporal[kg]
    #x=np.array([58,62,59,70,85])
    ## Recreo
    #y=np.array([10,15,17,25,34])

    x_aux = []
    y_aux = []
    n_1 = 0
    while(True):
        try:
            n_1 = int(input("Cantidad de n >> "))
            break
        except Exception as e:
            pass
    for _ in range(n_1):
        aux = float(input("x_{} >> ".format(_)))
        x_aux.append(aux)

    for _ in range(n_1):
        aux = float(input("y_{} >> ".format(_)))
        y_aux.append(aux)

    x = np.array(x_aux)
    y = np.array(y_aux)

    result = scipy.poly1d([0.0])
    for i in range (0,len(x)):
        temp_numerador= np.poly1d([1.0])
        denominador = 1.0
        for j in range(0,len(x)):
            if i !=j:
                temp_numerador *= scipy.poly1d([1.0,-x[j]])
                denominador *= x[i]-x[j]
        result +=(temp_numerador/denominador) *y[i]

    print("el resultado es ")
    print(result)
    print("")
    n= float(input("digite un numero"))
    print("el paso", n,"evaluado es", result(n))

    x_val = np.linspace(min(x),max(x)+1,0,1)
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.grid(True)

    for i in range (0, len(x)):
        plt.plot([x[i]],[y[i]],'ro')
    plt.plot(x_val, result(x_val))
    plt.axis([min(x)-1, max(x)+1,min(y)-1, max(y)+1])
    plt.show()
#metodo_lagrange()
