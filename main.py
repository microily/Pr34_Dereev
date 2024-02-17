from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class RainbowApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Метка для отображения названия цвета
        self.color_label = Label(text="Выберите цвет", font_size=20)
        layout.add_widget(self.color_label)

        # Текстовое поле для отображения кода цвета
        self.color_code_input = TextInput(multiline=False, readonly=True, font_size=16)
        layout.add_widget(self.color_code_input)

        # Кнопки с цветами радуги
        rainbow_colors = [
            ("Красный", "#ff0000"),
            ("Оранжевый", "#ff8800"),
            ("Желтый", "#ffff00"),
            ("Зеленый", "#00ff00"),
            ("Голубой", "#00ffff"),
            ("Синий", "#0000ff"),
            ("Фиолетовый", "#ff00ff")
        ]

        for color_name, color_code in rainbow_colors:
            button = Button(text=color_name, background_color=self.hex_to_rgb(color_code),
                            on_press=self.on_button_press)
            layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        color_name = instance.text
        color_code = self.rgb_to_hex(instance.background_color)

        self.color_label.text = f"Выбран цвет: {color_name}"
        self.color_code_input.text = color_code

    def hex_to_rgb(self, hex_code):
        hex_code = hex_code.lstrip("#")
        return [int(hex_code[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]

    def rgb_to_hex(self, rgb):
        return "#{:02x}{:02x}{:02x}".format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


if __name__ == '__main__':
    RainbowApp().run()
