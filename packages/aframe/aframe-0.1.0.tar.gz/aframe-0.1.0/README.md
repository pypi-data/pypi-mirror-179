# A-FRAME

An easy-to-use python wrapper for the A-Frame web framework.

`pip install aframe`  


## What is A-Frame?
A-Frame is a web framework for building virtual reality (VR) experiences. A-Frame is based on top of HTML, making it simple to get started. But A-Frame is not just a 3D scene graph or a markup language; the core is a powerful entity-component framework that provides a declarative, extensible, and composable structure to [three.js](https://threejs.org/).  

Originally conceived within Mozilla and now maintained by the co-creators of A-Frame within [Supermedium](https://supermedium.com), A-Frame was developed to be an easy yet powerful way to develop VR content. As an [independent open source project](https://github.com/aframevr/), A-Frame has grown to be one of the [largest VR communities](https://aframe.io/community/).  

A-Frame supports most VR headsets such as Vive, Rift, Windows Mixed Reality, Daydream, GearVR, Cardboard, Oculus Go, and can even be used for augmented reality. Although A-Frame supports the whole spectrum, A-Frame aims to define fully immersive interactive VR experiences that go beyond basic 360° content, making full use of positional tracking and controllers.  


## Example
Here is an example using the Aframe library with FastAPI to create a VR Hello World:  

```
from aframe import Aframe, xyz
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/')
def hello_world():
    a = Aframe()
    a.set_scene(background="color: #ECECEC")
    a.box(position=xyz(-1, 0.5, -3), rotation=xyz(0, 45, 0), 
          color="#4CC3D9", shadow=True)
    a.sphere(position=xyz(0, 1.25, -5), radius=1.25, 
             color="#EF2D5E", shadow=True)
    a.cylinder(position=xyz(1, 0.75, -3), radius=0.5, 
               height=1.5, color="#FFC65D", shadow=True)
    a.plane(position=xyz(0, 0.1, -4), rotation=xyz(-90, 0, 0), 
            width=4, height=4, color="#7BC8A4")
    return HTMLResponse(a.generate())

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
```  

For a more involved example, run the following in a script file:

```
from aframe.templates import fastapi
fastapi()
```