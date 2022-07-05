import kivy
from kivy.app import App
from kivy.core.window import Window

from bin.MainScreen import MainScreen

class SlaApp(App):
    # workaround to window resizing bug: https://github.com/kivy/kivy/issues/5359 part 1
    def to_window(self, x, y, initial=True, relative=False):
        return x,y

    def __init__(self, **kwargs):
        super(SlaApp, self).__init__(**kwargs)

        # workaround to window resizing bug: https://github.com/kivy/kivy/issues/5359 part 2
        self.y = 0

        # resize window
        Window.size = (1500, 800)

if __name__ == '__main__':
    kivy.Config.set('graphics', 'resizable', True)
    SlaApp().run()