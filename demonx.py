import tkinter as tk
from tkinter import messagebox
import time

def draw_skull():
    print("    _______________         ")
    time.sleep(0.1)
    print("   /               \       ")
    print("  /                 \      ")
    time.sleep(0.1)
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    time.sleep(0.1)
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    time.sleep(0.1)
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    time.sleep(0.1)
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    time.sleep(0.1)
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    time.sleep(0.1)
    print("   \_             _/       ")
    print("     \_         _/         ")
    time.sleep(0.1)
    print("       \_______/           ")

window = tk.Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
# window.iconbitmap('output\icons\icons8-demon-48.ico')

if messagebox.showerror('Erro', 'DemonX.iso está corrompido', type = 'okcancel') == True:
    for i in range(0,25):
        print('Sua vida foi corrompida')
        time.sleep(0.1)
        if i == 11:
            time.sleep(0.1)
            draw_skull()
            
        
    time.sleep(0.1)
else:
    for i in range(0,25):
        print('Sua vida foi corrompida')
        time.sleep(0.1)
        if i == 11:
            time.sleep(0.1)
            draw_skull()

window.deiconify()
window.destroy()
window.quit()