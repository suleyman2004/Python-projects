import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
f1=(1+x)/np.sqrt(x)
plt.plot(x,f1,color="blue",linewidth=1,linestyle="dotted")
plt.show()
