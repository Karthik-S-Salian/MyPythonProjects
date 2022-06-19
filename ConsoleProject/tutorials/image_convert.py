from PIL import Image
import glob

for file in glob.glob('resources/*.png'):
    im = Image.open(file)
    rgb_im = im.convert('RGB')  # RGBA FOR PNG RGB FOR JPG
    rgb_im.save(file.replace("png", 'jpg'), quality=95)
