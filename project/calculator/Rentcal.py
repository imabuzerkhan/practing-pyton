# Rent Calculator

Flatbill = int(input("Enter the flatbill amount: "))
Food_bill = int(input("Enter the food bill amount: "))
Water_bill = int(input("Enter the water bill amount: "))
Electricity_unit_spend = int(input("Enter electricity unit consumed: "))
Charge_per_unit = int(input("Enter charge per unit: "))
Person = int(input("Enter the number of persons: "))

total_Electricity_bill = Electricity_unit_spend * Charge_per_unit
print(f"Total electricity bill: {total_Electricity_bill}")

total_bill = (total_Electricity_bill + Flatbill + Water_bill + Food_bill) / Person
Round_bill = round(total_bill)

print(f"Each person's bill is: {Round_bill}")
