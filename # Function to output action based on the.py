# Function to output action based on the traffic light color
def traffic_light_action(color):
    if color == "Red":
        return "Stop"
    elif color == "Yellow":
        return "Get Ready"
    elif color == "Green":
        return "Go"
    else:
        return "Invalid color"

# Input from the user
color = input("Enter the traffic light color (Red, Yellow, Green): ").capitalize()

# Get the corresponding action
action = traffic_light_action(color)
print(f"Action: {action}")
