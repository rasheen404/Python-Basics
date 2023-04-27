from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import gyroscope

class GyroApp(App):
    def build(self):
        self.label = Label(text="Gyrometer values: X=0, Y=0, Z=0")
        Clock.schedule_interval(self.update_label, 1.0 / 60.0)
        gyroscope.enable()
        return self.label

    def update_label(self, dt):
        x, y, z = gyroscope.rotation_rate[:3]
        self.label.text = f"Gyrometer values: X={x}, Y={y}, Z={z}"

if __name__ == "__main__":
    GyroApp().run()
