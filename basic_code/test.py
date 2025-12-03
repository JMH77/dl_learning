import numpy as np
import matplotlib.pyplot as plt

print("test")
a = np.array([1,2,3])
print(a)

x = np.arange(1,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#绘制图形
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="sin")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos")
plt.legend()
plt.show()

