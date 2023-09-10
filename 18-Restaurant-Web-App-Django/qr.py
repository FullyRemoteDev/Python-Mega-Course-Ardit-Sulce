import qrcode
import os
from dotenv import load_dotenv

load_dotenv()

app18_ip = os.getenv('APP18_WEB_APP_HOST_IP')
app18_port = 8000
app18_url = f"http://{app18_ip}:{app18_port}"
image = qrcode.make(app18_url)
image.save('qr.png')
