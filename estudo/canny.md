### Filtro de canny

Na aula passada...



Vimos como melhorar o método sobel. Concluimos que deveríamos comparar nossa segmentação com um **gabarito humano**. Essa comparação deve ser **quantitativa**. Essa comparação olha para **positivios e negativos** (pixels classificados como bordas ou fundo), positivios ou negativos (ou seja, para cada categoria, se acertei ou errei). Para tanto usamos **precisão e acuidade**.



Um dos **problemas de sobel** é que, conforme aumentamos a suavização gaussiana aplicada antes de colocarmos o filtro de sobel, maior é a região de alto contraste entre duas regiões (pense que uma borda seria uma região **pontual** de alto contraste) ![sobel](/home/caio/Documentos/BCC/atual/MAC0468/estudo/sobel.png)

A intenção teorica do filtro de suavizamento seria de implementar esse pontilhado laranja. Mas como os pixels possuem valores discretos - e não continuos - geramos uma escadinha com mais degraus. Assim, se tomarmos um threshold alto, isso resulta numa borda grossa.



Uma solução a isso seria verificar qual é exatamente o pixel que apresenta valor máximo ao aplicarmos o gradiente. Esse único pixel sera nossa borda. (supressão de máximo). O problema é que essa solução ainda está sucetível a destacarmos bordas que não nos interessam, como bordas de texturas. Ainda teriamos que usar um limiar.

Além disso, o sobel é bem sensível a ruído, porque é uma região local de alto contraste (aplicar um filtro gaussiano acaba resolvendo um pouco). 



Uma outra solução interessante seria considerar dois thresholds diferentes: temos bordas fortes e bordas fracas, mais sutis. Com  1 threshold apenas, se tomarmos um valor alto, a borda mais baixa some. Se tomarmos um valor baixo, aparece muita sugeira.



O processo de misturar bordas fortes com fracas é chamado de  **histerese**.

### Filtro de Canny

O filtro de canny combina exatamente todas essas etapas. Quando aplicamos um filtro de canny estamos fazendo:

1. Remoção de ruído (gaussiano)
2. Calculando gradientes (**sobel**)
3. Supressaõ de máximo (**remoção de bordas grossas**)
4. Calculando duplo threshold (combinamos bordas fracas e fortes pela (**histerese**)

Vamos passar por cada etapa e tentar entender como isso funciona pra montar as bordas:

**remoção de ruido e sobel**: Isso é padrão pra gente começar a detectar bordas. Devido à suavização, ficamos com bordas grossas.

**supressão de máximo**: essa etapa serve justamente para tirarmos bordas grossas e considerarmos bordas mais finas. O que fazemos aqui é percorrer as bordas da imagem e olhar o gradiente em cada ponto (naturalmente, perpendicular à borda). Se esse ponto é um maximo local na direção do gradiente, então é uma borda fina. Do contrario, a gente zera o pixel (Supondo aqui que o fundo é preto).

**Duplo threshold**: Como queremos usar algumas bordas finas na nossa imagem, é conveniente usarmos 2 thresholds: um alto e baixo. Valores acima do threshold alto são considerados **bordas verdadeiras**. Valores abaixo do threshold baixo são descartados como candidatos. 

A graça vem quando consideramos bordas intermediárias, entre os dois thresholds: só consideramos uma borda intermediária como borda forte se ela estiver conectada a uma borda forte. Do contrario, descartamos.



Dessa forma a gente consegue juntar bordas fortes e fracas de forma coerente.



No openCv, para segmentar uma imagem usando canny, usa-se:

```python
res = cv.Canny(img, minVal=100, maxVal=200) 
```

Onde minVal e maxVal são os thresholds baixo e alto respectivamente.