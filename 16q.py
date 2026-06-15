import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

w1 = np.random.randn(2, 4)
w2 = np.random.randn(4, 1)

for _ in range(10000):
    layer1 = sigmoid(np.dot(X, w1))
    output = sigmoid(np.dot(layer1, w2))
    
    error = y - output
    d_w2 = np.dot(layer1.T, error * (output * (1 - output)))
    d_w1 = np.dot(X.T, np.dot(error * (output * (1 - output)), w2.T) * (layer1 * (1 - layer1)))
    
    w2 += d_w2
    w1 += d_w1

print("Outputs:\n", output)
