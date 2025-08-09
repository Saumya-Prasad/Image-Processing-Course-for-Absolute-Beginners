
## 📘 `README.md` for `Experiment_3` – **Power Law Transformation & Contrast Enhancement**

````markdown
# ⚡ Experiment 3: Power Law Transformation & Contrast Stretching

This experiment focuses on two fundamental **point processing techniques** used to enhance images:
1. **Power Law (Gamma) Transformation**
2. **Contrast Stretching**

Both techniques help in **improving visibility** and **extracting features** from underexposed or low-contrast images.

---

## 🎯 Objective

- Apply **Power Law Transformation** with different γ (gamma) values.
- Apply **Contrast Stretching** using a custom transformation function.
- Observe how each method enhances the image.
- Compare results and comment on performance.

---

## 📂 Files

- `Experiment_3.ipynb`: Main code notebook
- `dark.png`: Sample low contrast image used in the notebook

---

## 🧠 Concepts Explained

---

### 🔹 1. Importing Libraries

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
````

* `cv2`: For image loading and processing
* `numpy`: For numerical operations
* `matplotlib.pyplot`: For plotting images

---

### 🔹 2. Power Law Transformation (Gamma Correction)

```python
img = cv2.imread("dark.png")
gamma = [0.1, 0.2, 0.4, 0.67, 1.0, 1.5, 2.5]
for g in gamma:
    gamma_corrected = np.array(255 * (img / 255) ** g, dtype='uint8')
    plt.imshow(gamma_corrected)
    plt.title("Gamma = " + str(g))
    plt.show()
```

* `img / 255`: Normalizes pixel values between 0 and 1.
* `** g`: Applies the power-law exponent (`gamma`).
* `* 255`: Scales back to 8-bit range.
* `dtype='uint8'`: Converts float output to 8-bit image.
* Low γ (<1): Brightens image.
* High γ (>1): Darkens image.

✅ **Purpose:** Enhancing details in dark or bright regions.

---

### 🔹 3. Contrast Stretching

```python
img = cv2.imread("dark.png", 0)
def contrast_stretching(img):
    minmax_img = np.zeros(img.shape, dtype='uint8')
    min_val = np.min(img)
    max_val = np.max(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            minmax_img[i, j] = 255 * (img[i, j] - min_val) / (max_val - min_val)
    return minmax_img

out = contrast_stretching(img)
plt.imshow(out, cmap='gray')
plt.title("Contrast Stretched Image")
plt.show()
```

* Converts image to grayscale.
* Finds `min_val` and `max_val` from the image.
* Linearly stretches intensity values to the full range \[0, 255].
* Improves contrast in low dynamic range images.

✅ **Purpose:** Expands dynamic range to reveal more detail.

---

## 📊 Observations

| Method                  | Effect                           | Ideal Use Case                |
| ----------------------- | -------------------------------- | ----------------------------- |
| **Gamma Correction**    | Non-linear brightening/darkening | Adjusting mid-tone visibility |
| **Contrast Stretching** | Linear contrast expansion        | Low-contrast images           |

* Gamma < 1: Brightens dark regions.
* Gamma > 1: Darkens bright regions.
* Contrast Stretching: Best for uniformly dull images.

---

## 🧪 Experiment Result Summary

* **Power law** lets you tweak image brightness non-linearly, depending on gamma.
* **Contrast stretching** enhances detail without altering original shapes or structures.
* Both methods **do not lose spatial information** and are safe for visual preprocessing.

---

## 📝 Conclusion

This experiment provides practical insight into how mathematical transformations can be applied to enhance real-world images. Understanding how to control brightness and contrast at the pixel level is essential before diving into more complex processing like segmentation or edge detection.

---

