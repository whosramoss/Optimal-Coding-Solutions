'''
Scatter plot linked dashed  with parameterization of colors and highlights.
'''
import matplotlib.pyplot as plt

axisX1 = [1,3,5,7,9]
axisY1 = [2,3,7,1,0]

plt.title("Linked scatterplot")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(axisX1,axisY1, label="Production", color="r")
plt.plot(axisX1,axisY1, linestyle="--")
plt.legend()
plt.show()
