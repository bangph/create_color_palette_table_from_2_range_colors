from colour import Color

# Created by: Bang Pham Huu

brown_from = Color("#FFF201")
brown_colors = list(brown_from.range_to(Color("#FD3D00"),155))

green_from = Color("#80B107")
green_colors = list(green_from.range_to(Color("#036200"),100))

colors = brown_colors + green_colors

rgb_colors = []

for color in colors:
    value = color.hex

    if len(color.hex) == 4:
        tmp = color.hex[1:]
        red = tmp[0] + tmp[0]
        green = tmp[1] + tmp[1]
        blue = tmp[2] + tmp[2]
        value = "#" + red + green + blue

    rgb_color = str(tuple(bytearray.fromhex(value.replace("#","")))).replace("(", "[").replace(")", "]").replace(", ", ",")
    rgb_colors.append(rgb_color.replace("]", ",255]"))

rgb_colors.append("[255,255,255,255]")

print '"{\\\"colorPalette\\\":{\\\"colorTable\\\":[ ' + ",".join(rgb_colors) + ' ]}}"'
