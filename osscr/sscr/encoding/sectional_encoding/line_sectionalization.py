
class LineSectioner:

    def __init__(self, section_ratios: list) -> None:
        self.section_ratios = section_ratios
        self.number_of_sections = len(self.section_ratios)
        self.number_of_parts = sum(self.section_ratios)

    def get_sections_by_line(self, line: list) -> list[list]:
        edges_of_sections = self.get_edges_of_sections_by_line_len(len(line))
        return [
            line[edges_of_sections[i] : edges_of_sections[i + 1]]
            for i in range(self.number_of_sections)
        ]

    def get_edges_of_sections_by_line_len(self, line_len: int) -> list[int]:
        size_part = int(line_len // self.number_of_parts)
        edges_of_sections = [
            size_part * sum(self.section_ratios[0:i])
            for i in range(self.number_of_sections)
        ]
        return edges_of_sections + [line_len]
