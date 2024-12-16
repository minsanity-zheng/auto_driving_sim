def rotate_left(direction):
    """
    Rotate the direction 90 degrees to the left.

    Args:
        direction (str): The current direction (N, E, S, W).

    Returns:
        str: The new direction after rotation.
    """
    return {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }[direction]

def rotate_right(direction):
    """
    Rotate the direction 90 degrees to the right.

    Args:
        direction (str): The current direction (N, E, S, W).

    Returns:
        str: The new direction after rotation.
    """
    return {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }[direction]

def move_forward(x, y, direction):
    """
    Move one step forward in the given direction.

    Args:
        x (int): Current x-coordinate.
        y (int): Current y-coordinate.
        direction (str): The direction of movement (N, E, S, W).

    Returns:
        tuple: New x and y coordinates after moving forward.
    """
    if direction == 'N':
        return x, y + 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'S':
        return x, y - 1
    elif direction == 'W':
        return x - 1, y

def is_within_bounds(x, y, width, height):
    """
    Check if the coordinates are within the field boundaries.

    Args:
        x (int): X-coordinate.
        y (int): Y-coordinate.
        width (int): Width of the field.
        height (int): Height of the field.

    Returns:
        bool: True if within bounds, False otherwise.
    """
    return 0 <= x < width and 0 <= y < height

def is_name_existed(name, cars):
    """
    Check if the name is already given to an existing car.

    Args:
        name (str): Name of the new car.
        cars (list): List of existing cars with their name.

    Returns:
        bool: True if name existed, False otherwise.
    """
    return any(car['name'] == name for car in cars)

def is_position_occupied(x, y, cars):
    """
    Check if the position is already occupied by an existing car.

    Args:
        x (int): X-coordinate of the new car.
        y (int): Y-coordinate of the new car.
        cars (list): List of existing cars with their positions.

    Returns:
        bool: True if position is occupied, False otherwise.
    """
    return any(car['x'] == x and car['y'] == y for car in cars)