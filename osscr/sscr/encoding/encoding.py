from .sectional_encoding import SectionalEncoder
from .directional_encoding import DirectionalEncoder, HorizontalEncoder, VerticalEncoder
from .char_image import CharImage


class Encoder:

    def __init__(self, directional_encoders: list[DirectionalEncoder]) -> None:
        self.directional_encoders = directional_encoders

    def get_code_by_image(self, image: CharImage) -> str:
        codes = [
            directional_encoder.get_code_by_image(image) 
            for directional_encoder in self.directional_encoders
        ]
        return "".join(codes)


class SevenSegmentEncoder(Encoder):
    def __init__(self, horizontal_slice_locations: list[list[float]], vertical_slice_locations: list[list[float]]) -> None:
        horizontal_encoder = HorizontalEncoder(
            SectionalEncoder([1, 1], 1, 100), horizontal_slice_locations
        )
        vertical_encoder = VerticalEncoder(
            SectionalEncoder([1, 2, 1], 1, 100), vertical_slice_locations
        )
        super().__init__([horizontal_encoder, vertical_encoder])
    
    def get_code_by_image(self, image: CharImage) -> str:
        self._set_number_of_thresholds_by_height(image.height)
        return super().get_code_by_image(image)

    def _set_number_of_thresholds_by_height(self, height: int) -> None:
        number_of_thresholds = self._get_number_of_thresholds_by_height(height)
        for directional_encoder in self.directional_encoders:
            directional_encoder.set_number_of_thresholds(number_of_thresholds)

    def _get_number_of_thresholds_by_height(self, height: int|float, part_of_height=0.04) -> int:
        return max(1, int(height * part_of_height))

   

class DefaultEncoder(SevenSegmentEncoder):

    def __init__(self) -> None:
        super().__init__([[0.25], [0.75]], [[0.4, 0.55]])

