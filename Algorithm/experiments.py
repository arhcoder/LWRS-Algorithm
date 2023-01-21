import matplotlib.pyplot as plt
from logrps import logrps

#* It counts and verifies the bias on the selections,
#* repeating the selection experiment a lot of times:
times = int(input("\nRepetitions: "))

#? Example list of 10 objects;
#* The algorithm has to recieve this list and select randomly one object;
#* By repeating the selection a lot of times, the result has to be that the
#* first object "Obj1" is the most frecuent selected, and then "Obj2", etc.
#! IF YOU  WANT TO MAKE SOME EXPERIMENTS WITH AN OWN IDEA OF SELECTION LIST
#! YOU JUST HAVE TO PUT INTO THE LIST "objects" WHATEVER YOU WANT!
objects: list = ["Obj1", "Obj2", "Obj3", "Obj4", "Obj5", "Obj6", "Obj7", "Obj8", "Obj9", "Obj10"]
counter = []
n = len(objects)

#? Fills a counter vector with 0's; it will contains the amount of times that
#? each object of the list was selected:
for i in range(0, n):
    counter.append(0)

#/ Does all the repetitions of the experiment using the logrps function to select
#/ something on the list; and counts the times that each object was selected:
for _ in range(0, times):
    selected = logrps(objects)
    index = objects.index(selected)
    counter[index] += 1

#? Prints the data from the counter:
print(f"Objects on list: {n}")
print("\nSelected times:")
for i in range(0, n):
    print(f"Object #{i+1} [{objects[i]}]: {counter[i]} times selected;")


# Draws the line in a graph:
plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True

# Points with:
# (object, amountOfSelections ):
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
plt.xlabel("Number of object")
info = f"For {n} objects;\nWith {times} choices;"
plt.annotate(info,
xy=(0.96, 0.8), xytext=(0, 12),
xycoords=("axes fraction", "figure fraction"),
textcoords="offset points",
size=10, ha="right", va="top",
bbox=dict(boxstyle="square,pad=1.0", fc="white", ec="#8B0880", lw=2))

plt.plot(x_values, y_values, "o", c="#8B0880", mfc="#8B0880", linestyle="-")
plt.savefig("logselection.png", dpi="figure")
plt.show()
print()