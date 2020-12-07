distance = float(input("Please input the distance: "))
consumption = float(input("Please input fuel consumption per 100 km: "))
fuel_consumed = distance/consumption
print("Total distance: ", distance, "km", "\nConsumption per 100 km:", consumption, " litres", "\nFuel consumed: ", round(fuel_consumed,2), " litres")
