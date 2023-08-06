from enum import Enum, auto
import numpy as np


ZERO = np.array([0, 0])
LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])
UP = np.array([-1, 0])
DOWN = np.array([1, 0])


class HorizontalAlignment(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


class VerticalAlignment(Enum):
    TOP = auto()
    CENTER = auto()
    BOTTOM = auto()


def compute_text_size(strings):
    # The overall width of the text is the length of the longest line
    text_width = max(max(len(y) for y in string.split("\n")) for string in strings) if strings else 0

    # The overall height of the text is the number of lines in each string summed up
    text_height = sum(map(lambda string: len(string.split("\n")), strings))

    return np.array([text_height, text_width])


# Aligning text is different from aligning other objects, hence it has its own functions
# Need to horizontally align each text block individually, but vertically align the text as a whole
# Additionally, some text (e.g. ASCII art) needs to be aligned as a block instead of aligning each line individually
def addstr_multiline_aligned(stdscr, strings, horizontal_alignment=HorizontalAlignment.LEFT,
                             vertical_alignment=VerticalAlignment.TOP):
    # Calculates line the text should start at (i.e. the argument y for the addstr method) when aligned using the given
    # alignment
    y = align(stdscr, compute_text_size(strings), HorizontalAlignment.LEFT, vertical_alignment)[0]

    for string in strings:
        lines = string.split("\n")

        # Calculates column the text should start at (i.e. the argument x for the addstr method) when aligned using the
        # given alignment
        x = align(stdscr, compute_text_size([string]), horizontal_alignment, VerticalAlignment.TOP)[1]

        for line in lines:
            stdscr.addstr(y, x, line)
            y += 1


# Top-left corner of window
def window_min(stdscr):
    return np.array(stdscr.getbegyx())


# Size of the window - number of rows and columns in the window
def window_size(stdscr):
    return np.array(stdscr.getmaxyx())


# Bottom-right corner of window
def window_max(stdscr):
    return window_min(stdscr) + window_size(stdscr) - 1


# Output the given character at the specified positions
# Positions is expected to be a NumPy array of shape (N, 2), where N is the number of positions
# def add_chars(self, positions, char):
#     for position in positions:
#         self.stdscr.addch(position[0], position[1], char)


def align(stdscr, object_size, horizontal_alignment=HorizontalAlignment.LEFT, vertical_alignment=VerticalAlignment.TOP):
    if vertical_alignment == VerticalAlignment.BOTTOM:
        vertical_position = window_max(stdscr)[0] - object_size[0] + 1
    elif vertical_alignment == VerticalAlignment.CENTER:
        vertical_position = center(stdscr, object_size)[0]
    else:
        vertical_position = 0

    if horizontal_alignment == HorizontalAlignment.RIGHT:
        horizontal_position = window_max(stdscr)[1] - object_size[1] + 1
    elif horizontal_alignment == HorizontalAlignment.CENTER:
        horizontal_position = center(stdscr, object_size)[1]
    else:
        horizontal_position = 0

    return np.array([vertical_position, horizontal_position])


def center(stdscr, object_size):
    return window_min(stdscr) + ((window_size(stdscr) - object_size) // 2)


# Convert a 2D NumPy array into a set of tuples
# Each row in the array becomes a tuple
# def convert_to_tuple_set(array):
#     return set(map(tuple, array))


class Shape:
    def __init__(self, points):
        self.points = points

    @property
    def size(self):
        return (np.ptp(self.points, axis=0) + 1) if self.points.size != 0 else np.array([0, 0])


# TODO: Consistency with using / not using window_min instead of 0
class GameObject:
    # TODO: Allow aligning
    def __init__(self, stdscr, shape, char, position=np.array([0, 0]), velocity=np.array([0, 0])):
        self.stdscr = stdscr
        self.position = position
        self.velocity = velocity
        self.shape = shape
        self.char = char

    @property
    def next_position(self):
        return self.position + self.velocity

    def update(self):
        self.position = self.next_position

    def draw(self):
        for world_point in self.position + self.shape.points:
            self.stdscr.addch(world_point[0], world_point[1], self.char)

    def collides_with(self, other):
        self_next_world_points = self.next_position + self.shape.points
        other_next_world_points = other.next_position + other.shape.points

        return not set(tuple(x) for x in self_next_world_points)\
            .isdisjoint(set(tuple(x) for x in other_next_world_points))

    # Move the object instantaneously
    # def move(self, tran):

    # Checks whether the entire shape will be within the window, based on the *next* position
    @property
    def is_within_window(self):
        return np.all(np.array([0, 0]) <= self.next_position + self.shape.points)\
               and np.all(self.next_position + self.shape.points < window_size(self.stdscr))

    @classmethod
    def create_point(cls, stdscr, char):
        return cls(stdscr, Shape(np.array([[0, 0]])), char)

    # TODO: Potentially generalise to allow diagonal lines too (i.e. lines of any gradient)
    # TODO: Potentially could do collision check using formula instead of with rasterised points
    @classmethod
    def create_horizontal_line(cls, stdscr, length, char):
        return cls(stdscr, Shape(np.stack([
            np.zeros(length, dtype="int64"),
            np.arange(length)
        ]).T), char)

    @classmethod
    def create_vertical_line(cls, stdscr, length, char):
        return cls(stdscr, Shape(np.stack([
            np.arange(length),
            np.zeros(length, dtype="int64")
        ]).T), char)
