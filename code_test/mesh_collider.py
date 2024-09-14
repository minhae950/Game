from ursina import *
from ursina import Ursina, Entity, Pipe, Circle, Button, scene, EditorCamera, color
app = Ursina()

e = Button(parent=scene, model='sphere', x=2)
e.collider = 'box'          # add BoxCollider based on entity's bounds.
e.collider = 'sphere'       # add SphereCollider based on entity's bounds.
e.collider = 'capsule'      # add CapsuleCollider based on entity's bounds.
e.collider = 'mesh'         # add MeshCollider matching the entity's model.
e.collider = 'file_name'    # load a model and us it as MeshCollider.
e.collider = e.model        # copy target model/Mesh and use it as MeshCollider.

e.collider = BoxCollider(e, center=Vec3(0,0,0), size=Vec3(1,1,1))           # add BoxCollider at custom positions and size.
e.collider = SphereCollider(e, center=Vec3(0,0,0), radius=.75)              # add SphereCollider at custom positions and size.
e.collider = CapsuleCollider(e, center=Vec3(0,0,0), height=3, radius=.75)   # add CapsuleCollider at custom positions and size.
e.collider = MeshCollider(e, mesh=e.model, center=Vec3(0,0,0))              # add MeshCollider with custom shape and center.

m = Pipe(base_shape=Circle(6), thicknesses=(1, .5))
e = Button(parent=scene, model='cube', collider='mesh', color=color.red, highlight_color=color.yellow)

sphere = Button(parent=scene, model='icosphere', collider='mesh', color=color.red, highlight_color=color.yellow, x=4)

EditorCamera()

def input(key):
    if key == 'c':
        e.collider = None

        
app.run()

