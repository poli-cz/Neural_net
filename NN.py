import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    def __init__(self):         # only structure of network
        super().__init__()      # important for some reason # whatever...
        self.fc1 = nn.Linear(600, 1000) # activating function run on right side
        self.fc2 = nn.Linear(1000, 800)
        self.fc3 = nn.Linear(800, 600)
        self.fc4 = nn.Linear(600, 400)
        self.fc5 = nn.Linear(400, 3)    # We dont want to run sigmoid here... obviously

    def forward(self, x):
        x = F.relu(self.fc1(x))         # F.relu is activation f(x) Sigmoid and stuff around...

        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return F.log_softmax(x, dim=1)


net= Net()
print(net)

x=torch.rand((600,1))
x=x.view(-1, 600*1)     # we need to flatend array

output=net(x)
print(output)
