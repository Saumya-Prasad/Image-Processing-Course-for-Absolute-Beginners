# Experiment 1

This experiment introduces basic image operations such as loading, displaying, converting formats, and bit-depth reduction — a process used to decrease the number of gray levels in an image.


- Load and analyze an image.
- Understand image shape and pixel intensity.
- Apply **bit depth reduction** (gray level quantization).
- Observe the effect of reducing the number of intensity levels on image quality.


## 🧰 Requirements

- Python
- NumPy
- OpenCV (`cv2`)
- Jupyter Notebook

Install with:
pip install numpy opencv-python

# Key Concepts Explained:

1) img.shape
Returns the dimensions of the image.
For example, (226, 226, 3) means:
226 rows (height)
226 columns (width)
3 channels (Red, Green, Blue)



2) img.max()
Gives the maximum pixel intensity in the image.
For 8-bit images, values range from 0 to 255.
This helps understand brightness levels and contrast.



3) Bit Depth Reduction Logic
The user inputs the number of bits (e.g., 7 bits = 128 gray levels).

bits = int(input("Enter number of bits for image: "))
maxnew = 2 ** bits
factor = (maxnew - 1) / (maxoriginal - 1)

maxoriginal = Max pixel intensity in original image.
maxnew = New number of gray levels.
factor scales original pixel values to the reduced bit depth.



4) Pixel Transformation

imgNew2 = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        imgNew2[i, j] = factor * img[i, j, 0]
        
A new image array imgNew2 is created.
Only the Red channel (img[i, j, 0]) is used.
Each pixel is transformed using the scaling factor.



5) Output

imgNew2.max()
Checks the maximum value in the transformed image to confirm that quantization has occurred.



# 📎 Files in this Folder
Image_Processing_Experiment_1.ipynb – Main code notebook
README.md – This explanation

