from .line_encoding import LineEncoder
from .line_sectionalization import LineSectioner
from .conjunction_of_line_codes import ConjunctorOfCodes


class SectionalEncoder:

    def __init__(self, section_ratios: list[int|float], number_of_thresholds: int, threshold_value: int) -> None:
        self.line_sectioner = LineSectioner(section_ratios)
        self.line_encoder = LineEncoder(number_of_thresholds, threshold_value)
        self.conjunctor_of_codes = ConjunctorOfCodes()
    
    def set_number_of_thresholds(self, number_of_thresholds: int) -> None:
        self.line_encoder.number_of_thresholds = number_of_thresholds

    def get_conjunction_code_by_lines(self, lines: list[list]) -> str:
        list_of_codes = self.get_codes_by_lines(lines)
        return self.conjunctor_of_codes.get_conjunction_codes_by_list_of_codes(list_of_codes)

    def get_codes_by_lines(self, lines: list[list]) -> list[str]:
        return [self.get_code_by_line(line) for line in lines]

    def get_code_by_line(self, line: list) -> str:
        sections = self.line_sectioner.get_sections_by_line(line)
        section_codes = self.line_encoder.get_codes_by_lines(sections)
        return "".join(section_codes)
