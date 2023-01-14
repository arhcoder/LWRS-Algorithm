import matplotlib.pyplot as plt
from logrps import logrps

#* It counts and verifies the bias on the selections,
#* repeating the selection experiment a lot of times:
times = int(input("\nRepetitions: "))

#? Example list of 10 elements;
#* The algorithm has to recieve this list and select randomly one element;
#* By repeating the selection a lot of times, the result has to be that the
#* first element "E1" is the most frecuent selected, and then "E2", etc.
#! IF YOU  WANT TO MAKE SOME EXPERIMENTS WITH AN OWN IDEA OF SELECTION LIST
#! YOU JUST HAVE TO PUT INTO THE LIST "elements" WHATEVER YOU WANT!
elements: list = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
counter = []
n = len(elements)

#? Fills a counter vector with 0's; it will contains the amount of times that
#? each element of the list was selected:
for i in range(0, n):
    counter.append(0)

#/ Does all the repetitions of the experiment using the logrps function to select
#/ something on the list; and counts the times that each element was selected.
for _ in range(0, times):
    selected = logrps(elements)
    index = elements.index(selected)
    counter[index] += 1

#? Prints the data from the counter:
print(f"Elements on list: {n}")
print("\nSelected times:")
for i in range(0, n):
    print(f"Element #{i+1} [{elements[i]}]: {counter[i]} times selected;")


# Draws the line in a graph:
plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True

# Points with:
# (element, amountOfSelections ):
# points: list = []
x_values: list = []
y_values: list = []

# Put all the points:
for i in range(0, n):
    # points.append([i+1, counter[i]])
    x_values.append(i+1)
    y_values.append(counter[i])

# Shows the graphic:
plt.title("LOGARITHMIC RANDOM PONDERATED SELECTOR")
plt.ylabel("Amount of selected times")
plt.xlabel("Number of element")
info = f"For {n} elements;\nWith {times} choices;"
plt.annotate(info,
xy=(0.96, 0.8), xytext=(0, 12),
xycoords=("axes fraction", "figure fraction"),
textcoords="offset points",
size=10, ha="right", va="top",
bbox=dict(boxstyle="square,pad=1.0", fc="white", ec="b", lw=2))

plt.plot(x_values, y_values, "bo", linestyle="-")
plt.savefig("logselection.png", dpi="figure")
plt.show()
print()