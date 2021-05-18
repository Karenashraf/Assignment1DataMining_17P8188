import numpy as np

def randomization(n):
  A = np.random.random([n,1])
  return A


    
  raise NotImplementedError

def operations(h, w):
  A = np.random.random([h,w])
  B = np.random.random([h,w])
  s = A + B
  return A,B,s


    
  raise NotImplementedError


def norm(A, B):


  s = np.linalg.norm(A + B)
  return s
    
  raise NotImplementedError


def neural_network(inputs, weights):
    z= np.tanh(weights.T.dot(inputs))
    
    raise NotImplementedError

def scalar_function(x, y):
    if x<=y:
       return (np.dot(x,y))
    else:
       return(x/y)
    
    raise NotImplementedError

def vector_function(x, y):

    out = np.vectorize(scalar_function)
    return out
    
    raise NotImplementedError

