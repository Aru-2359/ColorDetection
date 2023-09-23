# Color Detection using Python with OpenCV and Pillow 🦄

## Introduction

Color Detection using Python with OpenCV and Pillow is a simple yet powerful project that allows you to identify and extract specific colors from images. Whether you're a designer, photographer, or just curious about the colors in your pictures, this project can help you analyze and manipulate color information with ease.

The project leverages two popular Python libraries:

- **OpenCV**: A powerful computer vision library that provides various tools for image processing, including color manipulation and detection.
- **Pillow**: A user-friendly Python Imaging Library that allows you to open, manipulate, and save many different image file formats.

## Features

- **Color Detection**: Detect and extract specific colors from an image by specifying their RGB values.
- **Color Visualization**: Visualize the detected color regions with bounding boxes and labels.
- **Export Results**: Save the color-detected image with bounding boxes for further analysis or sharing.

## Getting Started

Follow these steps to get started with the Color Detection project:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   ```

2. **Install Dependencies**:

   Make sure you have Python 3.x installed. Then, install the required libraries using pip:

   ```bash
   pip install opencv-python-headless pillow
   ```

3. **Run the Project**:

   ```bash
   python color_detection.py --image your_image.jpg
   ```

   Replace `your_image.jpg` with the path to the image you want to analyze.

4. **Interact with the GUI**:

   The project will open a graphical user interface (GUI) where you can specify the RGB values of the color you want to detect. Click the "Detect Color" button to see the results.

## Usage

1. **Specify RGB Values**:

   Enter the RGB values of the color you want to detect in the input fields provided in the GUI.

2. **Detect Color**:

   Click the "Detect Color" button to process the image and highlight regions that match the specified color.

3. **Save Results**:

   To save the color-detected image with bounding boxes and labels, click the "Save Image" button. The image will be saved in the project directory.


In this example, we detected the color red (RGB: 255, 0, 0) in the input image.

## Contributing

Contributions to this project are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the desire to explore computer vision and image processing techniques.
- Special thanks to the developers of OpenCV and Pillow for providing powerful tools for image analysis and manipulation.

---

Enjoy exploring and analyzing colors in your images with Color Detection using Python with OpenCV and Pillow! If you find this project useful, please consider giving it a star on GitHub and sharing it with others.
