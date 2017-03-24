from PIL import Image, ImageDraw, ImageOps


# Функция создания белого холста
def new_image(mode, size):
    ni = Image.new(mode, size)
    return ni


# Функция подготовки изображений для вставки
def resize_images(*args):
    # mask basic
    mask = Image.open('img/mask.png').convert('L')

    args = args[0]
    if len(args) != 9:
        return print('The function should takes 9 image links')
    im1 = Image.open(args[0])
    size = min(im1.size)
    box = (0,0,size,size)
    im1 = im1.crop(box).resize((150,150))
    out = ImageOps.fit(im1, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im1 = out

    im2 = Image.open(args[1])
    size = min(im2.size)
    box = (0,0,size,size)
    im2 = im2.crop(box).resize((150,150))
    out = ImageOps.fit(im2, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im2 = out

    im3 = Image.open(args[2])
    size = min(im3.size)
    box = (0,0,size,size)
    im3 = im3.crop(box).resize((150,150))
    out = ImageOps.fit(im3, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im3 = out

    im4 = Image.open(args[3])
    size = min(im4.size)
    box = (0,0,size,size)
    im4 = im4.crop(box).resize((150,150))
    out = ImageOps.fit(im4, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im4 = out

    im5 = Image.open(args[4])
    size = min(im5.size)
    box = (0,0,size,size)
    im5 = im5.crop(box).resize((150,150))
    out = ImageOps.fit(im5, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im5 = out

    im6 = Image.open(args[5])
    size = min(im6.size)
    box = (0,0,size,size)
    im6 = im6.crop(box).resize((150,150))
    out = ImageOps.fit(im6, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im6 = out

    im7 = Image.open(args[6])
    size = min(im7.size)
    box = (0,0,size,size)
    im7 = im7.crop(box).resize((150,150))
    out = ImageOps.fit(im7, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im7 = out

    im8 = Image.open(args[7])
    size = min(im8.size)
    box = (0,0,size,size)
    im8 = im8.crop(box).resize((150,150))
    out = ImageOps.fit(im8, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im8 = out

    im9 = Image.open(args[8])
    size = min(im9.size)
    box = (0,0,size,size)
    im9 = im9.crop(box).resize((150,150))
    out = ImageOps.fit(im9, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    im9 = out

    return im1, im2, im3, im4, im5, im6, im7, im8, im9


# Функция вставки изображений на холст
def images_append(canvas, images):
    canvas.paste(images[0], (0,0))
    canvas.paste(images[1], (155,0))
    canvas.paste(images[2], (310,0))

    canvas.paste(images[3], (0,155))
    canvas.paste(images[4], (155,155))
    canvas.paste(images[5], (310,155))

    canvas.paste(images[6], (0,310))
    canvas.paste(images[7], (155,310))
    canvas.paste(images[8], (310,310))
    return canvas


def collage(photo, out_name):

    # Создание холста
    mode = 'RGBA'
    size = 460, 460
    canvas = new_image(mode, size)

    # Подготовка изображений
    images = resize_images(photo)

    # Вставка изображений на холст
    nine_images = images_append(canvas, images)

    # Поворот холста
    out = nine_images.rotate(-15, resample=2)

    # Обрезка холста
    box = (50,50,410,410)
    crop = out.crop(box)
    draw = ImageDraw.Draw(crop)
    crop.save('%s.png' % (out_name), 'PNG')
    

if __name__ == "__main__":
    collage(photo, out_name)


"""
Example usage

from collage import collage
photo = ('name_photo.jpg')            # Принимает кортеж с 9 изображениями
out_name = 'example'                  # Название файла
out_name = '/home/example/photo'      # Пример с директорией сохранения файла
collage(nine, name)                   # Сохраняет файл, ничего не возвращает
"""
