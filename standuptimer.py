from win10toast import ToastNotifier
from time import sleep
import sys
import pystray
from PIL import Image
from threading import Thread, Timer

min = 45
min_to_sec = min * 60


running = True

toast = ToastNotifier()

toast.show_toast(
    "StandUP!",
    "Started reminder to stand up.",
    duration=3,
    threaded=True,
)

image = Image.open("icon.png")

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

icon = pystray.Icon("StandUP!", image, "StandUP!",
                        menu=pystray.Menu(
                            pystray.MenuItem("Exit", after_click)
                        )
                    )

def notif():
    toast.show_toast(
            "StandUP!",
            "Change your desk to standing mode.",
            duration= 20,
            threaded=True,
        )

def reminder():
    while True:
        clk = Timer(min_to_sec, notif)
        clk.start()
        clk.join()


t = Thread(target=reminder, daemon=True)
t.start()

icon.run()