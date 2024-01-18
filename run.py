import os
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

cloudinary.uploader.upload(
    "urutau.jpg",
    public_id="urutau",
    unique_filename=False,
    overwrite=True,
)

url_image = cloudinary.CloudinaryImage("urutau").build_url()

print(f"toma sua url: {url_image}")
