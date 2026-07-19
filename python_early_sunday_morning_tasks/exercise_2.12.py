speed = float(input("Enter Speed in (meters/second): "))

acceleration = float(input("Enter Acceleration in (meters/second): "))

minimum_runway_length = ((speed * speed) / (2 * acceleration))

print("The minimum runway length for this airplance is", minimum_runway_length)