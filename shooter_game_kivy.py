from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector
import random

Window.size = (1280, 720)

class ShooterGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.score = 0
        self.player_pos = [0, 2, 0]
        self.player_rotation = [0, 0]
        self.bullets = []
        self.enemies = []
        self.walls = []
        
        self.setup_ui()
        self.setup_game()
        
        Clock.schedule_interval(self.update, 1/60)
    
    def setup_ui(self):
        layout = FloatLayout()
        
        self.score_label = Label(
            text='Score: 0',
            font_size=30,
            pos=(50, Window.height - 80),
            size_hint=(None, None),
            color=(1, 1, 0, 1)
        )
        layout.add_widget(self.score_label)
        
        shoot_btn = Button(
            text='射击',
            font_size=24,
            size_hint=(None, None),
            size=(150, 80),
            pos=(50, Window.height - 150),
            background_color=(1, 0, 0, 1)
        )
        shoot_btn.bind(on_press=self.shoot)
        layout.add_widget(shoot_btn)
        
        jump_btn = Button(
            text='跳跃',
            font_size=24,
            size_hint=(None, None),
            size=(150, 80),
            pos=(Window.width - 350, 50),
            background_color=(0, 0, 1, 1)
        )
        jump_btn.bind(on_press=self.jump)
        layout.add_widget(jump_btn)
        
        exit_btn = Button(
            text='退出',
            font_size=24,
            size_hint=(None, None),
            size=(150, 80),
            pos=(Window.width - 180, 50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        exit_btn.bind(on_press=self.exit_game)
        layout.add_widget(exit_btn)
        
        self.add_widget(layout)
    
    def setup_game(self):
        for i in range(10):
            x = random.randint(-40, 40)
            z = random.randint(-40, 40)
            self.walls.append({'x': x, 'z': z})
        
        for i in range(15):
            x = random.randint(-40, 40)
            z = random.randint(-40, 40)
            self.enemies.append({'x': x, 'y': 1.5, 'z': z, 'color': (1, 0, 0, 1)})
    
    def shoot(self, instance):
        self.bullets.append({
            'x': self.player_pos[0],
            'y': self.player_pos[1],
            'z': self.player_pos[2],
            'dx': 0,
            'dy': 0,
            'dz': -1
        })
    
    def jump(self, instance):
        if self.player_pos[1] <= 2:
            self.player_pos[1] += 2
    
    def exit_game(self, instance):
        App.get_running_app().stop()
    
    def update(self, dt):
        self.player_pos[1] = max(2, self.player_pos[1] - 0.1)
        
        for bullet in self.bullets[:]:
            bullet['x'] += bullet['dx'] * 2
            bullet['y'] += bullet['dy'] * 2
            bullet['z'] += bullet['dz'] * 2
            
            if abs(bullet['x']) > 50 or abs(bullet['z']) > 50:
                self.bullets.remove(bullet)
                continue
            
            for enemy in self.enemies[:]:
                dist = ((bullet['x'] - enemy['x'])**2 + 
                       (bullet['y'] - enemy['y'])**2 + 
                       (bullet['z'] - enemy['z'])**2)**0.5
                if dist < 2:
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.score += 10
                    self.score_label.text = 'Score: ' + str(self.score)
                    
                    x = random.randint(-40, 40)
                    z = random.randint(-40, 40)
                    self.enemies.append({'x': x, 'y': 1.5, 'z': z, 'color': (1, 0, 0, 1)})
                    break

class ShooterApp(App):
    def build(self):
        return ShooterGame()

if __name__ == '__main__':
    ShooterApp().run()
