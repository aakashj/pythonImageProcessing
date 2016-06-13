from PIL import Image
picture = Image.open("source.png")
picture = picture.convert("RGBA")
pix = picture.load()
width, height = picture.size
print("width: {0}, height: {1}".format(width,height))

count = 0;
tot_colors = {(255,255,255, 255)}
for x in range(0, width):
	for y in range(0, height):
		tmp = pix[x,y]

		current_color = picture.getpixel( (x,y) )
		tot_colors |= {current_color}
		#tot_colors |= tmp
		if (tmp != (255, 127,39, 255)):
			count += 1;
			new_color = (255,255,255,255)
			#pix[x,y] = new_color
			picture.putpixel( (x,y), new_color)


picture.save("result.png")
print("Count ", count)
print(len(tot_colors))
#print(tot_colors)

