import cloudinary
from dotenv import load_dotenv

load_dotenv()

cloudinary.uploader.upload("usutau.jpg")
