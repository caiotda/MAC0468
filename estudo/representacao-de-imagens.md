# Representação de imagens

***

Representacão de cores:

* RGB
* HSV

### Filtros digitais

Muitas vezes, a imagem capturada vai conter imperfeições: seja por baixa qualidade do sensor, ou por baixa qualidade do transsutor entre sinal analogico e digital, ou até mesmo aberrações que vem da lente da câmera. Para tanto, existem **filtros digitais** que lidam com essas imperfeições da imagem.

Existem também alguns filtros óticos, que trabalham mais na camada de captação da imagem.

**Filtro de média**: 

Numa imagem, imaginamos que a distribuição de cores numa dada região da imagem deve ser razoavelmente uniforme (isso se tomarmos uma região pequena). O filtro de média basicamente seleciona uma região pequena da imagem, que temos suspeita de  ter um chuvisco - ruído -, e tiramos a média das cores naquela vizinhança. Substituimos a cor outlier pela média. Fazemos isso para cada pixel da região da imagem na qual vamos aplicar o filtro.

**Filtro de mediana**: a mesma coisa que o filtro anterior, mas aqui usamos a mediana ao invés de média. Isso é mais robusto estatisticamente.



### Convolução

Convolução é um processo de aplicação de um filtro g em uma imagem f. Fazemos isso aplicando um filtro de vizinhança de tamanho m numa imagem de tamanho 2m+1 x 2m+1:

A convolução é descrita matematicamente como:
$$
(g * f)* (x,y) = \sum_{i=0}^{2m}\sum_{j=0}^{2m}g(i, j) . f(x-m+i, y-m+j)
$$
O que isso significa, na prática, é que estamos aplicando um filtro g numa região x, y de f. Isso é feito multiplicando todo elemento na vizinhança m de (x,y) pela matriz g



Filtros de convolução podem ser usados para encontrar **bordas**. Isso porque bordas são regiões da imagem de alto contraste.

O que constitui uma borda? São descontinuidades de :

* Profundidade
* Orientação na superfície
* Iluminação
* Reflectância