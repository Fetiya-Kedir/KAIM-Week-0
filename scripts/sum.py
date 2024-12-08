# Function to draw a star pyramid
def draw_star_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Number of rows for the pyramid
rows = int(input("Enter the number of rows: "))
draw_star_pyramid(rows)
