from PIL import Image, ImageDraw
import random
from random import shuffle

def main(width, height, colors, alg, f):
    #width, height, color, algorithm, filename

#specifications

    width = width
    height = height
    colors = colors

    mode = 'RGB'
    dim = (width, height)
    color = 0 #default black

    image = Image.new(mode, dim)
    image.save(f)
    draw = ImageDraw.Draw(image)

# coordinates
    # coordinate = x, y = 180, 69
    # newcoord =  (width/2, height/2)
    # print(newcoord)
    # print (image.getpixel(newcoord))
    # draw.point(newcoord, 'white')
    # image.save(f)

    allcolors = []
    allcoords = []

    if colors == 32:
        for x in range(0,colors):
            for y in range(0,colors):
                for z in range(0,colors):
                    allcolors.append((  int(255 / colors * x), int(255 / colors * y), int(255 / colors * z) ))

    if colors == 256:
        for x in range(0,colors):
            for y in range(0,colors):
                for z in range(0,colors):
                    allcolors.append( (x,y,z) )

    if alg == 0:
        for x in range (0, width):
            for y in range (0, height):
                allcoords.append((x,y))

        for x in range(0, (colors*colors*colors)):
            # rand = random.randint()
            draw.point(allcoords[x], fill=(allcolors[x][0], allcolors[x][1], allcolors[x][2]))

    if alg == 1:
        for y in range (0, height):
            for x in range (0, width):
                allcoords.append((x,y))

        for x in range(0, (colors*colors*colors)):
            # rand = random.randint()
            draw.point(allcoords[x], fill=(allcolors[x][0], allcolors[x][1], allcolors[x][2]))

    if alg == 2:
        for x in range (0, width):
            for y in range (0, height):
                allcoords.append((x,y))

        shuffle(allcolors)
        for x in range(0, (colors*colors*colors)):
            # rand = random.randint()
            draw.point(allcoords[x], fill=(allcolors[x][0], allcolors[x][1], allcolors[x][2]))

    image.save(f)
    image.show(f)

main(256, 128, 32, 0, 'tester.png')
# main(256, 128, 32, 0, '15-bit linear lr.png')
# main(256, 128, 32, 1, '15-bit linear tb.png')
# main(256, 128, 32, 2, '15-bit random.png')
#
# main(4096, 4096, 256, 0, '24-bit linear lr.png')
# main(4096, 4096, 256, 1, '24-bit linear tb.png')
# main(4096, 4096, 256, 2, '24-bit random.png')

# algorithm key
#   0 = linear left to right
#   1 = linear top to bottom
#   2 = random
