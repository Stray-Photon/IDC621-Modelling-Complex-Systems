import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import scienceplots
import os

output_dir = "2Dmodelplots"
os.makedirs(output_dir, exist_ok=True)

N = 100
p = 0.015
steps = 1000
ignite_if_dead = True

EMPTY, TREE, FIRE = 0, 1, 2

grid = np.zeros((N, N), dtype=int)
frames = []

def neighbors(i, j):
    return [
        ((i - 1) % N, j),
        ((i + 1) % N, j),
        (i, (j - 1) % N),
        (i, (j + 1) % N),
    ]

def step(grid):
    new_grid = grid.copy()

    for i in range(N):
        for j in range(N):
            if grid[i, j] == FIRE:
                new_grid[i, j] = EMPTY
                for ni, nj in neighbors(i, j):
                    if grid[ni, nj] == TREE:
                        new_grid[ni, nj] = FIRE

    growth = np.random.rand(N, N) < p
    new_grid[(grid == EMPTY) & growth] = TREE

    if ignite_if_dead and not np.any(new_grid == FIRE):
        trees = np.argwhere(new_grid == TREE)
        if len(trees) > 0:
            i, j = trees[np.random.randint(len(trees))]
            new_grid[i, j] = FIRE

    return new_grid

# Simulation and Plotting

for t in range(steps):
    grid = step(grid)
    frames.append(grid.copy())

plt.style.use("science")
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

img = ax.imshow(frames[0], cmap="viridis", vmin=0, vmax=2)
ax.axis("off")

ax_slider = plt.axes([0.15, 0.15, 0.7, 0.03])
slider = Slider(ax_slider, "Time", 0, steps - 1, valinit=0, valstep=1)

ax_button = plt.axes([0.4, 0.05, 0.2, 0.06])
button = Button(ax_button, "Pause")

paused = False
current_frame = 0

def slider_update(val):
    global current_frame
    current_frame = int(val)
    img.set_data(frames[current_frame])
    fig.canvas.draw_idle()

slider.on_changed(slider_update)

def animate(_):
    global current_frame
    if not paused:
        current_frame = (current_frame + 1) % steps
        slider.set_val(current_frame)

ani = FuncAnimation(fig, animate, interval=40)

def toggle_pause(event):
    global paused
    paused = not paused
    button.label.set_text("Play" if paused else "Pause")

button.on_clicked(toggle_pause)

plt.show()

try:
    t_snapshot = int(input(f"\nTime step to save snapshot (0 – {steps-1}): "))

    if 0 <= t_snapshot < steps:
        snapshot_name = input("Enter filename for snapshot: ")
        save_path = os.path.join(output_dir, f"{snapshot_name}.png")

        plt.figure()
        plt.imshow(frames[t_snapshot], cmap="viridis", vmin=0, vmax=2)
        plt.axis("off")

        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Snapshot saved → {save_path}")
    else:
        print("Invalid time step.")

except ValueError:
    print("Invalid input.")