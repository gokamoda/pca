import numpy as np


def create_2d_oval_data(
    n_samples=2000,
    center=(0, 0),
    max_radius_width=2,
    max_radius_height=1,
    angle_degree=0,
):
    """Generate 2D oval data."""
    # create random points on and inside a circle with radius 1
    radiuss = np.random.uniform(0, 1, n_samples)
    thetas = np.random.uniform(0, 2 * np.pi, n_samples)
    x = radiuss * np.cos(thetas)
    y = radiuss * np.sin(thetas)

    # Apply the oval transformation
    ## First, scale the points to the desired oval shape
    x = x * max_radius_width
    y = y * max_radius_height

    ## Then rotate the points by the specified angle
    angle_rad = np.deg2rad(angle_degree)
    x_rotated = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    y_rotated = x * np.sin(angle_rad) + y * np.cos(angle_rad)

    # sampled_radius =
    return np.column_stack((x_rotated + center[0], y_rotated + center[1]))
