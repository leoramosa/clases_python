from consolemenu import *
from consolemenu.items import *
from colorama import Fore, Back, Style
import os

os.system('cls')

def mifuncion():
    print(Fore.CYAN)
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
def action(name):
    print( "\nHello from action {}!!!\n".format(name))
    Screen().input('Press [Enter] to continue')
def main():
    # Create the root menu
    menu = MultiSelectMenu("PLANILLA TRABAJADORES DE  COMPUTOR S.A.", "Seleccione la Opcion Deseada",
                           epilogue_text=("Seleccione una o más entradas separadas por comas y / o un rango "
                                          "o numeros. por ejemplo:  1,2,3   o   1-4   o   1,3-4"),
                           exit_option_text='Salir de la planilla de Computor S.A.')  # Customize the exit text
    # Add all the items to the root menu
    menu.append_item(FunctionItem("Listado de Productos", mifuncion, ''))
    menu.append_item(FunctionItem("Total de Sueldos basicos", action, args=['two']))
    menu.append_item(FunctionItem("Total de Bonificaciones", action, args=['three']))
    menu.append_item(FunctionItem("Total de Descuentos", action, args=['four']))
    menu.append_item(FunctionItem("Total de Sueldos Netos", action, args=['five']))
    # Show the menu
    menu.start()
    menu.join()
if __name__ == "__main__":
    main()





