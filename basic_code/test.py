import numpy as np
import matplotlib.pyplot as plt

print("test")
a = np.array([1,2,3])
print(a)

x = np.arange(1,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x**2)

#绘制图形
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, linestyle=":", label="cos(x)")
plt.plot(x, y3, linestyle="--", label="sin(x²)")
plt.title("sin&cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos")
plt.legend()
plt.show()



