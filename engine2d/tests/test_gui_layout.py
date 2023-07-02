from pytest import mark
from engine2d import DrawShapes

"""
TEST GUI

- click on 'draw shape' buttons and verify that layout is
the same as expected
- click on menu buttons and verify that layout is the same 
as expected
"""


@mark.buttons
def test_switch_color():
    """Test that 'Switch Color' button
    doesn't change layout."""
    engine = DrawShapes()

    # click on 'draw circle button'
    engine._circle_fields()

    # click on wipe up the board button
    engine._switch_color_button()

    buttons = []
    primary_buttons = []
    fields_and_labels = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    for item in engine.fields_and_labels:
        fields_and_labels.append(item[1])

    # verify the number of buttons, fields, labels is correct
    assert len(engine.buttons) == 1
    assert len(engine.primary_buttons) == 3
    assert len(engine.fields_and_labels) == 7

    # verify draw button is in place
    assert 'draw circle button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify fields and correct labels are in place
    assert 'field 1' in fields_and_labels
    assert 'field 2' in fields_and_labels
    assert 'field 3' in fields_and_labels
    assert 'X:' in fields_and_labels
    assert 'Y:' in fields_and_labels
    assert 'Radius:' in fields_and_labels
    assert 'Draw Circle' in fields_and_labels


@mark.buttons
def test_wipe_up_board():
    """Test that 'Wipe up the Board' button
    doesn't change layout."""

    engine = DrawShapes()

    # click on 'draw circle button'
    engine._circle_fields()

    # click on wipe up the board button
    engine._clean_up_button()

    buttons = []
    primary_buttons = []
    fields_and_labels = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    for item in engine.fields_and_labels:
        fields_and_labels.append(item[1])

    # verify the number of buttons, fields, labels is correct
    assert len(engine.buttons) == 1
    assert len(engine.primary_buttons) == 3
    assert len(engine.fields_and_labels) == 7

    # verify draw button is in place
    assert 'draw circle button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify fields and correct labels are in place
    assert 'field 1' in fields_and_labels
    assert 'field 2' in fields_and_labels
    assert 'field 3' in fields_and_labels
    assert 'X:' in fields_and_labels
    assert 'Y:' in fields_and_labels
    assert 'Radius:' in fields_and_labels
    assert 'Draw Circle' in fields_and_labels


@mark.buttons
def test_return_to_menu():
    """
    Test that clicking 'List of Options' button
    resets menu back to its original state.
    """
    engine = DrawShapes()

    # click on 'draw circle button'
    engine._circle_fields()

    # click on 'list of options' button
    engine.back_to_list_of_options()

    buttons = []
    primary_buttons = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    # verify correct number of buttons are on the page
    assert len(engine.buttons) == 3
    assert len(engine.primary_buttons) == 3

    # verify draw shape buttons are in place
    assert 'rectangle mode button' in buttons
    assert 'triangle mode button' in buttons
    assert 'circle mode button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify other objects are not on the page
    assert len(engine.fields_and_labels) == 0


@mark.buttons
def test_circle_mode_buttons():
    """
    Test that 'draw circle mode' has all the correct buttons
    and nothing else.
    """
    engine = DrawShapes()

    # click on 'draw circle button'
    engine._circle_fields()

    buttons = []
    primary_buttons = []
    fields_and_labels = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    for item in engine.fields_and_labels:
        fields_and_labels.append(item[1])

    # verify the number of buttons, fields, labels is correct
    assert len(engine.buttons) == 1
    assert len(engine.primary_buttons) == 3
    assert len(engine.fields_and_labels) == 7

    # verify draw button is in place
    assert 'draw circle button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify fields and correct labels are in place
    assert 'field 1' in fields_and_labels
    assert 'field 2' in fields_and_labels
    assert 'field 3' in fields_and_labels
    assert 'X:' in fields_and_labels
    assert 'Y:' in fields_and_labels
    assert 'Radius:' in fields_and_labels
    assert 'Draw Circle' in fields_and_labels


@mark.buttons
def test_triangle_mode_buttons():
    """
    Test that 'draw triangle mode' has all the correct buttons
    and nothing else.
    """
    engine = DrawShapes()

    # click on 'draw triangle button'
    engine._triangle_fields()

    buttons = []
    primary_buttons = []
    fields_and_labels = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    for item in engine.fields_and_labels:
        fields_and_labels.append(item[1])

    # verify the number of buttons, fields, labels is correct
    assert len(engine.buttons) == 1
    assert len(engine.primary_buttons) == 3
    assert len(engine.fields_and_labels) == 7

    # verify draw button is in place
    assert 'draw triangle button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify fields and correct labels are in place
    assert 'field 1' in fields_and_labels
    assert 'field 2' in fields_and_labels
    assert 'field 3' in fields_and_labels
    assert 'X1,Y1:' in fields_and_labels
    assert 'X2,Y2:' in fields_and_labels
    assert 'X3,Y3:' in fields_and_labels
    assert 'Draw Triangle' in fields_and_labels


@mark.buttons
def test_rectangle_mode_buttons():
    """
    Test that 'draw rectangle mode' has all the correct buttons
    and nothing else.
    """
    engine = DrawShapes()

    # click on 'draw rectangle button'
    engine._rectangle_fields()

    buttons = []
    primary_buttons = []
    fields_and_labels = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    for item in engine.fields_and_labels:
        fields_and_labels.append(item[1])

    # verify the number of buttons, fields, labels is correct
    assert len(engine.buttons) == 1
    assert len(engine.primary_buttons) == 3
    assert len(engine.fields_and_labels) == 7

    # verify draw button is in place
    assert 'draw rectangle button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify fields and correct labels are in place
    assert 'field 1' in fields_and_labels
    assert 'field 2' in fields_and_labels
    assert 'field 3' in fields_and_labels
    assert 'X1,Y1:' in fields_and_labels
    assert 'X2,Y2:' in fields_and_labels
    assert 'NA' in fields_and_labels
    assert 'Draw Rectangle' in fields_and_labels


@mark.buttons
def test_menu_buttons():
    """Test that menu has three draw shape buttons
    and three primary control buttons.
    """
    engine = DrawShapes()

    buttons = []
    primary_buttons = []

    for button in engine.buttons:
        buttons.append(button[1])

    for primary_button in engine.primary_buttons:
        primary_buttons.append(primary_button[1])

    # verify correct number of buttons are on the page
    assert len(engine.buttons) == 3
    assert len(engine.primary_buttons) == 3

    # verify draw shape buttons are in place
    assert 'rectangle mode button' in buttons
    assert 'triangle mode button' in buttons
    assert 'circle mode button' in buttons

    # verify primary control buttons are in place
    assert 'erase button' in primary_buttons
    assert 'switch color button' in primary_buttons
    assert 'menu button' in primary_buttons

    # verify other objects are not on the page
    assert len(engine.fields_and_labels) == 0
