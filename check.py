# -*- coding: utf-8 -*-
# 🎓 FINAL EXAM PRACTICE: CoDrone EDU Flight Readiness System
# Scenario: You are a lead engineer at e3 Aerospace. Before a drone can fly, 
# it must pass a "Pre-Check" based on real CoDrone EDU hardware specs.

# -------------------------------------------------------------------------
# STEP 1: LIBRARY & VENV CHECK (Instructor Verification)
# We are checking if the 'codrone_edu' library is active in your environment.
# -------------------------------------------------------------------------
library_status = ""
try:
    from codrone_edu.drone import Drone
    library_status = "Library detected. venv is active."
except ImportError:
    library_status = "System Check Failed: CoDrone EDU library not found."

print("--- System Diagnostics ---")
print(library_status) 
print("--------------------------\n")

# -------------------------------------------------------------------------
# STEP 2: FLIGHT DURATION ESTIMATE (Order of Operations)
# The CoDrone EDU has a maximum flight time of 480 seconds (8 minutes).
# Formula: Remaining Seconds = 480 - (Minutes Flown * 60)
# Need help? https://www.w3schools.com/python/python_operators.asp
# -------------------------------------------------------------------------

# Ask the user how many minutes they have already flown on this battery
minutes_input = input("How many minutes has this battery been used so far? ")
minutes_flown = float(minutes_input)

# TODO: Calculate the remaining_seconds using the formula above
remaining_seconds = 0 # Replace 0 with your formula: 480 - (minutes_flown * 60)

print(f"Estimated flight time remaining: {remaining_seconds} seconds")


# -------------------------------------------------------------------------
# STEP 3: FLIGHT PATH VERIFICATION (If/Elif/Else & Modulo)
# Scenario: You want to fly in a shape (polygon). The flight controller 
# only accepts an EVEN number of sides between 4 and 12.
# Need help? https://www.w3schools.com/python/python_conditions.asp
# -------------------------------------------------------------------------

sides_input = input("Enter an even number of sides for your flight shape (4-12): ")
num_sides = int(sides_input)

# TODO: Create an if-elif-else statement to verify the input:
# 1. If num_sides is less than 4 or greater than 12, print "Error: Out of range."
# 2. If the number is odd (num_sides % 2 != 0), print "Error: Must be an even number."
# 3. Else, print "Flight path verified! Preparing to fly."

# Write your code here:



# -------------------------------------------------------------------------
# STEP 4: MOTOR DIRECTION SCANNER (For Loops)
# The CoDrone EDU has 4 motors. 
# Motors 1 and 4 are Red/Blue wires (Clockwise - CW).
# Motors 2 and 3 are Black/White wires (Counter-Clockwise - CCW).
# Need help? https://www.w3schools.com/python/python_for_loops.asp
# -------------------------------------------------------------------------

print("\nStarting Motor Wiring Scan...")

# TODO: Create a for loop that ranges from 1 to 4 (representing the 4 motors)
# Inside the loop, use an if-else statement to print the wiring type:
# If the motor number is 1 or 4: Print "Motor [X]: Red/Blue Wires (CW)"
# Otherwise: Print "Motor [X]: Black/White Wires (CCW)"

# Write your loop here:


print("\n--- Pre-Check Complete ---")