# Importando 'Pillow' e 'os'
from PIL import Image, ImageFilter
import os

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

# Caminho para a pasta 'input' 
def in_file(filename):
    return os.path.join(INPUT_DIR, filename)


# Caminho para a pasta 'output' 
def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)


# Transforma a imagem em preto e branco
def Grayscale(colored):
    # Pega a largura e altura da imagem colorida(colored)
    width, height = colored.size
    # Cria uma nova imagem em preto e branco
    img = Image.new("RGB", (width, height))

    for x in range(width):
      for y in range(height):
        # Pega o pixel dessa posição (x,y)
        pixel = colored.getpixel((x,y))
        # Calcula a iluminação de cada pixel (média ponderada dos valores RGB do pixel sendo o peso o grau de importância que nossos olhos percebem a cor)
        luminancia = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
        # Troca as 'cores'
        img.putpixel((x,y), (luminancia, luminancia, luminancia))
    return img


# Detecta a borda
def Borda(original):
  # Cria o kernel
  kernel = ImageFilter.Kernel((3,3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)
  img = original.filter(kernel)
  return img


# Deixa a imagem borrada
def Blur(normal, r=1):
  img = normal.filter(ImageFilter.BoxBlur(r))
  return img


# Abre a imagem original
img = Image.open(in_file("Lenna.png"))

# Chama as funções 
img_grayscale = Grayscale(img)
img_borda = Borda(img)
img_blur = Blur(img)

# Salva as imagens
img_grayscale.save(out_file("img_grayscale.png"))
img_borda.save(out_file("img_borda.png"))
img_blur.save(out_file("img_blur.png"))
