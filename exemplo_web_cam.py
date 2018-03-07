import cv2
video = cv2.VideoCapture(0) #conectando a webcam do notebook caso tenha mais outra camera, tera q mudar o id o 0 é o padraoo
#video = cv2.VideoCapture("video\\video2.mp4") #caso queira fazer a detecção em um vídeo passe o video aqui
classificadorFace = cv2.CascadeClassifier ('cascades\haarcascade_frontalface_default.xml')

#Laço de repetação para exibião da imagem do webcam
while True:
    conectado, frame = video.read() #variavel conectado vai moestrar se a webcam esta conectado ou não
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificadorFace.detectMultiScale(frameCinza)
    for(x, y, l, a) in facesDetectadas:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0,0,255), 2)
    cv2.imshow('Vídeo', frame)
    #fechar  apertando q
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
