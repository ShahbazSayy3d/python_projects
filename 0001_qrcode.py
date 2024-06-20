#pip install qrcode
import qrcode as qr
img = qr.make("https://www.youtube.com/@ShahbazSayyed")
img.save("shahbaz_youtube.png")

