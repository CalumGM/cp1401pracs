HEX_COLOURS = {"Alice Blue": "#f0f8ff", "Antique White": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown": "#a52a2a",
               "burlywood": "#deb887"}

colour = input(">>> ")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
        colour = input(">>> ")
    else:
        print("Invalid hex code")
        colour = input(">>> ")
print("prgm end")

# joshuawong1
