import matplotlib.pyplot as plt

# def plot_and_save(x, y, filepath):
#     xa = [float(word) for word in x.split()]
#     ya = [float(word) for word in y.split()]

#     fig, ax = plt.subplots()
#     ax.plot(xa, ya)
#     plt.savefig(filepath, format="png")
#     plt.close()  # Close the plot to release resources

#     return filepath

# # Example usage:
# x_data = "1 2 3 4 5"
# y_data = "2 4 6 8 10"
# file_path = ".github/scripts/plot.png"
# plot_and_save(x_data, y_data, file_path)

x_data = "1 2 3 4 5"
y_data = "2 4 6 8 10"

xa = [float(word) for word in x_data.split()]
ya = [float(word) for word in y_data.split()]

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.savefig(".github/scripts/plot.png", format="png")
plt.close()
