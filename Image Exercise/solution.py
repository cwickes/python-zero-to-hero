from PIL import Image

word_matrix = Image.open('Image Exercise/word_matrix.png')
mask = Image.open('Image Exercise/mask.png')
mask = mask.resize((word_matrix.width, word_matrix.height))
mask.putalpha(200)
word_matrix.paste(mask, mask)
word_matrix.save('Image Exercise/solution.png')