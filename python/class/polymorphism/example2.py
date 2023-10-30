class Vehicle:
    def rotate(self):
        print("Reduz o consumo de combustível")


class ElectricVehicle(Vehicle):
    def rotate(self):
        super().rotate()
        print("Este veículo usa a eletricidade.")


electric_vehicle = ElectricVehicle()
electric_vehicle.rotate()
