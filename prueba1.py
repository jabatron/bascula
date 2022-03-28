from pywebio import start_server
from pywebio.output import put_text, put_table, use_scope, put_row, put_code, put_scope
from random import randint
from time import sleep
from datetime import datetime

from infi.systray import SysTrayIcon
import webbrowser
import fdb


# Abrir base de datos.
def abrir_base_de_datos(file):
    try:
        con = fdb.connect(dsn=file, user='sysdba', password='masterkey')
    except:
        print ('No se ha podido abrir la base de datos')

    return con

@use_scope('time', clear=True)
def show_time():
    put_text(str(datetime.now())[:19])

def leer_peso():

    put_row([ put_scope('time'), None, put_text('PESO'), None, put_scope('scope2'), ], size='20% 10px 5% 10px 20%')


    while True:
        with use_scope('scope2', clear=True):  # enter the existing scope and clear the previous content
            put_text(randint(0, 100))
        show_time()
        sleep (3)


def say_hello(systray):
    print ("Hello, World!")
    webbrowser.open('http://localhost:8080', new=2)

menu_options = (("Ver pesaje", None, say_hello),)
systray = SysTrayIcon("weight.ico", "Ver pesaje", menu_options)
systray.start()

if __name__ == '__main__':
    db = abrir_base_de_datos('localhost:C:\\PesoBasulaIDE\\Exe\\PESOS_BASCULA.FDB')
    cur = db.cursor()

    # cur.execute("select * from PESOS_BASCULA")
    cur.execute("insert into GT_PESO_BASCULA (PESO) values (1973)")
    db.commit()

   
    start_server(leer_peso, port=8080, debug=True)
    