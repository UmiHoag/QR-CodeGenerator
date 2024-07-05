import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=HrXA_7OY0Ic&ab_channel=JulietIvy-Topic")
img.save("qrcode.png")