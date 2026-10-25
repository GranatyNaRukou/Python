from pathlib import Path
    
def instructions_from_txt(file: Path) -> list:
    with open(file) as f:
        instructions = [line for line in f]
    return instructions

class Ship:
    def __init__(self):
        self.xy: complex = 0+0j
        self.direction:int = 90
        self.waypoint_xyj: complex = 10+1j

    def getDirection(self)->str:
        possible_directons = ["N", "E", "S", "W"]
        index = (self.direction // 90) % 4
        return possible_directons[index]

    def rotate_ship(self, degrees:int):
        self.direction += degrees


    def move_ship(self, command:str):
        direction = command[0]
        distance = int(command[1:])
        match direction:
            case "N":
                self.xy += distance * 1j
            case "S":
                self.xy -= distance * 1j
            case "E":
                self.xy += distance
            case "W":
                self.xy -= distance
            case "R":
                self.rotate_ship(distance)
            case "L":
                self.rotate_ship(-distance)
            case "F":
                self.move_ship(self.getDirection() + str(distance))

    def read_instructions(self, instructions: list):
        for command in instructions:
            self.move_ship(command)
    #Part 2
            #self.move_ship_waypoint(command)

    def rotate_waypoint_clockwise(self, degrees:int):
        for x in range(degrees // 90 % 4):
            self.waypoint_xyj *= -1j

    def rotate_waypoint_counter_clockwise(self, degrees:int):
        for x in range(degrees // 90 % 4):
            self.waypoint_xyj *= 1j

    def move_ship_waypoint(self, command:str):
        direction = command[0]
        distance = int(command[1:])
        match direction:
            case "N":
                self.waypoint_xyj += distance*1j
            case "S":
                self.waypoint_xyj -= distance*1j
            case "E":
                self.waypoint_xyj += distance
            case "W":
                self.waypoint_xyj -= distance
            case "R":
                self.rotate_waypoint_clockwise(distance)
            case "L":
                self.rotate_waypoint_counter_clockwise(distance)
            case "F":
                for i in range(distance):
                    self.xy += self.waypoint_xyj


def main():
    path = Path(__file__).parent / "data.txt"
    instructions = instructions_from_txt(path)
    lodicka: Ship = Ship()
    lodicka.read_instructions(instructions)
    x = abs(int(lodicka.xy.real))
    y = abs(int(lodicka.xy.imag))
    print(x + y)

if __name__ == "__main__":
    main()