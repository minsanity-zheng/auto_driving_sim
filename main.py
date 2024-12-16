import sys
import re
from auto_driving_sim import run_simulation, is_within_bounds, is_name_existed, is_position_occupied

def main():
    """
    Main function to handle user interaction and run the simulation.

    Returns:
        None
    """
    print("Welcome to Auto Driving Car Simulation!\n")
    field = {}
    cars = []

    while True:
        if not field:
            dimensions = input("Please enter the width and height of the simulation field in x y format: ").strip()
            if not re.match(r'^\d+ \d+$', dimensions):
                print("\nInvalid input. Please enter two integers separated by a space.")
                continue

            dimensions = dimensions.split()
            field['width'], field['height'] = int(dimensions[0]), int(dimensions[1])
            print(f"You have created a field of {field['width']} x {field['height']}.\n")

        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        choice = input().strip()

        if choice == '1':
            name = input("\nPlease enter the name of the car: ").strip()

            if is_name_existed(name, cars):
                print(f"\nName already existed. Please use another name.")
                continue

            position = input(f"\nPlease enter initial position of car {name} in x y Direction format: ").strip()
            if not re.match(r'^\d+ \d+ [NSEW]$', position):
                print("\nInvalid position format. Please enter in x y Direction format (e.g., 1 2 N).")
                continue

            position = position.split()
            x, y = int(position[0]), int(position[1])

            if not is_within_bounds(x, y, field['width'], field['height']):
                print(f"\nInvalid initial position. The position ({x}, {y}) is out of bounds.")
                continue
            
            if is_position_occupied(x, y, cars):
                print(f"\nInvalid initial position. The position ({x}, {y}) is already occupied by another car.")
                continue

            commands = input(f"\nPlease enter the commands for car {name}: ").strip().upper()
            if not re.match(r'^[LRF]+$', commands):
                print("\nInvalid commands. Please enter a sequence of L, R, and F only.")
                continue

            car = {
                'name': name,
                'x': x,
                'y': y,
                'direction': position[2],
                'commands': commands
            }
            cars.append(car)

            print("\nYour current list of cars are:")
            for car in cars:
                print(f"- {car['name']}, ({car['x']},{car['y']}) {car['direction']}, {car['commands']}")

        elif choice == '2':
            if not cars:
                print("\nNo cars to simulate. Add a car first.")
                continue
                   
            print("\nYour current list of cars are:")     
            for car in cars:
                print(f"- {car['name']}, ({car['x']},{car['y']}) {car['direction']}, {car['commands']}")

            sim_results = run_simulation(field, cars)
            print("\nAfter simulation, the result is:")
            for car in sim_results:
                if car[1]:
                    print(f"- {car[0]}, collides with {','.join(car[2])} at ({car[3]},{car[4]}) at step {car[5]}.")
                else:
                    print(f"- {car[0]}, ({car[2]},{car[3]}) {car[4]}")

            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            choice = input().strip()

            if choice == '1':
                field = {}
                cars = []
                continue
            elif choice == '2':
                print("Thank you for running the simulation. Goodbye!")
                sys.exit()

if __name__ == "__main__":
    main()
