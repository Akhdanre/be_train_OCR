import cv2
import pytesseract

def find_text(filename):
    img = cv2.imread(filename, 0)
    img = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
    img = cv2.equalizeHist(img)

    gray = cv2.adaptiveThreshold(
        img,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    text = pytesseract.image_to_string(
        gray,
        lang="ind+eng",
        config="--psm 6 --oem 3"
    )

    text = text.split("\n")

    r_text = []
    for line in text:
        if line.strip():
            r_text.append(line)

    text = "\n".join(r_text[1:])
    text = text.replace('|', "I")
    text = text.replace('‘', "'").replace('’', "'").replace('"', '')
    text = " ".join(text.split())

    return text
