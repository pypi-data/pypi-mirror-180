from PIL import Image
import numpy as np
import cv2

def Canny_Deriche_edge_detection(img_name):
    # Read the image
    img = Image.open(img_name)

    # Convert the image to grayscale
    gray = img.convert('L')

    # Apply the Canny-Deriche edge detector
    edges = np.zeros(gray.size)
    for i in range(1, gray.size[0]-1):
        for j in range(1, gray.size[1]-1):
            dx = int(gray.getpixel((i, j+1))) - int(gray.getpixel((i+1, j)))
            dy = int(gray.getpixel((i, j+1))) - int(gray.getpixel((i, j)))
            edges[i,j] = np.sqrt(dx*dx + dy*dy)

    # Rotate the array by 90 degrees
    edges = np.rot90(edges, k=3)

    # Convert the array to an image
    new_img = Image.fromarray(edges)

    return new_img



def frei_chen(img_name):
    # Read the image
    img = cv2.imread(img_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Define the Frei-Chen operators
    fc_x = np.array([[-1, 0, 1], [-np.sqrt(2), 0, np.sqrt(2)], [-1, 0, 1]])
    fc_y = np.array([[-1, -np.sqrt(2), -1], [0, 0, 0], [1, np.sqrt(2), 1]])

    # Apply the Frei-Chen edge detector
    edges_x = cv2.filter2D(gray, cv2.CV_64F, fc_x)
    edges_y = cv2.filter2D(gray, cv2.CV_64F, fc_y)
    edges = np.sqrt(np.square(edges_x) + np.square(edges_y))

    return edges


def log_edge_detection(img_name):
    # Read the image
    img = cv2.imread(img_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Log edge detector
    edges = cv2.Laplacian(gray, cv2.CV_64F, ksize=5)

    return edges



def prewitt_edge_detection(img_name):
    # Read the image
    img = cv2.imread(img_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Prewitt edge detector
    edges_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    edges_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges = np.sqrt(np.square(edges_x) + np.square(edges_y))

    return edges

# Test the function
def canny_edge_detection(img_name):
    # Read the image
    img = cv2.imread(img_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    return edges

def sobel_edge_detection(img_name):
    # Read the image
    img = cv2.imread(img_name)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection
    edges = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)

    return edges


class EdgeDetector:
    def __init__(self, img_name):
        # Read the image
        self.img = cv2.imread(img_name)

        # Convert the image to grayscale
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def detect_edges_prewitt(self,ksize=3):
        # Apply the Prewitt edge detector
        edges_x = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=ksize)
        edges_y = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=ksize)
        edges = np.sqrt(np.square(edges_x) + np.square(edges_y))
        return edges

    def detect_edges_canny(self):
        # Apply Canny edge detection
        edges = cv2.Canny(self.gray, 100, 200)
        return edges

    def detect_edges_sobel(self,ksize=5):
        # Apply Sobel edge detection
        edges = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=ksize)
        return edges
    
    def detect_edges_log(self,ksize=5):
        # Apply the Log edge detector
        edges = cv2.Laplacian(self.gray, cv2.CV_64F, ksize=ksize)
        return edges
    
    def detect_edges_frei_chen(self):
        # Define the Frei-Chen operators
        fc_x = np.array([[-1, 0, 1], [-np.sqrt(2), 0, np.sqrt(2)], [-1, 0, 1]])
        fc_y = np.array([[-1, -np.sqrt(2), -1], [0, 0, 0], [1, np.sqrt(2), 1]])

        # Apply the Frei-Chen edge detector
        edges_x = cv2.filter2D(self.gray, cv2.CV_64F, fc_x)
        edges_y = cv2.filter2D(self.gray, cv2.CV_64F, fc_y)
        edges = np.sqrt(np.square(edges_x) + np.square(edges_y))
        return edges

        return edges
    def detect_edges_laplacian(self):
        # Apply Laplacian edge detection
        edges = cv2.Laplacian(self.gray, cv2.CV_64F)
        return edges

    def detect_edges_canny_deriche(self):
        # Apply the Canny-Deriche edge detector
        edges = np.zeros(self.gray.size)
        for i in range(1, self.gray.size[0]-1):
            for j in range(1, self.gray.size[1]-1):
                dx = int(self.gray.getpixel((i, j+1))) - int(self.gray.getpixel((i+1, j)))
                dy = int(self.gray.getpixel((i, j+1))) - int(self.gray.getpixel((i, j)))
                edges[i,j] = np.sqrt(dx*dx + dy*dy)
        edges = np.rot90(edges, k=3)
        return edges

        # Rotate the edges image

        return edges
    def detect_edges_kirsch(self):
        # Define the Kirsch operator kernels
        kirsch_kernels = [
            np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
            np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
            np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
            np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),
            np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
            np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
            np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
            np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
        ]

        # Apply the Kirsch edge detector using each of the 8 operator kernels
        edges = np.zeros(self.gray.size)
        for kernel in kirsch_kernels:
            edges += np.absolute(cv2.filter2D(self.gray, cv2.CV_64F, kernel))

        # Normalize the detected edges to the range 0-255
        min_val, max_val, _, _ = cv2.minMaxLoc(edges)
        edges = (255 * ((edges - min_val) / (max_val - min_val)))
        return edges

        return edges
    def Marr_Hildreth_edge_detector(self,ksize):
        return cv2.Laplacian(self.gray, cv2.CV_64F, ksize=ksize)

        
    def zero_crossing_detect_edges(self):
        # Convert the image to grayscale
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Apply Canny edge detection
        edges = cv2.Canny(self.gray, 100, 200)

        # Find the contours in the edge map
        _, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Approximate the contours with polygons
        polygons = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)
            polygons.append(approx)

        # Draw the polygons on the original image
        zero_crossing_edges = self.img.copy()
        cv2.drawContours(zero_crossing_edges, polygons, -1, (0, 0, 0), 3)

        return zero_crossing_edges

