class ConjunctorOfLineCodes:
    def get_conjunction_line_code_by_line_codes(self, line_codes):
        conjunction_line_code = []
        for row in range(len(line_codes[0])):
            row_codes = [line_code[row] for line_code in line_codes]
            conjunction_line_code.append(self.get_conjunction_code_by_codes(row_codes))
        return "".join(conjunction_line_code)

    def get_conjunction_code_by_codes(self, codes):
        if "0" not in codes and None not in codes:
            return "1"
        return "0"
