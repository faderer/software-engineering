import torch
import numpy as np
import torch.nn.functional as F
from torch.autograd import Variable



np_data = np.arange(9).reshape((3, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()


print(
    '\nnp_data', np_data,
    '\ntorch_data', torch_data,
    '\ntensor2array', tensor2array
)

np_data = [[1, 2], [3, 4]]
torch_data = torch.tensor(np_data)

print(
    '\nnp_data', np.matmul(np_data, np_data),
    '\ntorch_data', torch.mm(torch_data, torch_data)
)