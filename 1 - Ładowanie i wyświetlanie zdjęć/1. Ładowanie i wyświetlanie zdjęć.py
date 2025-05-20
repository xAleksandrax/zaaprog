import cv2

# Zadanie 1
image_path = "jamnik.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Zadanie 1", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Zadanie 2
image_color = cv2.imread(image_path)
if image_color is not None:
    (h, w, c) = image_color.shape
    print(f"[Zadanie 2] Wymiary: {w}x{h}, Liczba kanałów: {c}")
else:
    print("[Zadanie 2] Nie udało się wczytać obrazu.")

# Zadanie 3
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image_gray is not None:
    print(f"[Zadanie 3] Wymiary: {image_gray.shape[1]}x{image_gray.shape[0]}, Liczba kanałów: 1")
    cv2.imshow("Zadanie 3", image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("[Zadanie 3] Nie udało się wczytać obrazu.")

# Zadanie 4
if image_gray is not None:
    output_path = "gray_output.jpg"
    cv2.imwrite(output_path, image_gray)
    print(f"[Zadanie 4] Obraz w skali szarości zapisany jako {output_path}")

# Zadanie 5
img1 = cv2.imread(image_path)
img2 = cv2.imread(image_path)

if img1 is not None and img2 is not None:
    cv2.imshow("Zadanie 5: Obraz 1", img1)
    cv2.imshow("Zadanie 5: Obraz 2", img2)
    print("[Zadanie 5]")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("[Zadanie 5] Nie udało się wczytać jednego z obrazów.")

# Zadanie 6
image_resizable = cv2.imread(image_path)
if image_resizable is not None:
    cv2.namedWindow("Zadanie 6: Zmienny rozmiar", cv2.WINDOW_NORMAL)
    cv2.imshow("Zadanie 6: Zmienny rozmiar", image_resizable)
    print("[Zadanie 6]")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("[Zadanie 6] Nie udało się wczytać obrazu.")
