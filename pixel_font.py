class PixelFont:
    def __init__(self):
        self._height = 1
        self._font_data = {}

    def empty_data(self):
        return [""] * self._height

    def __getitem__(self, key):
        try:
            return self._font_data[key]
        except:
            try:
                return self._font_data[key.upper()]
            except:
                return self.empty_data()

    def string(self, text):
        output = self.empty_data()
        for char in text:
            pixels = self[char]
            for i in range(self._height):
                output[i] = '.'.join([p for p in (output[i], pixels[i]) if len(p) > 0])
        return output

    def show_string(self, text):
        for line in self.string(text):
            print(line)


class PixelFont5Narrow(PixelFont):
    def __init__(self):
        self._height = 5
        self._font_data = {
            # digits
            '0': [
                '.#.',
                '#.#',
                '#.#',
                '#.#',
                '.#.',
            ],
            '1': [
                '.#',
                '##',
                '.#',
                '.#',
                '.#',
            ],
            '2': [
                '##.',
                '..#',
                '.##',
                '#..',
                '###',
            ],
            '3': [
                '##.',
                '..#',
                '##.',
                '..#',
                '##.',
            ],
            '4': [
                '#.#',
                '#.#',
                '.##',
                '..#',
                '..#',
            ],
            '5': [
                '###',
                '#..',
                '##.',
                '..#',
                '##.',
            ],
            '6': [
                '.#.',
                '#..',
                '##.',
                '#.#',
                '.#.',
            ],
            '7': [
                '###',
                '..#',
                '.#.',
                '.#.',
                '.#.',
            ],
            '8': [
                '.#.',
                '#.#',
                '.#.',
                '#.#',
                '.#.',
            ],
            '9': [
                '.#.',
                '#.#',
                '.##',
                '..#',
                '.#.',
            ],

            # letters
            'A': [
                '.#.',
                '#.#',
                '###',
                '#.#',
                '#.#',
            ],
            'B': [
                '##.',
                '#.#',
                '##.',
                '#.#',
                '##.',
            ],
            'C': [
                '.##',
                '#..',
                '#..',
                '#..',
                '.##',
            ],
            'D': [
                '##.',
                '#.#',
                '#.#',
                '#.#',
                '##.',
            ],
            'E': [
                '###',
                '#..',
                '###',
                '#..',
                '###',
            ],
            'F': [
                '###',
                '#..',
                '###',
                '#..',
                '#..',
            ],
            'G': [
                '.##',
                '#..',
                '#.#',
                '#.#',
                '.##',
            ],
            'H': [
                '#.#',
                '#.#',
                '###',
                '#.#',
                '#.#',
            ],
            'I': [
                '#',
                '#',
                '#',
                '#',
                '#',
            ],
            'J': [
                '..#',
                '..#',
                '..#',
                '..#',
                '##.',
            ],
            'K': [
                '#.#',
                '#.#',
                '##.',
                '#.#',
                '#.#',
            ],
            'L': [
                '#..',
                '#..',
                '#..',
                '#..',
                '###',
            ],
            'M': [
                '#...#',
                '##.##',
                '#.#.#',
                '#...#',
                '#...#',
            ],
            'N': [
                '##.',
                '#.#',
                '#.#',
                '#.#',
                '#.#',
            ],
            'O': [
                '.#.',
                '#.#',
                '#.#',
                '#.#',
                '.#.',
            ],
            'P': [
                '##.',
                '#.#',
                '##.',
                '#..',
                '#..',
            ],
            'Q': [
                '.#.',
                '#.#',
                '#.#',
                '###',
                '.##',
            ],
            'R': [
                '##.',
                '#.#',
                '##.',
                '#.#',
                '#.#',
            ],
            'S': [
                '.##',
                '#..',
                '.#.',
                '..#',
                '##.',
            ],
            'T': [
                '###',
                '.#.',
                '.#.',
                '.#.',
                '.#.',
            ],
            'U': [
                '#.#',
                '#.#',
                '#.#',
                '#.#',
                '.##',
            ],
            'V': [
                '#.#',
                '#.#',
                '#.#',
                '#.#',
                '.#.',
            ],
            'W': [
                '#...#',
                '#...#',
                '#.#.#',
                '#.#.#',
                '.#.#.',
            ],
            'X': [
                '#.#',
                '#.#',
                '.#.',
                '#.#',
                '#.#',
            ],
            'Y': [
                '#.#',
                '#.#',
                '.#.',
                '.#.',
                '.#.',
            ],
            'Z': [
                '###',
                '..#',
                '.#.',
                '#..',
                '###',
            ],

            # symbols
            '#': [
                '.#.#.',
                '#####',
                '.#.#.',
                '#####',
                '.#.#.',
            ],
            '.': [
                '.',
                '.',
                '.',
                '.',
                '#',
            ],
            '-': [
                '...',
                '...',
                '###',
                '...',
                '...',
            ],
            ' ': [
                '...',
                '...',
                '...',
                '...',
                '...',
            ],
            ':': [
                '.',
                '#',
                '.',
                '#',
                '.',
            ],
            '!': [
                '#',
                '#',
                '#',
                '.',
                '#',
            ],
            '?': [
                '##.',
                '..#',
                '.#.',
                '...',
                '.#.',
            ],
            '(': [
                '.#',
                '#.',
                '#.',
                '#.',
                '.#',
            ],
            ')': [
                '#.',
                '.#',
                '.#',
                '.#',
                '#.',
            ],
            '[': [
                '##',
                '#.',
                '#.',
                '#.',
                '##',
            ],
            ']': [
                '##',
                '.#',
                '.#',
                '.#',
                '##',
            ],
            '<': [
                '..#',
                '.#.',
                '#..',
                '.#.',
                '..#',
            ],
            '>': [
                '#..',
                '.#.',
                '..#',
                '.#.',
                '#..',
            ],
            '+': [
                '...',
                '.#.',
                '###',
                '.#.',
                '...',
            ],
            '*': [
                '...',
                '#.#',
                '.#.',
                '#.#',
                '...',
            ],
            '/': [
                '..#',
                '..#',
                '.#.',
                '#..',
                '#..',
            ],
            '\\': [
                '#..',
                '#..',
                '.#.',
                '..#',
                '..#',
            ],
            '_': [
                '...',
                '...',
                '...',
                '...',
                '###',
            ],
            '\'': [
                '#',
                '#',
                '.',
                '.',
                '.',
            ],
            '"': [
                '#.#',
                '#.#',
                '...',
                '...',
                '...',
            ],
            ',': [
                '..',
                '..',
                '..',
                '.#',
                '#.',
            ],
            ';': [
                '..',
                '.#',
                '..',
                '.#',
                '#.',
            ],
            '|': [
                '#',
                '#',
                '.',
                '#',
                '#',
            ],
            '^': [
                '.#.',
                '#.#',
                '...',
                '...',
                '...',
            ],
            '@': [
                '.##.',
                '#..#',
                '#.#.',
                '#...',
                '.###',
            ],
        }

class PixelFont10(PixelFont):
    def __init__(self):
        self._height = 10
        self._font_data = {}
