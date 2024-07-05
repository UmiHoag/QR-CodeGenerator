import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,error_correction = qrcode.constrants.ERROR_CORRECT_H, box_size = 10, border = 4
                    ,image_factory=None, mask_pattern=None)  
qr.adddata("")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color="blue", image_factory=None)
img.save("")