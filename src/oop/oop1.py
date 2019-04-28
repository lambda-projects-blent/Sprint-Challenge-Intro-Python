# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle():
    pass


class FlightVehicle(Vehicle):
    # Flight Vehicle is inheriting from base class Vehicle
    pass


class Airplane(FlightVehicle):
  # Airplane is inheriting from base class FlightVehicle
    pass


class Starship(FlightVehicle):
  # Starship is inheriting from base class FlightVehicle
    pass


class GroundVehicle(Vehicle):
  # GroundVehicle is inheriting from base class Vehicle
    pass


class Car(GroundVehicle):
  # Car is inheriting from base class GroundVehicle
    pass


class Motorcycle(GroundVehicle):
  # MotorCycle is inheriting from base class GroundVehicle
    pass
