# Image-Resizer-Tool


Live Demo: [https://image-resizer-tool-pqunn8cmshaj4pg6viwpfy.streamlit.app/]
(https://image-resizer-tool-pqunn8cmshaj4pg6viwpfy.streamlit.app/)

---

## Overview

The **Image Resizer Tool** is a streamlined web application built with Streamlit that empowers users to upload images and resize them precisely by specifying custom pixel dimensions. It provides a side-by-side preview of the original and resized images at their true pixel sizes, ensuring clear visual comparison without distortion or automatic scaling.

---

## Key Features

- **Flexible Image Upload:** Accepts common image formats (JPG, JPEG, PNG, WEBP) with large file size support (up to 200MB).  
- **Accurate Resizing:** Users can define exact width and height values for resizing images.  
- **True Dimension Preview:** Utilizes embedded HTML with base64 encoding to display images at real pixel dimensions inside scrollable containers, preserving aspect ratios and preventing automatic scaling issues.  
- **Side-by-Side Comparison:** Facilitates intuitive visual comparison between original and resized images.  
- **Downloadable Output:** Provides an option to download the resized image in PNG format seamlessly.

---

## Implementation Highlights

- Developed using **Streamlit** for rapid and interactive UI creation.  
- Image manipulation powered by the **Pillow (PIL)** library to ensure reliable and efficient resizing.  
- Custom HTML/CSS embedding enables precise control over image rendering and layout, overcoming limitations of default Streamlit image scaling behavior.  
- Designed for usability and responsiveness, handling various image sizes and formats gracefully.

---

## Getting Started

To run the project locally:

1. **Install required packages:**

```bash
pip install streamlit pillow

2.streamlit run app.py

3.Access the app: Open your browser and navigate to http://localhost:8501
