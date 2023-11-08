#10.1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Moving up from {self.current} floor to {self.current+1} floor")
            self.current += 1
    def floor_down(self):
        if self.current > self.bottom:
            print(f"Moving down from {self.current} floor to {self.current-1} floor")
            self.current -= 1

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range(floor-self.current):
                self.floor_up()
        elif floor < self.current:
            for i in range(self.current-floor):
                self.floor_down()
        else:
            print("You are already on that floor")

#10.2
class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator, floor):
        print(f"Elevator {elevator} moving...")
        self.elevators[elevator-1].go_to_floor(floor)
#10.3
    def fire_alarm(self):
        print("Fire!!!")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)


building = Building(1,6,3)
building.run_elevator(1,5)
building.run_elevator(3,2)
building.run_elevator(2,3)
building.run_elevator(1,3)

building.fire_alarm()

#10.4


