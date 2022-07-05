import kivy
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button

from src.FilesManager import FileManager

class MainScreen(Screen):
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self._file_manager = FileManager()
        self._files_buttons = []

    def on_enter(self):
        # Keyboard on_down callback
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _available_files_refresh(self):
        self._file_manager.refresh()
        # files count update
        file_count = self._file_manager.get_file_count()
        self.ids.available_files_label.text = f"Currently available: {file_count} .sl1 files"
        # files list update
        self.ids.files_list
        files_list = self._file_manager.get_files()
        for index in range(files_list):
            file = files_list[index]
            button = Button(text=f"{file}", size_hint=(1, 0.1), on_press=self.file_button_click(index))
            self._files_buttons.append(button)

    def file_button_click(self, id):
        for btn in self._files_buttons:




    # Events from UI
    def zoom_minus_click(self):
        pass

    def zoom_plus_click(self):
        pass

    def layer_vertical_slider_slide(self, direction=0):
        pass

    def layer_horizontal_slider_slide(self, direction=0):
        pass

    def available_files_button_click(self):
        self._available_files_refresh()

    def layer_previous_button_click(self):
        pass

    def layer_next_button_click(self):
        pass

    # Keyboard control
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.file_previous_button_click()
        elif keycode[1] == 'right':
            self.file_next_button_click()
        elif keycode[1] == 'up':
            self.layer_next_button_click()
        elif keycode[1] == 'down':
            self.layer_previous_button_click()
        elif keycode[1] == 'r':
            self.available_files_button_click()
        elif keycode[1] == 'w':
            self.layer_vertical_slider_slide(direction=+1)
        elif keycode[1] == 's':
            self.layer_vertical_slider_slide(direction=-1)
        elif keycode[1] == 'd':
            self.layer_horizontal_slider_slide(direction=+1)
        elif keycode[1] == 'a':
            self.layer_horizontal_slider_slide(direction=-1)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None