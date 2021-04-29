from PIL import Image, ImageDraw, ImageFont
import random
import textwrap


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
            text_comb = f'{text}-{author}'
            im = Image.open(img_path)
            ratio = width / float(im.size[0])
            height = int(ratio * float(im.size[1]))
            image_resized = im.resize((width, height), Image.NEAREST)
            draw = ImageDraw.Draw(image_resized)
            # for the wrapper I got help from https://stackoverflow.com/questions/8257147/wrap-text-in-pi
            wrapper = textwrap.TextWrapper(width=50)
            word_lst = wrapper.wrap(text=text_comb)
            text_new = ''
            for word in word_lst[:-1]:
                text_new = text_new + word + '\n'
                text_new += word_lst[-1]
            draw.text((random.randint(0, width),
                      (random.randint(0, height))), text_new)
            tmp = f'{random.randint(1,100)}'
            img_path = img_path.split('/')[-1]
            output = f'{self.output_dir}{img_path}'
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
