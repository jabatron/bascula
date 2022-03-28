from infi.systray import SysTrayIcon
import webbrowser


def say_hello(systray):
    print ("Hello, World!")
    webbrowser.open('http://localhost:8080', new=2)
menu_options = (("Ver pesaje", None, say_hello),)
systray = SysTrayIcon("weight.ico", "Ver pesaje", menu_options)
systray.start()