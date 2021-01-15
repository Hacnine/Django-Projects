class FourDigitConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return str(value)  # 4 = four box d = integer


