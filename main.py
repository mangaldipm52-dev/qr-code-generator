import qrcode

url = input("Enter Your URL: ").strip()
filename = input("Enter file name: ").strip()

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{filename}.png")

print("QR Code created successfully!")


