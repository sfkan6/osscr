from .object_detection import Image, Contour, Camera
from cv2.typing import MatLike
import cv2



class CV2Contour(Contour):
    def __init__(self, contour: MatLike) -> None:
        self.contour = contour

    @property
    def area(self):
        return cv2.contourArea(self.contour)

    @property
    def bounding_rect(self):
        return cv2.boundingRect(self.contour)


class CV2Image(Image):
    def __init__(self, image: MatLike) -> None:
        self.image = image
    
    @property
    def height(self) -> int:
        return self.shape[0]
     
    @property
    def width(self) -> int:
        return self.shape[1]

    @property
    def shape(self):
        return self.image.shape

    def copy(self):
        return Image(self.image.copy())
   
    def write(self, path) -> None:
        cv2.imwrite(path, self.image)

    @classmethod
    def read(cls, path) -> Image:
        return cls(cv2.imread(path))


class DeadVideoCapture:

    def __init__(self) -> None:
        pass

    def isOpened(self):
        return False

    def read(self):
        return 1, []


class CV2Camera(Camera):

    def __init__(self, path=0, debug=False) -> None:
        video_capture = DeadVideoCapture()
        if not debug:
            video_capture = cv2.VideoCapture(path)

        self.camera = video_capture

    @property
    def is_connected(self) -> bool:
        return self.camera.isOpened()

    def get_image(self) -> Image:
        success, frame = self.camera.read()
        return CV2Image(frame)

    def frame_to_bytes(self, image: Image) -> bytes:
        ret, buffer = cv2.imencode('.jpg', image.image)
        return buffer.tobytes()

