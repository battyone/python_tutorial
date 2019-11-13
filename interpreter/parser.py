# Token Types
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__(self)


class Interpreter:
    def __init__(self, text):
        # input like '3+5'
        self.text = text

        # index into text
        self.pos = 0

        self.current_token = None

    def error(self):
        raise Exception('Error parsing string')

    def get_next_token(self):
        """
        Lexical analyzer (aka scanner or tokenizer)

        Method to break strings into tokens
        """

        text = self.text
