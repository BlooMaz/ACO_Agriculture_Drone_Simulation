import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg



def create_figure(coords):
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(0, 400)  # Set X-axis limits
    ax.set_ylim(0, 400)  # Set Y-axis limits

    marker_img = mpimg.imread('drone_pointer.png')  # Replace with the path to your image file

    # Create a scatter plot with an initial position
    point = ax.scatter(coords[0][0], coords[0][1], marker='o')

    # Define the number of steps for interpolation
    num_steps = 50  # Increase this value for smoother movement

    # Traverse through the list of coordinates
    for i in range(1, len(coords)):
        # Get the current and next coordinates
        x_current, y_current = coords[i - 1]
        x_next, y_next = coords[i]

        # Calculate the intermediate positions using linear interpolation
        x_interp = np.linspace(x_current, x_next, num=num_steps)
        y_interp = np.linspace(y_current, y_next, num=num_steps)

        # Update the position of the point for each intermediate position
        for j in range(num_steps):
            x, y = x_interp[j], y_interp[j]
            point.set_offsets((x, y))
            plt.pause(0.01)  # Pause for a short duration to observe the movement

    # Show the final plot
    plt.show()
