from typing import Union, Tuple
"""pixpy native module"""
from __future__ import annotations
import pixpy._pixpy
import typing
import os
import pixpy.color as color
import pixpy.event as event
import pixpy.key as key


__all__ = [
    "Console",
    "Context",
    "Float2",
    "Font",
    "Image",
    "Int2",
    "Screen",
    "TileSet",
    "all_events",
    "color",
    "event",
    "get_display",
    "get_event",
    "get_pointer",
    "is_pressed",
    "key",
    "load_font",
    "load_png",
    "open_display",
    "rgba",
    "run_loop",
    "save_png",
    "was_pressed"
]


class Console():
    def __init__(self, cols: int = 80, rows: int = 50, font_file: str = '', tile_size:Union[Float2, Tuple[float,float]] = Int2(0, 0), font_size: int = 16) -> None: ...
    def cancel_line(self) -> None: 
        """
        Stop line edit mode
        """
    def clear(self) -> None: ...
    def get(self, arg0:Union[Int2, Tuple[int, int]]) -> int: 
        """
        Get char at position
        """
    def get_font_image(self) -> Image: ...
    def get_image_for(self, tile: int) -> Image: ...
    def get_line(self) -> None: 
        """
        Enter line edit mode
        """
    def get_tiles(self) -> typing.List[int]: ...
    def put(self, pos:Union[Int2, Tuple[int, int]], tile: int) -> None: 
        """
        Put char at position
        """
    def read_line(self) -> None: 
        """
        Enter line edit mode
        """
    def render(self, context: Context, pos:Union[Float2, Tuple[float,float]] = Float2(0.000000, 0.000000), size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000)) -> None: 
        """
        Render the console to the display
        """
    def set_color(self, arg0: int, arg1: int) -> None: ...
    def set_line(self, arg0: str) -> None: 
        """
        Change the edited line
        """
    def set_tiles(self, tiles: typing.List[int]) -> None: ...
    @typing.overload
    def write(self, text: str) -> None: ...
    @typing.overload
    def write(self, tiles: typing.List[str]) -> None: ...
    @property
    def cursor_on(self) -> bool:
        """
        :type: bool
        """
    @cursor_on.setter
    def cursor_on(self, arg0: bool) -> None:
        pass
    @property
    def cursor_pos(self) -> Int2:
        """
        :type:Union[Int2, Tuple[int, int]]
        """
    @cursor_pos.setter
    def cursor_pos(self, arg1:Union[Int2, Tuple[int, int]]) -> None:
        pass
    @property
    def grid_size(self) -> Int2:
        """
        Get number cols and rows

        :type:Union[Int2, Tuple[int, int]]
        """
    @property
    def tile_size(self) -> Int2:
        """
        Get size of a single tile

        :type:Union[Int2, Tuple[int, int]]
        """
    pass
class Context():
    def __init__(self, size:Union[Float2, Tuple[float,float]] = Float2(0.000000, 0.000000)) -> None: ...
    def circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def clear(self, color: int = 0) -> None: ...
    @typing.overload
    def draw(self, drawable: Console, top_left:Union[Float2, Tuple[float,float]] = Float2(0.000000, 0.000000), size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000)) -> None: ...
    @typing.overload
    def draw(self, image: Image, top_left: typing.Optional[Float2] = None, center: typing.Optional[Float2] = None, size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000), rot: float = 0) -> None: ...
    def filled_circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def filled_rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, end:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, start:Union[Float2, Tuple[float,float]], end:Union[Float2, Tuple[float,float]]) -> None: ...
    def plot(self, center:Union[Float2, Tuple[float,float]], color: int) -> None: ...
    def rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    @property
    def context(self) -> Context:
        """
        :type: Context
        """
    @property
    def draw_color(self) -> int:
        """
        :type: int
        """
    @draw_color.setter
    def draw_color(self, arg1: int) -> None:
        pass
    @property
    def line_width(self) -> float:
        """
        :type: float
        """
    @line_width.setter
    def line_width(self, arg1: float) -> None:
        pass
    pass
class Float2():
    @typing.overload
    def __add__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __add__(self, arg0:Union[Int2, Tuple[int, int]]) -> Float2: ...
    @typing.overload
    def __add__(self, arg0: float) -> Float2: ...
    def __eq__(self, arg0:Union[Float2, Tuple[float,float]]) -> bool: ...
    @typing.overload
    def __floordiv__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __floordiv__(self, arg0:Union[Int2, Tuple[int, int]]) -> Float2: ...
    @typing.overload
    def __floordiv__(self, arg0: float) -> Float2: ...
    def __getitem__(self, arg0: int) -> float: ...
    @typing.overload
    def __init__(self, arg0: typing.Tuple[float, float]) -> None: ...
    @typing.overload
    def __init__(self, x: float = 0, y: float = 0) -> None: ...
    @typing.overload
    def __init__(self, x: float = 0, y: int = 0) -> None: ...
    @typing.overload
    def __init__(self, x: int = 0, y: float = 0) -> None: ...
    @typing.overload
    def __init__(self, x: int = 0, y: int = 0) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __mul__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __mul__(self, arg0:Union[Int2, Tuple[int, int]]) -> Float2: ...
    @typing.overload
    def __mul__(self, arg0: float) -> Float2: ...
    def __ne__(self, arg0:Union[Float2, Tuple[float,float]]) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __sub__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __sub__(self, arg0:Union[Int2, Tuple[int, int]]) -> Float2: ...
    @typing.overload
    def __sub__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __truediv__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __truediv__(self, arg0:Union[Int2, Tuple[int, int]]) -> Float2: ...
    @typing.overload
    def __truediv__(self, arg0: float) -> Float2: ...
    def angle(self) -> float: 
        """
        Get the angle between the vector and (1,0).
        """
    def clamp(self, low:Union[Float2, Tuple[float,float]], high:Union[Float2, Tuple[float,float]]) -> Float2: 
        """
        Separately clamp the x and y component between the corresponding components in the given arguments.
        """
    def clip(self, low:Union[Float2, Tuple[float,float]], high:Union[Float2, Tuple[float,float]]) -> Float2: ...
    def cossin(self) -> Float2: ...
    @staticmethod
    def from_angle(arg0: float) -> Float2: 
        """
        From angle
        """
    def mag(self) -> float: 
        """
        Get magnitude (length) of vector
        """
    def mag2(self) -> float: 
        """
        Get the squared magnitude
        """
    def norm(self) -> Float2: 
        """
        Get the normalized vector.
        """
    def sign(self) -> Float2: ...
    def toi(self) -> Int2: 
        """
        Convert a `Float2` to an `Int2`
        """
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @property
    def y(self) -> float:
        """
        :type: float
        """
    ONE: Float2 # value = Float2(1.000000, 1.000000)
    ZERO: Float2 # value = Float2(0.000000, 0.000000)
    __hash__ = None
    pass
class Font():
    def make_image(self, text: str, size: int, color: int = 4294967295) -> Image: ...
    UNSCII_FONT: Font
    pass
class Image():
    @typing.overload
    def __init__(self, size:Union[Float2, Tuple[float,float]]) -> None: 
        """
        Splits the image into as many _width_ * _height_ images as possible, first going left to right, then top to bottom.
        """
    @typing.overload
    def __init__(self, width: int, height: int) -> None: ...
    @typing.overload
    def __init__(self, width: int, pixels: typing.List[int]) -> None: ...
    def bind(self, unit: int = 0) -> None: ...
    def circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def clear(self, color: int = 0) -> None: ...
    def copy_from(self, image: Image) -> None: ...
    def copy_to(self, image: Image) -> None: ...
    @typing.overload
    def draw(self, drawable: Console, top_left:Union[Float2, Tuple[float,float]] = Float2(0.000000, 0.000000), size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000)) -> None: ...
    @typing.overload
    def draw(self, image: Image, top_left: typing.Optional[Float2] = None, center: typing.Optional[Float2] = None, size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000), rot: float = 0) -> None: ...
    def filled_circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def filled_rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, end:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, start:Union[Float2, Tuple[float,float]], end:Union[Float2, Tuple[float,float]]) -> None: ...
    def plot(self, center:Union[Float2, Tuple[float,float]], color: int) -> None: ...
    def rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    def set_as_target(self) -> None: ...
    @typing.overload
    def split(self, cols: int = -1, rows: int = -1, width: int = 8, height: int = 8) -> typing.List[Image]: 
        """
        Splits the image into as many _width_ * _height_ images as possible, first going left to right, then top to bottom.
        """
    @typing.overload
    def split(self, size:Union[Float2, Tuple[float,float]]) -> typing.List[Image]: ...
    @property
    def context(self) -> Context:
        """
        :type: Context
        """
    @property
    def draw_color(self) -> int:
        """
        :type: int
        """
    @draw_color.setter
    def draw_color(self, arg1: int) -> None:
        pass
    @property
    def height(self) -> float:
        """
        :type: float
        """
    @property
    def line_width(self) -> float:
        """
        :type: float
        """
    @line_width.setter
    def line_width(self, arg1: float) -> None:
        pass
    @property
    def pos(self) -> Float2:
        """
        :type:Union[Float2, Tuple[float,float]]
        """
    @property
    def size(self) -> Float2:
        """
        :type:Union[Float2, Tuple[float,float]]
        """
    @property
    def width(self) -> float:
        """
        :type: float
        """
    pass
class Int2():
    @typing.overload
    def __add__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __add__(self, arg0:Union[Int2, Tuple[int, int]]) -> Int2: ...
    @typing.overload
    def __add__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __add__(self, arg0: int) -> Int2: ...
    def __eq__(self, arg0:Union[Int2, Tuple[int, int]]) -> bool: ...
    @typing.overload
    def __floordiv__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __floordiv__(self, arg0:Union[Int2, Tuple[int, int]]) -> Int2: ...
    @typing.overload
    def __floordiv__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __floordiv__(self, arg0: int) -> Int2: ...
    def __getitem__(self, arg0: int) -> int: ...
    @typing.overload
    def __init__(self, arg0: typing.Tuple[int, int]) -> None: ...
    @typing.overload
    def __init__(self, x: float = 0, y: float = 0) -> None: ...
    @typing.overload
    def __init__(self, x: float = 0, y: int = 0) -> None: ...
    @typing.overload
    def __init__(self, x: int = 0, y: float = 0) -> None: ...
    @typing.overload
    def __init__(self, x: int = 0, y: int = 0) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __mul__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __mul__(self, arg0:Union[Int2, Tuple[int, int]]) -> Int2: ...
    @typing.overload
    def __mul__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __mul__(self, arg0: int) -> Int2: ...
    def __ne__(self, arg0:Union[Int2, Tuple[int, int]]) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __sub__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __sub__(self, arg0:Union[Int2, Tuple[int, int]]) -> Int2: ...
    @typing.overload
    def __sub__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __sub__(self, arg0: int) -> Int2: ...
    @typing.overload
    def __truediv__(self, arg0:Union[Float2, Tuple[float,float]]) -> Float2: ...
    @typing.overload
    def __truediv__(self, arg0:Union[Int2, Tuple[int, int]]) -> Int2: ...
    @typing.overload
    def __truediv__(self, arg0: float) -> Float2: ...
    @typing.overload
    def __truediv__(self, arg0: int) -> Int2: ...
    def clamp(self, low:Union[Int2, Tuple[int, int]], high:Union[Int2, Tuple[int, int]]) -> Int2: ...
    def sign(self) -> Int2: ...
    def tof(self) -> Float2: 
        """
        Convert a `Int2` to an `Float2`. Convenience function, since it converts automatically.
        """
    @property
    def x(self) -> int:
        """
        :type: int
        """
    @property
    def y(self) -> int:
        """
        :type: int
        """
    ONE: Int2 # value = Int2(1, 1)
    ZERO: Int2 # value = Int2(0, 0)
    __hash__ = None
    pass
class Screen():
    def circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def clear(self, color: int = 0) -> None: ...
    @typing.overload
    def draw(self, drawable: Console, top_left:Union[Float2, Tuple[float,float]] = Float2(0.000000, 0.000000), size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000)) -> None: ...
    @typing.overload
    def draw(self, image: Image, top_left: typing.Optional[Float2] = None, center: typing.Optional[Float2] = None, size:Union[Float2, Tuple[float,float]] = Float2(-1.000000, -1.000000), rot: float = 0) -> None: ...
    def filled_circle(self, center:Union[Float2, Tuple[float,float]], radius: float) -> None: ...
    def filled_rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, end:Union[Float2, Tuple[float,float]]) -> None: ...
    @typing.overload
    def line(self, start:Union[Float2, Tuple[float,float]], end:Union[Float2, Tuple[float,float]]) -> None: ...
    def plot(self, center:Union[Float2, Tuple[float,float]], color: int) -> None: ...
    def rect(self, top_left:Union[Float2, Tuple[float,float]], size:Union[Float2, Tuple[float,float]]) -> None: ...
    def set_as_target(self) -> None: ...
    def swap(self) -> None: 
        """
        Synchronize with the frame rate of the display and swap buffers. This is normally the last thing you do in your render loop.
        """
    @property
    def context(self) -> Context:
        """
        :type: Context
        """
    @property
    def draw_color(self) -> int:
        """
        :type: int
        """
    @draw_color.setter
    def draw_color(self, arg1: int) -> None:
        pass
    @property
    def frame_counter(self) -> int:
        """
        :type: int
        """
    @property
    def height(self) -> int:
        """
        :type: int
        """
    @property
    def line_width(self) -> float:
        """
        :type: float
        """
    @line_width.setter
    def line_width(self, arg1: float) -> None:
        pass
    @property
    def size(self) -> Int2:
        """
        :type:Union[Int2, Tuple[int, int]]
        """
    @property
    def width(self) -> int:
        """
        :type: int
        """
    pass
class TileSet():
    @typing.overload
    def __init__(self, font_file: str, size: int) -> None: ...
    @typing.overload
    def __init__(self, tile_size:Union[Float2, Tuple[float,float]]) -> None: ...
    def get_image_for(self, arg0: str) -> Image: ...
    pass
def all_events() -> typing.List[typing.Union[event.NoEvent, event.Key, event.Move, event.Click, event.Text, event.Resize, event.Quit]]:
    """
    Return a list of all pending events.
    """
def get_display() -> Screen:
    pass
def get_event() -> typing.Union[event.NoEvent, event.Key, event.Move, event.Click, event.Text, event.Resize, event.Quit]:
    """
    Get the next event. Returns _NoEvent_ when there are no more events.
    """
def get_pointer() -> Float2:
    """
    Get the xy coordinate of the mouse pointer (in screen space).
    """
def is_pressed(key: typing.Union[int, str]) -> bool:
    """
    Returns _True_ if the keyboard or mouse key is held down.
    """
def load_font(name: str, size: int = 0) -> Font:
    """
    Load a TTF font
    """
def load_png(file_name: str) -> Image:
    """
    Create an _Image_ from a png file on disk.
    """
@typing.overload
def open_display(size:Union[Int2, Tuple[int, int]], full_screen: bool = False) -> Screen:
    """
    Opens a new window with the given size. This also initializes pix and is expected to have been called before any other pix calls.

    Opens a new window with the given size. This also initializes pix and is expected to have been called before any other pix calls.
    """
@typing.overload
def open_display(width: int = -1, height: int = -1, full_screen: bool = False) -> Screen:
    pass
def rgba(red: float, green: float, blue: float, alpha: float) -> int:
    """
    Combine four color components into a color.
    """
def run_loop() -> bool:
    """
    Should be called first in your main rendering loop. Clears all pending events and all pressed keys. Returns _True_ as long as the application is running (the user has not closed the window or quit in some other way
    """
def save_png(image: Image, file_name: str) -> None:
    """
    Save an _Image_ to disk
    """
def was_pressed(key: typing.Union[int, str]) -> bool:
    """
    Returns _True_ if the keyboard or mouse key was pressed this loop. `run_loop()` refreshes these states.
    """
