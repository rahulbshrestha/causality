import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def dependence(x: np.ndarray, y: np.ndarray) -> float:
    """ Return a measure of dependence between x and y
        
        Higher return value means higher depenence.
        Ideally, a return value of zero means x and y are independent.

    """



    reg = LinearRegression().fit(x , y)
    print(reg.score(x, y))

    # Phase 1: Determine causal order


    # Phase 2: Remove superflous edges



def visualise(X, Y):
    plt.plot(X, Y, 'o')
    plt.show()

if __name__ == '__main__':

    X = np.random.uniform(0, 1, (150,))
    Y = X ** 2 + np.random.uniform(0, 1, (150,))
    
    dependence(X, Y)
    #visualise(X, Y)

    #test_stat, p = hsic_test_gamma(X, Y)
    #print(f'test_stat: {test_stat}, p: {p}')
