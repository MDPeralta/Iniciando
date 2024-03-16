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
        
        personas_viaje = prompt("PASAJEROS", "Ingrese la cantidad de pasajeros para el viaje:")
        personas_viaje = int(personas_viaje)

        planeta = prompt("PLANETA", "Ingrese un planeta destino (marte, luna, titan)")

        temporada = prompt("TEMPORADA", "Ingrese la temporada para el viaje (verano, primavera, otoño o invierno)")

        marte_viaje = 60e6 * 8
        luna_viaje = 50e4 * 8 
        titan = 1300e6 * 8
        suma_descuento = 0

        if planeta == "marte":
            if personas_viaje > 5:
                descuento = 50

                if temporada == "verano":
                    suma_descuento = 10
                
                elif temporada == "otoño" or temporada == "primavera":
                    suma_descuento = 25
                
                else:
                    suma_descuento = 0
            
            else:
                descuento = 0
        
            precio_total = marte_viaje / 1e6
        
        elif planeta == "luna":

            if personas_viaje > 5:
                descuento = 40
            
                if temporada == "verano":
                    suma_descuento = 15
                
                elif temporada == "otoño" or temporada == "primavera":
                    suma_descuento = 25
                
                else:
                    suma_descuento = 0
            else:
                descuento = 0
                
            precio_total = luna_viaje /1e6

        else:
            if personas_viaje > 5:
                descuento = 30

                if temporada == "otoño" or temporada == "primavera":
                    suma_descuento = 20 

                elif temporada == "verano":
                    suma_descuento = 10
            
            else:
                descuento = 0
            
            precio_total = titan / 1e6
        
        precio_descuento = precio_total - (precio_total * (descuento/100)) 
        precio_neto = precio_descuento + (precio_descuento * (suma_descuento/100))

        print(f"Viajando hacia {planeta} con {personas_viaje} pasajeros tiene un costo de {precio_neto} bitcoins")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
