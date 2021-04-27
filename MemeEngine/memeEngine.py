from PIL import Image, ImageDraw
import random


class MemeEngine:
    """
    This class is responsible
    for:
        1.Loading of a file from disk
        2.Transform image by resizing
        3.Add a caption to an image
    """

    def __init__(self, output_dir):
        """
        take a required argument for where
        to save the generated images
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """
        Return an address of a Meme
        """
        try:
            text = f'{text}-{author}'
            image_extenstion = img_path.split('.')[-1]
            im = Image.open(img_path)
            ratio = width / float(im.size[0])
            height = int(ratio * float(im.size[1]))
            image_resized = im.resize((width, height))
            draw = ImageDraw.Draw(image_resized)
            draw.text((random.randint(0, width),
                      (random.randint(0, height))), text)
            tmp = f'{random.randint(1,100)}'
            output = f'{self.output_dir}{tmp}.{image_extenstion}'
            image_resized.save(output)
            return output
        except Exception as e:
            print(e)


if __name__ == "__main__":
    img = MemeEngine('./imageresized.png')
    img.make_mem(
        '../_data/photos/dog/xander_1.jpg',
        "talent can win games but teams will win win championchips",
        'mj')
