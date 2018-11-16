from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds = Dots(600, 600, 150, 450, 150, 450)
    # Testing the top row
    dots_to_eat = []
    assert len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    for i in range(len(ds.top_row)):
        dots_to_eat.append(ds.top_row[i])
    ds.eat(dots_to_eat)
    assert len(ds.top_row) == 0
    # Testing the bottom row
    assert len(ds.bottom_row) == ds.WIDTH//ds.SPACING + 1
    dots_to_eat = []
    for i in range(ds.WIDTH//ds.SPACING + 1):
        dots_to_eat.append(ds.bottom_row[0])
        ds.eat(dots_to_eat)
        assert len(ds.bottom_row) == ds.WIDTH//ds.SPACING + 1 - 1 * (i + 1)
    # Testing the left column
    dots_to_eat = []
    assert len(ds.left_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        dots_to_eat.append(ds.left_col[0])
    ds.eat(dots_to_eat)
    assert len(ds.top_row) == 0
    # Testing the right column
    assert len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    dots_to_eat = []
    for i in range(ds.HEIGHT//ds.SPACING + 1):
        dots_to_eat.append(ds.right_col[0])
        ds.eat(dots_to_eat)
        assert len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1 - 1 * (i + 1)


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)


test_eat()
