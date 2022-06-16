import numpy as np 
import matplotlib.pyplot as plt



def f1(number_of_samples):
    return np.random.normal(0,1, (number_of_samples, 5)) #returning noise?

def f2(x1,x4,x5):
    return ((-2 * x1) + (3 * x4) + (5 * x5))

def f3(x1):
    return (2 * x1)

def f4(x3):
    return (-x3)

def f5(x3, alpha):
    return (alpha * x3)


def sample(n: int, alpha: float) -> np.ndarray: 
    
    x1 = f1(n)
    x3 = f3(x1)
    x4 = f4(x3)
    x5 = f5(x3, alpha)
    x2 = f2(x1, x4, x5)

    return x2



if __name__ == '__main__':
    arr = sample(200, 2)
    plt.plot(arr, 'o')
    plt.show()

    #print(arr)