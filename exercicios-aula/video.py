import cv2 as cv
import numpy as np

def capture ( cap ):
    # Captura video quadro a quadro
    _, frame = cap.read()
    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(cinza,(15,15), 0)
    
    return blur

def main():
    cap = cv.VideoCapture(0)
    fundo = capture(cap)
    alfa = 0.5
    limiar = 200
    # Na minha maquina isso da problema... acho que problema
    # é a aminha camera que demora pra captar luz

    while(True):
        cinza = capture(cap)
        sub = (np.abs(cinza - fundo) > limiar).astype('uint8')
        sub = cv.normalize(sub, sub, 0, 255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
        fundo = alfa * fundo + (1-alfa) * fundo
        # processamento
        #canny = cv.Canny(cinza, 70, 90)
        # Mostra último quadro
        cv.imshow('Cinza', cinza)
        #cv.imshow('Canny', canny)
        cv.imshow('sub', sub)
        # Mostra diferença de dois frames seguidos
        # quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

main()