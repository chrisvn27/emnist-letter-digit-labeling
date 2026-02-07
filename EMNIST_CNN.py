from torchvision.datasets import EMNIST

dataset= EMNIST('./', 'balanced',  train= True, download=True)

img = dataset[0][0]

print(img)