import streamlit as st
from PIL import Image
import io
import zipfile

st.set_page_config(page_title="📸 Image Resizer Tool", layout="wide")
st.title("📸 Image Resizer Tool")

# Upload images
uploaded_files = st.file_uploader(
    "Upload images",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True
)

# Resize settings
col1, col2, col3 = st.columns(3)
with col1:
    width = st.number_input("Width (px)", min_value=1, value=800)
with col2:
    height = st.number_input("Height (px)", min_value=1, value=600)
with col3:
    maintain_aspect = st.checkbox("Maintain aspect ratio", value=True)

if uploaded_files:
    resized_images = []

    for file in uploaded_files:
        # Load original
        original_image = Image.open(file)
        resized_image = original_image.copy()

        if maintain_aspect:
            # Calculate aspect-preserving size
            w_percent = width / float(resized_image.size[0])
            new_height = int(float(resized_image.size[1]) * w_percent)
            resized_image = resized_image.resize((width, new_height), Image.LANCZOS)
        else:
            resized_image = resized_image.resize((width, height), Image.LANCZOS)

        # Preview
        st.markdown(f"### {file.name}")
        col_a, col_b = st.columns(2)
        with col_a:
            st.image(original_image, caption=f"Original ({original_image.size[0]}x{original_image.size[1]})", use_container_width=True)
        with col_b:
            st.image(resized_image, caption=f"Resized ({resized_image.size[0]}x{resized_image.size[1]})", use_container_width=True)

        # Save resized for download
        img_byte_arr = io.BytesIO()
        resized_image.save(img_byte_arr, format=original_image.format)
        img_byte_arr.seek(0)
        resized_images.append((file.name, img_byte_arr))

    # ZIP download
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for filename, img_data in resized_images:
            zip_file.writestr(filename, img_data.read())
    zip_buffer.seek(0)

    st.download_button(
        label="📦 Download All Resized Images as ZIP",
        data=zip_buffer,
        file_name="resized_images.zip",
        mime="application/zip"
    )
