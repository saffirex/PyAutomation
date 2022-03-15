from PIL import Image
from io import BytesIO
import requests

r=requests.get('https://api.github.com/events')
i = Image.open(BytesIO(r.content))
