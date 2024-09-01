import cv2
import pytesseract

# Charger l'image de la maquette
image = cv2.imread('maquette.png')

# Utiliser OpenCV pour détecter des contours (par exemple, pour trouver des boutons)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)

# Trouver les contours des éléments
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours détectés
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Afficher l'image avec les contours détectés
cv2.imshow('UI Elements', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Utiliser Tesseract pour la reconnaissance de texte (pytesseract doit être installé)
text = pytesseract.image_to_string(image)
print("Text detected in image:", text)
