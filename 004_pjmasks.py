"""
loops Example

author: Anirudh Panth
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


Catboy = 18
Gecko = 19
Owlete = Catboy + Gecko
print (Owlete)



Catboy = 18
Gecko = 20
Owlete = Gecko + (Gecko  - Catboy) 
print (Owlete)


plt.plot([1, 2, 3], [Catboy, Gecko, Owlete], 'yo')
plt.show()
