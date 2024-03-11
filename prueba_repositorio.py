import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mauro
apellido: Peralta
---
Ejercicio: if_01
---
La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #el costo por millón de kilómetros es de 8 bitcoin
        personas_viaje = prompt("cantidad de personas", "Ingrese cantidad de pesonas en el viaje")

        personas_viaje = int(personas_viaje)

        temporada = prompt("Temporada", "Ingrese la temporada")

        planeta = prompt("Eleccion de planeta", "Elegir destino")

        Datos_cliente = self.txt_edad.get()

        match planeta:
            case "marte":
                if personas_viaje > 5:
                    descuento = 50
                elif temporada == "verano":
                    primer_suma_descuento = 10
                elif temporada == "otoño" or temporada == "primavera":
                    segunda_suma_descuento = 25
                else:
                    descuento = 0

        
        
        

                


            
            


        #if planeta == "marte":
         #   if personas_viaje > 5:
         #       descuento = 50
          #  elif temporada ("verano"):
           #     suma_descuento = 10
            
            

        
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
