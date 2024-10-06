
class LineEncoder:

    def __init__(self, number_of_thresholds: int, threshold_value: int) -> None:
        self.number_of_thresholds = number_of_thresholds
        self.threshold_value = threshold_value

    def get_codes_by_lines(self, lines: list[list[int | float]]) -> list[str]:
        return [self.get_code_by_line(line) for line in lines]
    
    def get_code_by_line(self, line: list[int | float]) -> str:
        max_in_row = 0
        count = 0

        for value in line:
            if value >= self.threshold_value:
                count += 1
            else:
                max_in_row = max(max_in_row, count)
                count = 0

        if max(max_in_row, count) > self.number_of_thresholds:
            return "1"
        return "0"

