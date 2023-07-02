from pytest import mark
from engine2d import DrawShapes


"""
TEST VALIDATION

- test input validation
"""


@mark.validation
@mark.parametrize("dimensions", [[(123, 135), (500, )],
                                 [('sdfsd'), (259, 125)],
                                 [(), ()]])
def test_rectangle_validation(dimensions):
    """Test validation for 'draw rectangle' function."""
    engine = DrawShapes()

    engine.x1_y1 = dimensions[0]
    engine.x2_y2 = dimensions[1]

    engine.draw_rectangle()

    error_message = "Invalid input! Input for required fields should be two integers separated by a comma with no space in between. Ex: 23,23"

    assert engine.error_message == error_message


@mark.validation
@mark.parametrize("dimensions", [[(123, 135), (500,), (500, 245)],
                                 [('sdfsd'), (259, 125), (500, 353)],
                                 [(), (), ()]])
def test_triangle_validation(dimensions):
    """Test validation for 'draw triangle' function."""
    engine = DrawShapes()

    engine.x1_y1 = dimensions[0]
    engine.x2_y2 = dimensions[1]
    engine.x3_y3 = dimensions[2]

    engine.draw_triangle()

    error_message = "Invalid input! Input should be two integers separated by a comma with no space in between. Ex: 23,23"

    assert engine.error_message == error_message


@mark.validation
@mark.parametrize("dimensions", [['sdf', 100, 26],
                                 [None, None, None],
                                 ['233', '534', '345']])
def test_circle_validation(dimensions):
    """Test validation for 'draw circle' function."""
    engine = DrawShapes()

    engine.x = dimensions[0]
    engine.x = dimensions[1]
    engine.radius = dimensions[2]

    engine.draw_circle()

    error_message = "Invalid input! Input should be an integer."

    assert engine.error_message == error_message
