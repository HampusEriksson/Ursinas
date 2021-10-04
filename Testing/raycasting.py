from ursina.prefabs.first_person_controller import *


class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent=self.controller)
        self.hand_gun = Entity(parent=self.controller.camera_pivot,
                               scale=0.1,
                               position=Vec3(0.7, -1, 1.5),
                               rotation = Vec3(0,170,0),
                               model = "triple",
                               texture = "tripleshotgun_Base_Color",
                               visible = False)

        self.knife = Entity(parent=self.controller.camera_pivot,
                               scale=0.4,
                               position=Vec3(0.7, -1, 1.5),
                               rotation=Vec3(0, 170, 0),
                               model="triple",
                               texture="tripleshotgun_Base_Color",
                               visible=False)

        self.weapons = [self.hand_gun, self.knife]
        self.current_weapon = 0
        self.switch_weapon()

    def switch_weapon(self):
        for i,v in enumerate(self.weapons):
            if i == self.current_weapon:
                v.visible = True
            else:
                v.visible = False

    def input(self,key):
        try:
            print(key)
            self.current_weapon = int(key)-1
            self.switch_weapon()

        except ValueError:
            pass

        if key == "scroll up":
            self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
            self.switch_weapon()

        if key == "scroll up":
            self.current_weapon = (self.current_weapon - 1) % len(self.weapons)
            self.switch_weapon()


    def update(self):
        self.controller.camera_pivot.y = 2-held_keys["left control"]


app = Ursina()


ground = Entity(model="plane", scale = 20, texture = "white_cube", texture_scale = (20,20,20), collider = "mesh")
player = Player(position = (0,10,0))

# EditorCamera()

app.run()
