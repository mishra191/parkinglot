# parkinglot
This repository contains a Python-based Parking Lot Management System, designed to handle parking reservations and fee calculations. The system is tested using the unittest framework to ensure reliability and accuracy.

Key Features:
Parking Reservation:

Reserve Parking Spot: Users can reserve a parking spot at a specified start time.
Generate Parking Ticket: A parking ticket is generated upon reservation, including the ticket number and reservation details.
Parking Unreservation:

Unreserve Parking Spot: Users can unreserve their parking spot at a specified end time.
Generate Parking Receipt: Upon unreservation, a receipt is generated that calculates the total parking fee based on the duration of the parking.
Fee Calculation:

The system calculates parking fees based on the duration of stay, with the fee increasing over time.
Test Scenarios:
The system has been tested through multiple scenarios to validate its functionality:

Test 1: Reservation and unreservation of a parking spot for a 1-hour duration, resulting in a fee of $10.00.
Test 2: Reservation and unreservation for a 3-hour duration, resulting in a fee of $20.00.
Test 3: Reservation and unreservation for a 4-hour duration, resulting in a fee of $30.00.

This repository offers a robust solution for managing parking reservations and fee calculations, with comprehensive unit tests to ensure correct functionality. This has some extra features as below


● The parking lot will allow different types of vehicles to be parked:


● Each vehicle will occupy a single spot and the spot size will be different for different
vehicles.


● The number of spots per vehicle type will be different for different parking lots. For
example

○ Motorcycles/scooters: 100 spots
○ Cars/SUVs: 80 spots
○ Buses/Trucks: 40 spots


● When a vehicle is parked, a parking ticket should be generated with the spot number
and the entry date-time.


● When a vehicle is unparked, a receipt should be generated with the entry date-time,
exit date-time, and the applicable fees to be paid.

● The parking lot will allow different types of vehicles to be parked


● Each vehicle will occupy a single spot and the spot size will be different for different
vehicles.


● The number of spots per vehicle type will be different for different parking lots. For
example
○ Motorcycles/scooters: 100 spots
○ Cars/SUVs: 80 spots
○ Buses/Trucks: 40 spots


● When a vehicle is parked, a parking ticket should be generated with the spot number
and the entry date-time.


● When a vehicle is unparked, a receipt should be generated with the entry date-time,
exit date-time, and the applicable fees to be paid.
