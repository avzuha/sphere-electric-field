import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon0 = 8.854e-12  # Permittivity of free space

# Step 1: User input
R = float(input("Enter the radius of the sphere (in meters): "))
q = float(input("Enter the total charge of the sphere (in Coulombs): "))

# Step 2: Function to calculate E using Gauss's law
def electric_field(r, R, q):
    if r < R:  # Inside sphere
        E = (1 / (4 * np.pi * epsilon0)) * (q * r / R**3)
    elif np.isclose(r, R):  # On surface
        E = (1 / (4 * np.pi * epsilon0)) * (q / R**2)
    else:  # Outside sphere
        E = (1 / (4 * np.pi * epsilon0)) * (q / r**2)
    return E

# Step 3: Plot sphere and allow user to click
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), R, color='lightblue', alpha=0.5)
ax.add_artist(circle)

ax.set_xlim(-1.5*R, 1.5*R)
ax.set_ylim(-1.5*R, 1.5*R)
ax.set_aspect('equal', 'box')
ax.set_title("Click anywhere to calculate Electric Field")

# Step 4: Handle click event
def onclick(event):
    if event.xdata is None or event.ydata is None:
        return
    r = np.sqrt(event.xdata**2 + event.ydata**2)  # distance from center
    E = electric_field(r, R, q)
    print(f"Point clicked: (x={event.xdata:.2f}, y={event.ydata:.2f}), r={r:.2f} m")
    print(f"Electric Field at this point: {E:.3e} N/C")

    # Step 5: Generate graph of E vs r
    r_values = np.linspace(0.01, 2*R, 500)
    E_values = [electric_field(rv, R, q) for rv in r_values]

    plt.figure()
    plt.plot(r_values, E_values, label="Electric Field vs r")
    plt.axvline(R, color='red', linestyle='--', label="Sphere Surface (R)")
    plt.xlabel("Distance r (m)")
    plt.ylabel("Electric Field E (N/C)")
    plt.title("Electric Field Distribution")
    plt.legend()
    plt.grid(True)
    plt.show()

# Connect click event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
