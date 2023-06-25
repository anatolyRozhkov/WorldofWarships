import tkinter as tk
import random


class Engine2D:
    """Create canvas, display buttons for drawing shapes and control buttons."""
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = None
        self._set_canvas()

        # widget default coordinates (use this for positioning buttons & fields)
        self.x_value_for_widgets = 180
        self.y_value_for_widgets = 420

        # keep widgets and drawings in one place
        self.buttons = []
        self.drawings = []
        self.fields_and_labels = []

        # control buttons
        self._clean_up_button()
        self._switch_color_button()

        # default color
        self.color = 'red'

    def main_loop(self):
        self.window.mainloop()

    def _switch_color_button(self) -> None:
        """Creates button for switching colors."""

        button = tk.Button(self.window, text="Switch Color", command=self.switch_color)
        self.canvas.create_window(self.x_value_for_widgets + 370,
                                  self.y_value_for_widgets + 40, window=button)

    def switch_color(self) -> None:
        """Sets a random color for drawing."""
        list_of_colors = ['blue', 'green', 'yellow', 'cyan', 'red', 'black', 'white', 'magenta']
        self.color = random.choice(list_of_colors)

    @staticmethod
    def delete_widget(what_to_delete) -> None:
        """Deletes provided widget object."""
        what_to_delete.destroy()

    def _set_canvas(self, width: int = 750, height: int = 480) -> None:
        """Sets canvas."""
        self.canvas = tk.Canvas(self.window, width=width, height=height)
        self.canvas.pack()

    def clean_up(self) -> None:
        """Erises all drawings from canvas."""
        for drawing in self.drawings:
            self.canvas.delete(drawing)

        self.drawings = []

    def _clean_up_button(self) -> None:
        """Button for wiping up all drawings from the board."""
        button = tk.Button(self.window, text="Wipe up the board", command=self.clean_up)
        self.canvas.create_window(self.x_value_for_widgets + 370,
                                  self.y_value_for_widgets, window=button)

    def _fields(self, *args: str) -> list:
        """Creates fields for specifying drawing dimensions.
        Those fields are then passed down as a list, so that
        draw functions could get values from them"""

        for button in self.buttons:
            self.delete_widget(button)

        # create fields
        field_1 = tk.Entry(self.window)
        field_2 = tk.Entry(self.window)
        field_3 = tk.Entry(self.window)

        # create labels
        label_1 = tk.Label(self.window, text=args[0])
        label_2 = tk.Label(self.window, text=args[1])
        label_3 = tk.Label(self.window, text=args[2])
        label_instructions = tk.Label(self.window, text=args[3])

        fields_and_labels = [field_1, field_2, field_3, label_1, label_2, label_3, label_instructions]

        # keep track of those widgets
        for widget in fields_and_labels:
            self.fields_and_labels.append(widget)

        # draw labels
        self.canvas.create_window(self.x_value_for_widgets, self.y_value_for_widgets - 20, window=label_1)
        self.canvas.create_window(self.x_value_for_widgets, self.y_value_for_widgets, window=label_2)
        self.canvas.create_window(self.x_value_for_widgets, self.y_value_for_widgets + 20, window=label_3)
        self.canvas.create_window(self.x_value_for_widgets + 150,
                                  self.y_value_for_widgets - 50, window=label_instructions)

        # field widget
        self.canvas.create_window(self.x_value_for_widgets + 150, self.y_value_for_widgets - 20, window=field_1)
        self.canvas.create_window(self.x_value_for_widgets + 150, self.y_value_for_widgets, window=field_2)
        self.canvas.create_window(self.x_value_for_widgets + 150, self.y_value_for_widgets + 20, window=field_3)

        return [field_1, field_2, field_3]


class Circle(Engine2D):
    """Draw circles."""
    def __init__(self):
        super().__init__()

        # display draw circle button
        self._open_circle_fields_button()

        # drawing coordinates and parameters
        self.x = None
        self.y = None
        self.radius = None

    def _open_circle_fields_button(self) -> None:
        """Button for displaying fields that are needed to specify dimensions for a circle."""
        button = tk.Button(self.window, text="draw circle", command=self._circle_fields)

        # add button to list of button widgets
        self.buttons.append(button)

        # draw widget
        self.canvas.create_window(self.x_value_for_widgets,
                                  self.y_value_for_widgets, window=button)

    def _draw_circle_button(self) -> None:
        """Button for triggering draw_circle function; drawing a circle."""
        button = tk.Button(self.window, text="Draw",
                           command=self.draw_circle)

        self.buttons.append(button)

        self.canvas.create_window(self.x_value_for_widgets - 100, self.y_value_for_widgets, window=button)

    def draw_circle(self) -> None:
        """Draw a circle using dimensions provided by user."""
        x_value = int(self.x.get())
        y_value = int(self.y.get())
        radius_value = int(self.radius.get())

        print(f"Drawing Circle:({x_value}, {y_value}) with radius {radius_value}. Color: {self.color}.")

        new_drawing = self.canvas.create_oval(x_value - radius_value,
                                              y_value - radius_value,
                                              x_value + radius_value,
                                              y_value + radius_value,
                                              outline=self.color)

        # add this to the list of drawings
        self.drawings.append(new_drawing)

    def _circle_fields(self) -> None:
        """Fields where user will specify dimensions for a circle to be drawn."""
        fields = self._fields('X:', 'Y:', 'Radius:', 'Draw Circle')

        # draw circle
        self._draw_circle_button()

        # assign values
        self.x = fields[0]
        self.y = fields[1]
        self.radius = fields[2]


class Triangle(Engine2D):
    """Draw triangles."""
    def __init__(self):
        super().__init__()

        # display draw triangle
        self._open_triangle_fields_button()

        # assign values
        self.x1_y1 = None
        self.x2_y2 = None
        self.x3_y3 = None

    def _open_triangle_fields_button(self) -> None:
        """Button for displaying fields that are needed to specify dimensions for a triangle."""
        button = tk.Button(self.window, text="draw triangle", command=self._triangle_fields)

        # add button to button widgets
        self.buttons.append(button)

        # draw button
        self.canvas.create_window(self.x_value_for_widgets,
                                  self.y_value_for_widgets + 40, window=button)

    def _draw_triangle_button(self) -> None:
        """Button for triggering draw_triangle function; drawing a triangle."""
        button = tk.Button(self.window, text="Draw",
                           command=self.draw_triangle)

        # keep track of this button
        self.buttons.append(button)

        self.canvas.create_window(self.x_value_for_widgets - 100, self.y_value_for_widgets, window=button)

    def draw_triangle(self) -> None:
        """Draw a triangle using dimensions provided by user."""
        # first point
        x1 = int(self.x1_y1.get().split(',')[0])
        y1 = int(self.x1_y1.get().split(',')[1])

        # second point
        x2 = int(self.x2_y2.get().split(',')[0])
        y2 = int(self.x2_y2.get().split(',')[1])

        # third point
        x3 = int(self.x3_y3.get().split(',')[0])
        y3 = int(self.x3_y3.get().split(',')[1])

        print(f"Drawing Triangle: {x1,y1}, {x2,y2}, {x3,y3}. Color: {self.color}.")

        # draw polygon
        new_drawing = self.canvas.create_polygon([x1, y1, x2, y2, x3, y3],
                                                 outline=self.color,
                                                 fill=self.color)

        # add this to the list of drawings
        self.drawings.append(new_drawing)

    def _triangle_fields(self) -> None:
        """Fields where user will specify dimensions for a triangle to be drawn.
        IMPORTANT:
        for one point both x and y coordinates should be provided
        together in one field. They should be separated by a comma with no gap,
        as follows: "43,53"
        """
        fields = self._fields('X1,Y1:', 'X2,Y2:', 'X3,Y3:', 'Draw Triangle')

        # draw triangle
        self._draw_triangle_button()

        # assign values
        self.x1_y1 = fields[0]
        self.x2_y2 = fields[1]
        self.x3_y3 = fields[2]


class Rectangle(Engine2D):
    """Draw rectangles."""
    def __init__(self):
        super().__init__()

        # display draw circle button
        self._open_rectangle_fields_button()

        # drawing coordinates and parameters
        self.x1_y1 = None
        self.x2_y2 = None

    def _open_rectangle_fields_button(self) -> None:
        """Button for displaying fields that are needed to specify dimensions for a rectangle."""
        button = tk.Button(self.window, text="draw rectangle", command=self._rectangle_fields)

        # add button to list of button widgets
        self.buttons.append(button)

        # draw widget
        self.canvas.create_window(self.x_value_for_widgets,
                                  self.y_value_for_widgets - 40, window=button)

    def _draw_rectangle_button(self) -> None:
        """Button for triggering draw_rectangle function; drawing a rectangle."""
        button = tk.Button(self.window, text="Draw",
                           command=self.draw_rectangle)

        # keep track of this button
        self.buttons.append(button)

        self.canvas.create_window(self.x_value_for_widgets - 100, self.y_value_for_widgets, window=button)

    def draw_rectangle(self) -> None:
        """Draw a rectangle using dimensions provided by user."""
        # first point
        x1 = int(self.x1_y1.get().split(',')[0])
        y1 = int(self.x1_y1.get().split(',')[1])

        # second point
        x2 = int(self.x2_y2.get().split(',')[0])
        y2 = int(self.x2_y2.get().split(',')[1])

        print(f"Drawing Rectangle: {x1, y1}, {x2, y2}. Color: {self.color}.")

        new_drawing = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color)

        # add this to the list of drawings
        self.drawings.append(new_drawing)

    def _rectangle_fields(self) -> None:
        """Fields where user will specify dimensions for a rectangle to be drawn.
        IMPORTANT:
        for one point both x and y coordinates should be provided
        together in one field. They should be separated by a comma with no gap,
        as follows: "43,53"

        The bottom field is not used in this case.
        """
        fields = self._fields('X1,Y1:', 'X2,Y2:', 'NA', 'Draw Rectangle')

        # draw circle
        self._draw_rectangle_button()

        # assign values
        self.x1_y1 = fields[0]
        self.x2_y2 = fields[1]


class DrawShapes(Circle, Triangle, Rectangle):
    """Bring all pieces of the program together."""
    def __init__(self):
        super().__init__()

        self._list_of_options_button()

    def _list_of_options_button(self) -> None:
        """Button for returning to 'menu' """
        button = tk.Button(self.window, text="List of Options",
                           command=self.back_to_list_of_options)

        self.canvas.create_window(self.x_value_for_widgets + 370, self.y_value_for_widgets - 40, window=button)

    def back_to_list_of_options(self) -> None:
        """Remove all fields and buttons.
        Basically return to 'state 1', where you can choose what
        shape you want to draw."""
        for widget in self.fields_and_labels:
            self.delete_widget(widget)

        for button in self.buttons:
            self.delete_widget(button)

        self._open_circle_fields_button()
        self._open_triangle_fields_button()
        self._open_rectangle_fields_button()
