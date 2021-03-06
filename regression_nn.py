# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:22:26 2020

@author: Saeed Ahmad
"""

import torch
import torch.nn as nn

# f = w * x

# f = 2 * x
X = torch.tensor([1,2,3,4], dtype = torch.float32)
Y = torch.tensor([2,4,6,8], dtype = torch.float32)

w = torch.tensor(0.0, dtype = torch.float32, requires_grad = True)

# model prediction

def forward(x):
    return w*x



print(f'Prediction before training: f(5) = {forward(5):.3f}')



#Training 
learning_rate = 0.01
n_iters = 100


loss = nn.MSELoss()
optimizer = torch.optim.SGD([w],lr=learning_rate)

for epoch in range(n_iters):
    #prediction = forward pass
    y_pred = forward(X)
    
    #loss
    l = loss(Y, y_pred)
    
    #gradients = backward pass
    l.backward()
    
    #updated weights
    optimizer.step()
        
    #reset the gradients to zero
    optimizer.zero_grad()
    
    
    if epoch%2 == 0:
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')
        
    
print(f'Prediction after training: f(5) = {forward(5):.3f}')