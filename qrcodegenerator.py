import qrcode
import image

qr = qrcode.QRCode(version=15, box_size=10, border=5)
# Put the link in the data to generate the Qrcode. 
data = "https://rishabhneogi1234.wixsite.com/travelblog-rishabhne"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
#Now you have to give the file name.
img.save("test.png")
#You will get an image of the qrcode of that particular link within the same folder

#Like here I enter my travel blogging website link and then I get the QR of the link with test.png name 