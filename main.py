try: from PIL.Image import open
except: from Image import open
from sys import stdout
from datetime import timedelta
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
def I2T(File):
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	isrow = True
	for pixel in data:
		if isrow:
			print('<div class="frame-row">')
			isrow = False
		if field:
			if pixel > 127: stdout.write('<div class="c2"></div>\n')
			else: stdout.write('<div class="c1"></div>\n')
		counter = counter + 1
		if counter >= w:
			counter = 0
			print("</div>")
			if field: isrow = True
			field = not field
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
index = 0
while success:
	index += 1
	print('<div class="frame' + str(index) + '">')
	I2T(BytesIO(imencode(".jpg", resize(image, (16, 8), interpolation = 3))[1]))
	print("</div>")
	vidcap.read()
	vidcap.read()
	success, image = vidcap.read()
	
