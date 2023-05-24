import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from fuzzy_system import fuzzy_system


def main():
    # Get a fuzzy system instance
    sim = fuzzy_system()

    # Simulate at higher resolution with full accuracy
    upsampled = np.linspace(-2, 2, 21)
    x, y = np.meshgrid(upsampled, upsampled)
    z = np.zeros_like(x)

    # Loop through the system 21*21 times to collect the control surface
    for i in range(21):
        for j in range(21):
            sim.input["error"] = x[i, j]
            sim.input["delta"] = y[i, j]
            sim.compute()
            z[i, j] = sim.output["output"]

    # Plot the result in pretty 3D with alpha blending
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    cmap = matplotlib.colormaps["viridis"]  # type: ignore

    surf = ax.plot_surface(
        x, y, z, rstride=1, cstride=1, cmap=cmap, linewidth=10, antialiased=True
    )

    cset = ax.contourf(x, y, z, zdir="z", offset=-2.5, cmap=cmap, alpha=0.5)
    cset = ax.contourf(x, y, z, zdir="x", offset=3, cmap=cmap, alpha=0.5)
    cset = ax.contourf(x, y, z, zdir="y", offset=3, cmap=cmap, alpha=0.5)

    ax.view_init(30, 200)
    ax.set_xlabel("Error input")
    ax.set_ylabel("Delta input")
    ax.set_zlabel("Output")

    fig.colorbar(surf, shrink=0.5)
    plt.show()


if __name__ == "__main__":
    main()
