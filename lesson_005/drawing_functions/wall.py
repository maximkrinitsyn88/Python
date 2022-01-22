import simple_draw as sd


def draw_wall(start_x, start_y):
    brick_width = 50
    brick_height = 25
    for y in range(8):
        if y % 2 == 0:
            shift = 25
        else:
            shift = 0
        for x in range(8):
            left_bottom_x = start_x + shift + brick_width * x
            left_bottom_y = start_y + brick_height * y
            left_bottom_point = sd.get_point(left_bottom_x, left_bottom_y)
            right_top_x = left_bottom_x + brick_width
            right_top_y = left_bottom_y + brick_height
            right_top_point = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom=left_bottom_point, right_top=right_top_point, color='orange', width=1)
