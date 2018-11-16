from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450, 150, 450, g)
    # when pacaman is at the upper left of the row and faces nagative
    # it eats two dots
    pacaman_x = 0
    pacaman_y = m.TOP_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=-1)
    assert len(m.dots.top_row) == m.WIDTH//m.dots.SPACING - 1
    # when pacaman is at the lower right of the row and faces positive
    # it eats two dots
    pacaman_x = m.WIDTH
    pacaman_y = m.BOTTOM_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=1)
    assert len(m.dots.bottom_row) == m.WIDTH//m.dots.SPACING - 1
    # when pacaman is at the upper left and faces positive
    # it eats only one dot
    pacaman_x = m.LEFT_VERT
    pacaman_y = 0
    m.eat_dots(pacaman_x, pacaman_y, direction=1)
    assert len(m.dots.left_col) == m.HEIGHT//m.dots.SPACING
    # when pacaman is at the lower lower right and faces negative
    # it eats  dots
    pacaman_x = m.RIGHT_VERT
    pacaman_y = m.HEIGHT
    m.eat_dots(pacaman_x, pacaman_y, direction=-1)
    assert len(m.dots.right_col) == m.HEIGHT//m.dots.SPACING
    # when pacaman is at the upper left intersection
    # it eats two dots: one from the top row, the other from the left column
    pacaman_x = m.LEFT_VERT
    pacaman_y = m.TOP_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=1)
    assert len(m.dots.top_row) == m.WIDTH//m.dots.SPACING - 2
    assert len(m.dots.left_col) == m.HEIGHT//m.dots.SPACING - 1
    # when pacaman is at the lower left intersection
    # it eats two dots: one from the bottom row
    # the other from the right column
    pacaman_x = m.LEFT_VERT
    pacaman_y = m.BOTTOM_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=1)
    assert len(m.dots.bottom_row) == m.WIDTH//m.dots.SPACING - 2
    assert len(m.dots.left_col) == m.HEIGHT//m.dots.SPACING - 2
    # when pacaman is at the upper right intersection
    # it eats two dots: one from the top row, the other from the right column
    pacaman_x = m.RIGHT_VERT
    pacaman_y = m.TOP_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=1)
    assert len(m.dots.top_row) == m.WIDTH//m.dots.SPACING - 3
    assert len(m.dots.right_col) == m.HEIGHT//m.dots.SPACING - 1
    # when pacaman is at the lower right intersection
    # it eats two dots: one from the bottom row
    # the other from the right column
    pacaman_x = m.RIGHT_VERT
    pacaman_y = m.BOTTOM_HORIZ
    m.eat_dots(pacaman_x, pacaman_y, direction=-1)
    assert len(m.dots.bottom_row) == m.WIDTH//m.dots.SPACING - 3
    assert len(m.dots.right_col) == m.HEIGHT//m.dots.SPACING - 2
