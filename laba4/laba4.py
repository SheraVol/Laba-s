import os.path
import numpy as np
import matplotlib.pyplot as plt
def main():
    with open('Func/Chisla.conf', 'r') as f:
        k = f.read()
        k = str(k)
        k = k.split(' ')
        print("Данные нам числа - ", list(map(int,k)))
        a=int(k[0])
        b=int(k[1])
        x=np.linspace(-a,a,b)
        y=np.sin(2*x*np.pi)
        print(y)
        plt.plot(x,y)
        plt.show()
        plt.savefig('Func/laba44.svg')


file_path = r'Func/Chisla.conf'
flag = os.path.isfile(file_path)

if flag:
    main()
else:

    print("Файл не найден")
    a,b=input().split(' ')
    k1 = a + ' ' + b
    print(k1)
    with open('Func/Chisla.conf','w')as f1:
        f1.write(str(k1))
        f1.close()
        main()
