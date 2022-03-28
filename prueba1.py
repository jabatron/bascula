from pywebio import start_server
from pywebio.output import put_text, put_table, use_scope, put_row, put_code, put_scope
from random import randint
from time import sleep
from datetime import datetime

from infi.systray import SysTrayIcon
import webbrowser



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
    start_server(leer_peso, port=8080, debug=True)
    