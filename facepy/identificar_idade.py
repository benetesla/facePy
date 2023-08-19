import cv2

# Inicializar o detector de faces do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a câmera (0 é o índice da câmera padrão)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Detectar rostos na imagem da câmera
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Fazer uma estimativa simples da idade com base na largura do rosto
        idade_estimada = int(w * 0.15)  # Exemplo
        
        # Desenhar retângulo ao redor do rosto
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Exibir a idade estimada
        cv2.putText(frame, f"Idade: {idade_estimada}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Exibir a imagem da câmera com retângulos e idades estimadas
    cv2.imshow('Detecção de Idade', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
