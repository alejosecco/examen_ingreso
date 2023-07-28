# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []
        self.lista_poder_pokemones = []
        self.lista_tipo_pokemones = []


    def btn_mostrar_informe_1(self):
        menor_poder = 200
        nombre_menor_poder = None
        for index in range(len(self.lista_nombre_pokemones)):
            print(f"posicion: {index}- nombre: {self.lista_nombre_pokemones[index]}")
            #3 Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
            if self.lista_tipo_pokemones[index] == "psiquico" and self.lista_poder_pokemones[index] < menor_poder:
                menor_poder = self.lista_poder_pokemones[index]
                nombre_menor_poder = self.lista_nombre_pokemones[index]
        if menor_poder != 200:
            mensaje = f"el pokemon psiquico con menos poder es {nombre_menor_poder} con un total de {menor_poder} de poder"
        else:
            mensaje = "no hay pokemones psiquicos"
        alert("informe 1", mensaje)


    def btn_mostrar_informe_2(self):
        #6) - tipo de los pokemones del tipo que mas pokemones posea. 
        contador_psiquico = 0
        contador_agua = 0
        contador_electrico = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == "agua":
                contador_agua += 1
            elif tipo == "psiquico":
                contador_psiquico +=1
            else:
                contador_electrico +=1
        if contador_psiquico < contador_agua > contador_electrico:
            mensaje = "el tipo de pokemon mas ingresado fue de agua"
        elif contador_electrico < contador_psiquico > contador_agua:
            mensaje = "el tipo de pokemon mas ingresado fue psiquico"
        elif contador_agua <contador_electrico > contador_psiquico:
            mensaje = "el tipo de pokemon mas ingresade fue electrico"
        else:
            mensaje = "no hubo un tipo de pokemon mas ingresado"
        alert("informe 2", mensaje)


    def btn_mostrar_informe_3(self):
        #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
        listado_mayor_que_el_promedio = []
        if len(self.lista_poder_pokemones) != 0:
            promedio_poder = sum(self.lista_poder_pokemones) / len(self.lista_nombre_pokemones)
            for index in range(len(self.lista_poder_pokemones)):
                if self.lista_poder_pokemones[index] > promedio_poder:
                    listado_mayor_que_el_promedio.append(self.lista_nombre_pokemones[index])
            alert("informe 3", f"los pokemones con mayor poder que el promedio son:{listado_mayor_que_el_promedio}")
        else:
            alert("error", "no se ingresaron pokemones")


    def btn_cargar_pokedex_on_click(self):
        for pokemon in range(10):
            nombre_ingresado = prompt("nombre", "ingrese el nombre del pokemon")
            while nombre_ingresado == None or nombre_ingresado == "" or not nombre_ingresado.isalpha():
                nombre_ingresado = prompt("nombre", "ingrese un nombre valido")
            self.lista_nombre_pokemones.append(nombre_ingresado)
            elemento_ingresado = prompt("elemento", "ingrese el elemento del pokemon(agua, psiquico, electrico)")
            while elemento_ingresado != "agua" and elemento_ingresado != "psiquico" and elemento_ingresado != "electrico":
                elemento_ingresado = prompt("elemento", "ingrese un elemento valido(agua, psiquico, electrico)")
            self.lista_tipo_pokemones.append(elemento_ingresado)
            poder_ingresado = prompt("poder", "ingrese el poder del pokemon (50-200)")
            while poder_ingresado == None or poder_ingresado == "" or not poder_ingresado.isnumeric() or int(poder_ingresado) <50 or int(poder_ingresado)>200:
                poder_ingresado = prompt("poder", "ingrese un poder valido (50-200)")
            self.lista_poder_pokemones.append(int(poder_ingresado))


if __name__ == "__main__":
    app = App()
    app.mainloop()