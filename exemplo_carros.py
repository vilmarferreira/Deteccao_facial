import cv2
classificador = cv2.CascadeClassifier('cascades\cars.xml') #carregar arquivo com padroes de face
imagem = cv2.imread('outros\\carro2.jpg')
##deixar em escala de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# detectar face na imagem
facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.01)
print(len(facesDetectadas))
print(facesDetectadas)
for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    #      imagem|coordenadas da face| coordenadas do desenho| cor da borda | e largura da borda
    cv2.rectangle(imagem,(x, y), (x + l, y + a), (0, 0, 255), 2)  #desenhar o retangulo
cv2.imshow ("Faces detectadas", imagem)
cv2.waitKey()
