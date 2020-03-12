import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("input.csv")


y_pos = np.arange(len(data['Column3']))
plt.bar(y_pos, data['Column3'], align='center', alpha=0.5)
plt.xticks(y_pos, data['Column1'])
plt.ylabel('Performance')
plt.title('Title')
plt.show()