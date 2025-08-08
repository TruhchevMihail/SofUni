from project.plants.base_plant import BasePlant

# Test class that inherits from BasePlant
class ConcretePlant(BasePlant):
    def plant_details(self):
        return f"Plant: {self.name}, Price: {self.price}, Water Needed: {self.water_needed}"

# Test valid initialization
try:
    plant = ConcretePlant("Rose", 10.5, 500)
    print("Valid initialization test: PASSED")
    print(f"Plant details: {plant.plant_details()}")
except Exception as e:
    print(f"Valid initialization test: FAILED - {str(e)}")

# Test invalid name (empty)
try:
    plant = ConcretePlant("", 10.5, 500)
    print("Empty name test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Plant name cannot be null or empty!":
        print("Empty name test: PASSED")
    else:
        print(f"Empty name test: FAILED - Wrong error message: {str(e)}")

# Test invalid name (whitespace only)
try:
    plant = ConcretePlant("   ", 10.5, 500)
    print("Whitespace name test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Plant name cannot be null or empty!":
        print("Whitespace name test: PASSED")
    else:
        print(f"Whitespace name test: FAILED - Wrong error message: {str(e)}")

# Test invalid price (zero)
try:
    plant = ConcretePlant("Rose", 0, 500)
    print("Zero price test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Price must be greater than zero!":
        print("Zero price test: PASSED")
    else:
        print(f"Zero price test: FAILED - Wrong error message: {str(e)}")

# Test invalid price (negative)
try:
    plant = ConcretePlant("Rose", -5.5, 500)
    print("Negative price test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Price must be greater than zero!":
        print("Negative price test: PASSED")
    else:
        print(f"Negative price test: FAILED - Wrong error message: {str(e)}")

# Test invalid water_needed (too low)
try:
    plant = ConcretePlant("Rose", 10.5, 0)
    print("Low water test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Water needed must be between 1 and 2000 ml!":
        print("Low water test: PASSED")
    else:
        print(f"Low water test: FAILED - Wrong error message: {str(e)}")

# Test invalid water_needed (too high)
try:
    plant = ConcretePlant("Rose", 10.5, 2001)
    print("High water test: FAILED - Should have raised ValueError")
except ValueError as e:
    if str(e) == "Water needed must be between 1 and 2000 ml!":
        print("High water test: PASSED")
    else:
        print(f"High water test: FAILED - Wrong error message: {str(e)}")

# Test that BasePlant cannot be instantiated directly
try:
    base_plant = BasePlant("Test", 10.0, 100)
    print("Abstract class test: FAILED - Should not be able to instantiate BasePlant")
except TypeError:
    print("Abstract class test: PASSED - Cannot instantiate abstract class")
except Exception as e:
    print(f"Abstract class test: FAILED - Wrong error type: {type(e).__name__}")