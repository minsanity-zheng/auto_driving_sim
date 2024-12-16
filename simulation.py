from .utils import rotate_left, rotate_right, move_forward, is_within_bounds

def run_simulation(field, cars):
    """
    Run the simulation for all cars.

    Args:
        field (dict): Field dimensions with 'width' and 'height'.
        cars (list): List of car dictionaries with their details.

    Returns:
        list: Final status of the cars
    """
    steps = max(len(car['commands']) for car in cars)
    car_positions = {car['name']: (car['x'], car['y']) for car in cars}
    car_collison = {car['name']: False for car in cars}
    car_Collision_cars = {car['name']: [] for car in cars}
    car_Collision_step = {car['name']: 0 for car in cars}
    sim_result = []

    for step in range(steps):
        for car in cars:
            if step >= len(car['commands']) or car_collison[car['name']]:
                continue

            command = car['commands'][step]
            x, y, direction = car['x'], car['y'], car['direction']

            if command == 'L':
                car['direction'] = rotate_left(direction)
            elif command == 'R':
                car['direction'] = rotate_right(direction)
            elif command == 'F':
                new_x, new_y = move_forward(x, y, direction)

                if is_within_bounds(new_x, new_y, field['width'], field['height']):
                    car['x'], car['y'] = new_x, new_y
            car_positions[car['name']] = (car['x'], car['y'])

        # Check for collisions
        for car in cars:
            if car_collison[car['name']]:
                continue
            for other_car in cars:
                if car['name'] != other_car['name'] and car_positions[car['name']] == car_positions[other_car['name']]:
                    car_collison[car['name']] = True
                    car_Collision_step[car['name']] = step + 1
                    car_Collision_cars[car['name']].append(other_car['name'])
                    if not car_collison[other_car['name']]:
                        car_collison[other_car['name']] = True
                        car_Collision_step[other_car['name']] = step + 1
                        car_Collision_cars[other_car['name']].append(car['name'])

    for car in cars:
        if car_collison[car['name']]:
            sim_result.append([car['name'],car_collison[car['name']],car_Collision_cars[car['name']],car['x'],car['y'],car_Collision_step[car['name']]])
        else:
            sim_result.append([car['name'],car_collison[car['name']],car['x'],car['y'],car['direction']])
    return sim_result