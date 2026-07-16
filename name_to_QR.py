import qrcode
mess= input("enter your message: ").strip()
file_name = input("enter your file name: ")

qr = qrcode.QRCode()
qr.add_data(mess)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{file_name}.png")

print("QR code genarate successfully!!!")
