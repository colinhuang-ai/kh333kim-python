# line 1: import lib
import matplotlib.pyplot as plt

# init array
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [120, 145, 138, 170, 190]

# line 2: set figure size
plt.figure(figsize=(8, 5))
plt.plot(days, visitors, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# draw
plt.title("Library Visitors by Day")
plt.xlabel("Day")
plt.ylabel("Visitors")

plt.tight_layout()
plt.show()

# support non-ui
plt.savefig("library_visitors.png")