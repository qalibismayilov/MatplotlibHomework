import matplotlib.pyplot as plt

print("Matplotlib isleyir")
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

temperature = [18, 20, 22, 21, 24, 26, 23]
plt.figure(figsize=(10, 5))

plt.plot(days, temperature, marker="o", linestyle="--")
plt.title("Heftelik Temperatur")
plt.xlabel("Gunler")
plt.ylabel("Temperatur (°C)")

plt.grid(True)
for i, temp in enumerate(temperature):
    plt.text(i, temp + 0.3, str(temp), ha="center")
plt.show()
languages = ["Python", "JavaScript", "Java", "C#", "C++"]
students = [35, 28, 22, 18, 15]










plt.figure(figsize=(10, 5))

plt.barh(languages, students, color=["gold", "blue", "green", "orange", "purple"])
for i, value in enumerate(students):
    plt.text(value + 0.5, i, str(value), va="center")

plt.xlabel("Telebe sayi")
plt.ylabel("Proqramlasdirma dilleri")
plt.title("Proqramlasdirma dillerini secen telebeler")
plt.figure(figsize=(10, 5))

plt.bar(languages, students)

plt.xlabel("Proqramlasdirma dilleri")
plt.ylabel("Telebe sayi")
plt.title("Proqramlasdirma dilleri - Vertical")

plt.show()
study_hours = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]

scores = [45, 50, 55, 60, 65, 70, 74, 80, 88, 95]

ages = [18, 19, 18, 20, 21, 19, 22, 20, 23, 21]
fig = plt.figure(figsize=(10, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
scatter = ax.scatter(
    study_hours,
    scores,
    c=ages,
    cmap="viridis",
    marker="o",
    s=100
)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Exam Score")
ax.set_title("Study Hours vs Exam Score")

ax.grid(True)
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label("Age")
max_index = scores.index(max(scores))

ax.scatter(
    study_hours[max_index],
    scores[max_index],
    marker="*",
    s=250,
    edgecolors="black",
    linewidths=1.5
)
ax2 = fig.add_axes([0.58, 0.15, 0.3, 0.25])

ax2.bar(study_hours, scores)

ax2.set_xlabel("Hours")
ax2.set_ylabel("Score")
ax2.set_title("Scores")
plt.show()