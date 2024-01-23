

class BtnDict(dict):

    __slots__ = {
        'static path': None,
        'press path': None,
        'hover path': None,
        'width': None,
        'height': None
    }

    def __init__(self, static: str, press: str, hover, width, height):
        
        self.__slots__
