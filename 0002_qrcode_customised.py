import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4, 
)

qr.add_data("https://www.youtube.com/@ShahbazSayyed")
qr.make(fit=True)

qr_img = qr.make_image(fill_color="white", back_color="red")

# Save image to file
qr_img.save("Shahbaz_yt.png")
