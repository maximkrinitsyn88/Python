import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
start_point_x = 0
start_point_y = 0


def draw_rainbow():
    for _ in range(2200, 2341, 20):
        color = rainbow_colors.pop(6)
        rainbow_colors.insert(0, color)
        sd.circle(center_position=sd.get_point(start_point_x, start_point_y), radius=_, color=color, width=30)
