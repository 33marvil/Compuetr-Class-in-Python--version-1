"""code goes here"""

class Computer:

    def __init__(self, mark, type, processor):
        self.__mark = mark
        self.__type = type
        self.__processor = processor

    # getter method
    @property
    def mark(self):
        return self.__mark

    # setter
    @mark.setter
    def mark(self,mark):
        raise AttributeError #("Dell")

    # getter
    @property
    def processor(self):
        return self.__processor

    # setter
    @processor.setter
    def processor(self, processor):
        self.__processor = processor # modifica por asignación

    @property
    def type(self):
        raise AttributeError

    @type.setter
    def type(self, type):
        self.__type = type
