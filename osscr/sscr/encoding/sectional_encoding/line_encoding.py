class LineEncoder:
    def __init__(self, threshold_number_of_pixels: int, threshold_value: int = 100):
        self.threshold_number_of_pixels = threshold_number_of_pixels
        self.threshold_value = threshold_value

    def get_codes_by_lines(self, lines):
        return [self.get_code_by_line(line) for line in lines]

    def get_code_by_line(self, line):
        max_in_row = 0
        count = 0

        for pixel_value in line:
            if pixel_value >= self.threshold_value:
                count += 1
            else:
                max_in_row = max(max_in_row, count)
                count = 0

        if max(max_in_row, count) > self.threshold_number_of_pixels:
            return "1"
        return "0"
