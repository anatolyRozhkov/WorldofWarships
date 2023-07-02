from pytest import mark
from engine2d import DrawShapes

"""
TEST BASIC OPERATIONS

- test drawing shapes of different colors
- test erasing shapes
"""


@mark.basics
def test_erase_shapes():
    """Draw shapes, then erase them."""
    engine = DrawShapes()

    # set dimensions for triangle and rectangle
    engine.x1_y1 = (123, 135)
    engine.x2_y2 = (500, 245)
    engine.x3_y3 = (259, 125)

    # set dimensions for circle
    engine.x = 200
    engine.y = 300
    engine.radius = 25

    # draw shapes
    engine.draw_rectangle()
    engine.draw_triangle()
    engine.draw_circle()

    # verify shapes have been drawn
    assert len(engine.drawings) == 3

    engine.clean_up()

    # verify shapes have been erased
    assert len(engine.drawings) == 0


@mark.basics
@mark.parametrize("dimensions", [[(123, 135), (500, 245), 'blue'],
                                 [(223, 135), (259, 125), 'red']])
def test_draw_rectangle(dimensions: list):
    """Draw a rectangle with specified dimensions,
    verify it's in the list of drawn shapes."""
    engine = DrawShapes()

    engine.x1_y1 = dimensions[0]
    engine.x2_y2 = dimensions[1]
    engine.color = dimensions[2]

    message = f"Drawing Rectangle: {dimensions[0]}, {dimensions[1]}. Color: {dimensions[2]}."

    engine.draw_rectangle()

    # verify exactly one shape has been drawn
    assert len(engine.drawings) == 1

    # verify the shape has a correct message
    # engine.drawings -> [drawing object, message]
    # engine.drawings[0][1] -> message
    assert engine.drawings[0][1] == message


@mark.basics
@mark.parametrize("dimensions", [[(123, 135), (500, 245), (500, 245), 'blue'],
                                 [(223, 135), (259, 125), (500, 353), 'red']])
def test_draw_triangle(dimensions: list):
    """Draw a triangle with specified dimensions,
    verify it's in the list of drawn shapes."""
    engine = DrawShapes()

    engine.x1_y1 = dimensions[0]
    engine.x2_y2 = dimensions[1]
    engine.x3_y3 = dimensions[2]
    engine.color = dimensions[3]

    message = f"Drawing Triangle: {dimensions[0]}, {dimensions[1]}, {dimensions[2]}. Color: {dimensions[3]}."

    engine.draw_triangle()

    # verify exactly one shape has been drawn
    assert len(engine.drawings) == 1

    # verify the shape has a correct message
    # engine.drawings -> [drawing object, message]
    # engine.drawings[0][1] -> message
    assert engine.drawings[0][1] == message


@mark.basics
@mark.parametrize("dimensions", [[125, 135, 25, 'green'], [325, 235, 40, 'yellow']])
def test_draw_circle(dimensions: list):
    """Draw a circle with specified dimensions,
    verify it's in the list of drawn shapes."""
    engine = DrawShapes()

    engine.x = dimensions[0]
    engine.y = dimensions[1]
    engine.radius = dimensions[2]
    engine.color = dimensions[3]

    message = f"Drawing Circle:({dimensions[0]}, {dimensions[1]}) with radius {dimensions[2]}. Color: {dimensions[3]}."

    engine.draw_circle()

    # verify exactly one shape has been drawn
    assert len(engine.drawings) == 1

    # verify the shape has a correct message
    # engine.drawings -> [drawing object, message]
    # engine.drawings[0][1] -> message
    assert engine.drawings[0][1] == message
