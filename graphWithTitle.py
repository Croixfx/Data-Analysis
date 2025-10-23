import matplotlib.pyplot as plt
X = range(1,50)
Y = [value*3 for value in X]
print("Values of X: ")
print(range(1,50))
print("Values of Y(Thrice of x): ")
print(Y)
plt.plot(X,Y)
plt.xlabel("X - Axis")
plt.ylabel("Y - axis")
plt.title("Draw a line")
plt.show()