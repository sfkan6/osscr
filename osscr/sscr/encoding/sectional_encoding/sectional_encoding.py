from .line_encoding import LineEncoder
from .line_sectionalization import LineSectioner
from .conjunction_of_line_codes import ConjunctorOfLineCodes


class SectionalEncoder:
    def __init__(self, section_ratios, threshold_number_of_pixels):
        self.line_sectioner = LineSectioner(section_ratios)
        self.line_encoder = LineEncoder(threshold_number_of_pixels)
        self.conjunctor_of_line_codes = ConjunctorOfLineCodes()

    def set_threshold_number_of_pixels(self, threshold_number_of_pixels):
        self.line_encoder = LineEncoder(threshold_number_of_pixels)

    def get_conjunction_code_by_lines(self, lines):
        line_codes = self.get_codes_by_lines(lines)
        return self.conjunctor_of_line_codes.get_conjunction_line_code_by_line_codes(
            line_codes
        )

    def get_codes_by_lines(self, lines):
        return [self.get_code_by_line(line) for line in lines]

    def get_code_by_line(self, line):
        sections = self.line_sectioner.get_sections_by_line(line)
        section_codes = self.line_encoder.get_codes_by_lines(sections)
        return "".join(section_codes)
