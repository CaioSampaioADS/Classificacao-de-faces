from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2

class Interface():

    def Captura(self):
        self.filename = askopenfilename()

        self.image = Image.open(self.filename)

        self.photo = ImageTk.PhotoImage(self.image)


        self.label = Label(self.root, image=self.photo).grid(row=1, column=0, padx=15, pady=5, rowspan=3)




    def ClassificarImagens(self):

        i = cv2.imread(self.filename)
        iPB = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

        df = cv2.CascadeClassifier('harcascade.xml')

        faces = df.detectMultiScale(iPB,
                                    scaleFactor=1.05, minNeighbors=7,
                                    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(i, (x, y), (x + w, y + h), (0, 255, 255), 7)


        cv2.imwrite("imagens/saida.jpg", i)

        self.imagem = Image.open("imagens/saida.jpg")

        self.photoo = ImageTk.PhotoImage(self.imagem)



        self.label = Label(self.root, image=self.photoo).grid(row=4, column=0, padx=15, pady=5, rowspan=3)






    def __init__(self):
        self.contador = 0
        self.root = Tk()
        self.root.resizable(True, True)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.title("Identificaçao de imagens")

        Button(self.root, text='selecione a imagem', command=self.Captura).grid(row=0, column=0, pady=5)

        Button(self.root, text='Classificar', command=self.ClassificarImagens, width=10, height=2).grid(row=2, column=1)
        vbar = Scrollbar(self.root, orient=VERTICAL)

        self.root.mainloop()


Interface()








