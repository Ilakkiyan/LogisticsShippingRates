weight = float(input("Enter the package weight in kilogram: "))
rate = float(input("Enter the shipping rate per kilogram: "))

shipping_cost = weight * rate

print(f"Shipping Cost: {shipping_cost} USD")
