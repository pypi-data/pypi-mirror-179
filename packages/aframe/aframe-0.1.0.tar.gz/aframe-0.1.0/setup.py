# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aframe', 'aframe.examples']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'inline-example>=0.1.1,<0.2.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'aframe',
    'version': '0.1.0',
    'description': '',
    'long_description': '# A-FRAME\n\nAn easy-to-use python wrapper for the A-Frame web framework.\n\n`pip install aframe`  \n\n\n## What is A-Frame?\nA-Frame is a web framework for building virtual reality (VR) experiences. A-Frame is based on top of HTML, making it simple to get started. But A-Frame is not just a 3D scene graph or a markup language; the core is a powerful entity-component framework that provides a declarative, extensible, and composable structure to [three.js](https://threejs.org/).  \n\nOriginally conceived within Mozilla and now maintained by the co-creators of A-Frame within [Supermedium](https://supermedium.com), A-Frame was developed to be an easy yet powerful way to develop VR content. As an [independent open source project](https://github.com/aframevr/), A-Frame has grown to be one of the [largest VR communities](https://aframe.io/community/).  \n\nA-Frame supports most VR headsets such as Vive, Rift, Windows Mixed Reality, Daydream, GearVR, Cardboard, Oculus Go, and can even be used for augmented reality. Although A-Frame supports the whole spectrum, A-Frame aims to define fully immersive interactive VR experiences that go beyond basic 360° content, making full use of positional tracking and controllers.  \n\n\n## Example\nHere is an example using the Aframe library with FastAPI to create a VR Hello World:  \n\n```\nfrom aframe import Aframe, xyz\nfrom fastapi import FastAPI\nfrom fastapi.responses import HTMLResponse\nimport uvicorn\n\napp = FastAPI()\n\n@app.get(\'/\')\ndef hello_world():\n    a = Aframe()\n    a.set_scene(background="color: #ECECEC")\n    a.box(position=xyz(-1, 0.5, -3), rotation=xyz(0, 45, 0), \n          color="#4CC3D9", shadow=True)\n    a.sphere(position=xyz(0, 1.25, -5), radius=1.25, \n             color="#EF2D5E", shadow=True)\n    a.cylinder(position=xyz(1, 0.75, -3), radius=0.5, \n               height=1.5, color="#FFC65D", shadow=True)\n    a.plane(position=xyz(0, 0.1, -4), rotation=xyz(-90, 0, 0), \n            width=4, height=4, color="#7BC8A4")\n    return HTMLResponse(a.generate())\n\nif __name__ == \'__main__\':\n    uvicorn.run("main:app", port=8000, log_level="info", reload=True)\n```  \n\nFor a more involved example, run the following in a script file:\n\n```\nfrom aframe.templates import fastapi\nfastapi()\n```',
    'author': 'MBeebe',
    'author_email': 'pyn-sol@beebe.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
