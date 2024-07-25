# Creating a QR Code Generator

# First install qrcode module from powershell using pip

import qrcode
features = qrcode.QRCode(version=1, box_size=20, border=3)

# Write any website or URL name below to create it's QR Code

my_qr = qrcode.make("https://www.youtube.com/")

my_qr.save("my_qr.png")
