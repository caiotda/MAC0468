import cv2 as cv
import sys

'''
Filtros: 
* Borramento
* Gaussiano
* Sobel
* Laplaciano

Para fazermos os filtros, usamos *convolução*. 

Os filtros são usados para lidarmos com imperfeiçẽs na
imagem: as vezes por uma falha no sensor ou flutuação
elétrica, a imagem capturada vem com algum problema.

Esses filtros normalmente olham para valores de pixels
dentro de uma vizinhança e decidem como eliminar ruido
baseado nos valores proximos. 

Alguns exemplos de filtro:

Filtro de media: blur


Aqui o que fazemos é aplicar o filtro para cada pixel
de uma região. O que fazemos é determinar o tamanho 
de uma região e criar uma amtriz chamada kernel assim:

digamos, kernel = 3x3
|1  1   1|
|1  1   1|
|1  1   1|

Multiplicamos a região por esse kernel e dividimos por 9 (que é a soma de todos os termos no kernel)

Multiplicar pelo kernel e então dividir pela soma de 
termos é o que chamamos de **convolução**.

Esse filtro é aplicado para o elemento no centro da ]
vizinhança.

Quanto maior o tamanho do kernel, mais intensa é a 
transformação

### Filtro gaussiano

Com o filtro de média, o borramento das médias é muito
intenso. Isso acontece porque o kernel aplica a 
convolução igualmente a todo pixel da vizinhança.

O filtro gaussiano usa justamente uma superficie
gaussiana para distribuir esse peso entre os pixels da 
vizinhança. Quanto mais distante do centro do kernel,
menor é o peso no pixel (se assemelhando a uma curva
gaussiana, na forma de sino)

Rode o exemplo do messi com filtro de media com kernel
size 9. As feições do messi ficam bem mais visiveis, 
as bordas mais definidas. O que acaba sendo 
preferível para processamento de sinais
'''

def on_trackbar_blur(valor):
    blurring_med = valor
    blur_1 = cv.blur(img, (blurring_med,blurring_med)) #Kernel do blur de 5x5
    cv.imshow("borrado", blur_1)


def on_trackbar_gauss(valor):
    blurring_gauss = valor
    gb = cv.GaussianBlur(img, (blurring_gauss,blurring_gauss), 0) #Kernel do blur de 5x5
    cv.imshow("gaussiano", gb)


def main():
    global blur_1, gb, blurring_med, blurring_gauss, img
    blurring_med = 5
    blurring_gauss = 5
    if len(sys.argv) != 2:
        print("erro")
        return
    else:
        fname = sys.argv[1]
        img   = cv.imread(fname)
        ddepth= cv.CV_16S
        
        # Converte imagem para tons de cinza e aplica um filtro de cinza 
        # Antes de aplicar o filtro de sobel.
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (9, 9), 0)

        # Monta filtro de sobel para cada direção.
        grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=1, delta=0)
        grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=1, delta=0)
        
        #Converte para valores absolutos
        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        # Tomando as componentes verticais e horizontais, tira a intensidade
        # do gradiente em cada ponto (teorema de pitagoras)
        grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        # Aplica filtro de media. Tamano do kernel é blurring_med x blurring_med
        blur_1 = cv.blur(img, (blurring_med,blurring_med))

        # Aplica filtro gaussiano.
        gb   = cv.GaussianBlur(img, (blurring_gauss, blurring_gauss), 0)
        cv.imshow("borrado", blur_1)
        cv.imshow("gaussiano", gb)

        cv.imshow("sobel", grad)

        
        # Cria trackbars que controlam o tamanho do kernel. Note como conforme
        # aumentamos o tamanho do kernel, mais borrada fica a imagem. Ademais, 
        # veja como o filtro gaussiano preserva bordas.
        cv.createTrackbar("borrao", "borrado", 0, 10, on_trackbar_blur)
        cv.createTrackbar("borrao", "gaussiano", 0, 10, on_trackbar_gauss)
        cv.waitKey(0)

main()