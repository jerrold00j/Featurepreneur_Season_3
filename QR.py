import qrcode
data = 'https://t.me/featurethonseason3'
img = qrcode.make(data)
img.save('Featurethon_QR.png')