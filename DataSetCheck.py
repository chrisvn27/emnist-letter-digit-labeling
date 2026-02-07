import matplotlib.pyplot  as plt
import numpy as np
from torchvision.datasets  import EMNIST

traindataset = EMNIST('./', 'balanced', train=True, download=True)
testdataset = EMNIST('./', 'balanced', train=False, download=True)

print("Len of train dataset",  len(traindataset))
print("Len of test dataset",  len(testdataset))

fig, axs = plt.subplots(1, 5, figsize=(10,2))

for i in range(5):
    img, label  = traindataset[i]
    img = np.array(img).T
    axs[i].imshow(img, cmap='gray')
    axs[i].set_title(f'label no. :{str(label)}, character: {traindataset.classes[label]}')
    axs[i].axis('off')

plt.tight_layout()
plt.show()


