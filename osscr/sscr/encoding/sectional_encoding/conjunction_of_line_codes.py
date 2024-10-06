
class ConjunctorOfCodes:

    def get_conjunction_codes_by_list_of_codes(self, list_of_codes: list[str | list[str]]) -> str:
        conjunction_codes = []
        for col in range(len(list_of_codes[0])):
            col_codes = [codes[col] for codes in list_of_codes]
            conjunction_codes.append(self.get_conjunction_code_by_codes(col_codes))
        return "".join(conjunction_codes)

    def get_conjunction_code_by_codes(self, codes: list|str) -> str:
        if "0" not in codes:
            return "1"
        return "0"
