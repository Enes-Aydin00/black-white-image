from PIL import Image
name = input("Dosyanın tam adını giriniz: ")
resim = Image.open(name)
kopya_resim = resim.copy()
x, y = resim.size
for dim1 in range(x):
    for dim2 in range(y):
        kod = resim.getpixel((dim1, dim2))
        Rr = kod[0]
        Gg = kod[1]
        Bb = kod[2]
        ort = int((Rr+Gg+Bb)/3)
        kopya_resim.putpixel((dim1, dim2), (ort, ort, ort))
kopya_resim.save("output_BlackWhite.png")
