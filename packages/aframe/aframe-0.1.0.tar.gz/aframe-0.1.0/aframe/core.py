import json
import requests

from bs4 import BeautifulSoup
from .a_html import ATag, HTMLBuilder


class Aframe:
    def __init__(self, version='1.3.0'):
        self.html_builder = HTMLBuilder()
        self.asset_options = None
        self.version = version
        self.__initialize_scripts()
    
    def update_configurations(self, config: dict):
        """Update HTML Configurations.

        Currently supported config keys:  

        - asset_load_timeout: int (milliseconds)

        Args:
            config (dict): keys to update in config
        """
        self.html_builder.configuration.update(config)

    def __initialize_scripts(self):
        self.html_builder.scripts.append(
            f'<script src="https://aframe.io/releases/'
            f'{self.version}/aframe.min.js"></script>')

    """ PRIMITIVES """

    def __parent_or_child(self, kw):
        """allow nesting of tags, incomplete"""
        if any([i in kw for i in ('is_parent', 'is_child')]):
            return True
        else:
            return False

    def primitive(self, tagname, **kwargs):
        tag = ATag()
        tag.tagname = f'a-{tagname}'
        tag.parameters = kwargs
        self.html_builder.objects.append(tag)

    def entity(self, **kwargs):
        self.primitive('entity', **kwargs)

    def box(self, **kwargs):
        """The box primitive creates shapes such as boxes, cubes, or walls. 
        
        See [A-Frame: <a-box>](https://aframe.io/docs/1.3.0/primitives/a-box.html)
        for examples and attributes.
        """
        self.primitive('box', **kwargs)

    def camera(self, **kwargs):
        """The camera primitive determines what the user sees. 
        
        We can change the viewport by modifying the camera entity's position and rotation.  
        
        See [A-Frame: <a-camera>](https://aframe.io/docs/1.3.0/primitives/a-camera.html)
        for examples and attributes.
        """
        self.primitive('camera', **kwargs)

    def circle(self, **kwargs):
        """The circle primitive creates circle surfaces.
        
        See [A-Frame: <a-circle>](https://aframe.io/docs/1.3.0/primitives/a-circle.html)
        for examples and attributes.
        """
        self.primitive('circle', **kwargs)

    def cone(self, **kwargs):
        """The cone primitive creates a cone shape.
        
        See [A-Frame: <a-cone>](https://aframe.io/docs/1.3.0/primitives/a-cone.html)
        for examples and attributes.
        """
        self.primitive('cone', **kwargs)

    def curvedimage(self, **kwargs):
        """The curved image primitive creates images that bend around the user. 
        
        Curved images arranged around the camera can be pleasing for legibility since each pixel 
        sits at the same distance from the user. They can be a better choice than angled flat planes 
        for complex layouts because they ensure a smooth surface rather than a series of awkward seams between planes.  

        Under the hood, a curved image is a double-sided open-ended cylinder with textures mapped to the inside of the cylinder.
        
        See [A-Frame: <a-curvedimage>](https://aframe.io/docs/1.3.0/primitives/a-curvedimage.html)
        for examples and attributes.
        """
        self.primitive('curvedimage', **kwargs)

    def cylinder(self, **kwargs):
        """The cylinder primitive is used to create tubes and curved surfaces.
        
        See [A-Frame: <a-cylinder>](https://aframe.io/docs/1.3.0/primitives/a-cylinder.html)
        for examples and attributes.
        """
        self.primitive('cylinder', **kwargs)

    def dodecahedron(self, **kwargs):
        """The dodecahedron primitive is used to create dodecahedron surfaces.
        
        See [A-Frame: <a-dodecahedron>](https://aframe.io/docs/1.3.0/primitives/a-dodecahedron.html)
        for examples and attributes.
        """
        self.primitive('dodecahedron', **kwargs)

    def gltf_model(self, **kwargs):
        """The glTF model primitive displays a 3D glTF model created from a 3D modeling program or downloaded from the web.
        
        See [A-Frame: <a-gltf-model>](https://aframe.io/docs/1.3.0/primitives/a-gltf-model.html)
        for examples and attributes.
        """
        self.primitive('gltf-model', **kwargs)

    def icosahedron(self, **kwargs):
        """The icosahedron primitive is used to create icosahedron surfaces.
        
        See [A-Frame: <a-icosahedron>](https://aframe.io/docs/1.3.0/primitives/a-icosahedron.html)
        for examples and attributes.
        """
        self.primitive('icosahedron', **kwargs)

    def image(self, **kwargs):
        """The image primitive shows an image on a flat plane.
        
        See [A-Frame: <a-image>](https://aframe.io/docs/1.3.0/primitives/a-image.html)
        for examples and attributes.
        """
        self.primitive('image', **kwargs)

    def light(self, **kwargs):
        """A light changes the lighting and shading of the scene.
        
        See [A-Frame: <a-light>](https://aframe.io/docs/1.3.0/primitives/a-light.html)
        for examples and attributes.
        """
        self.primitive('light', **kwargs)

    def link(self, **kwargs):
        """The link primitive provides a compact API to define links that resembles the traditional `<a>` tag.
        
        See [A-Frame: <a-link>](https://aframe.io/docs/1.3.0/primitives/a-link.html)
        for examples and attributes.
        """
        self.primitive('link', **kwargs)

    def obj_model(self, **kwargs):
        """The .OBJ model primitive displays a 3D Wavefront model.
        
        See [A-Frame: <a-obj-model>](https://aframe.io/docs/1.3.0/primitives/a-obj-model.html)
        for examples and attributes.
        """
        self.primitive('obj-model', **kwargs)

    def octahedron(self, **kwargs):
        """The octahedron primitive is used to create octahedron surfaces.
        
        See [A-Frame: <a-octahedron>](https://aframe.io/docs/1.3.0/primitives/a-octahedron.html)
        for examples and attributes.
        """
        self.primitive('octahedron', **kwargs)

    def plane(self, **kwargs):
        """The plane primitive creates flat surfaces.
        
        See [A-Frame: <a-plane>](https://aframe.io/docs/1.3.0/primitives/a-plane.html)
        for examples and attributes.
        """
        self.primitive('plane', **kwargs)

    def ring(self, **kwargs):
        """The ring primitive creates a ring or disc shape.
        
        See [A-Frame: <a-ring>](https://aframe.io/docs/1.3.0/primitives/a-ring.html)
        for examples and attributes.
        """
        self.primitive('ring', **kwargs)

    def sky(self, **kwargs):
        """The sky primitive adds a background color or 360° image to a scene. 
        
        A sky is a large sphere with a color or texture mapped to the inside.  
        
        See [A-Frame: <a-sky>](https://aframe.io/docs/1.3.0/primitives/a-sky.html)
        for examples and attributes.
        """
        self.primitive('sky', **kwargs)

    def sound(self, **kwargs):
        """The sound primitive wraps the sound component. 
        
        See [A-Frame: <a-sound>](https://aframe.io/docs/1.3.0/primitives/a-sound.html)
        for examples and attributes.
        """
        self.primitive('sound', **kwargs)

    def sphere(self, **kwargs):
        """The sphere primitive creates a spherical or polyhedron shapes. 
        
        See [A-Frame: <a-sphere>](https://aframe.io/docs/1.3.0/primitives/a-sphere.html)
        for examples and attributes.
        """
        self.primitive('sphere', **kwargs)

    def tetrahedron(self, **kwargs):
        """The tetrahedron primitive is used to create tetrahedron surfaces.
        
        See [A-Frame: <a-tetrahedron>](https://aframe.io/docs/1.3.0/primitives/a-tetrahedron.html)
        for examples and attributes.
        """
        self.primitive('tetrahedron', **kwargs)

    def text(self, **kwargs):
        """Wraps the text component.
        
        See [A-Frame: <a-text>](https://aframe.io/docs/1.3.0/primitives/a-text.html)
        for examples and attributes.
        """
        self.primitive('text', **kwargs)

    def torus_knot(self, **kwargs):
        """The torus knot primitive creates pretzel shapes.
        
        See [A-Frame: <a-torus-knot>](https://aframe.io/docs/1.3.0/primitives/a-torus-knot.html)
        for examples and attributes.
        """
        self.primitive('torus-knot', **kwargs)

    def torus(self, **kwargs):
        """The torus primitive creates donut or tube shapes.
        
        See [A-Frame: <a-torus>](https://aframe.io/docs/1.3.0/primitives/a-torus.html)
        for examples and attributes.
        """
        self.primitive('torus', **kwargs)

    def triangle(self, **kwargs):
        """The triangle primitive creates triangle surfaces.
        
        See [A-Frame: <a-triangle>](https://aframe.io/docs/1.3.0/primitives/a-triangle.html)
        for examples and attributes.
        """
        self.primitive('triangle', **kwargs)

    def video(self, **kwargs):
        """The video primitive plays a video as a texture on a flat plane.
        
        See [A-Frame: <a-video>](https://aframe.io/docs/1.3.0/primitives/a-video.html)
        for examples and attributes.
        """
        self.primitive('video', **kwargs)

    def videosphere(self, **kwargs):
        """The videosphere primitive plays 360° videos in the background of the scene. 
        
        Videospheres are a large sphere with the video texture mapped to the inside.  
        
        See [A-Frame: <a-videosphere>](https://aframe.io/docs/1.3.0/primitives/a-videosphere.html)
        for examples and attributes.
        """
        self.primitive('videosphere', **kwargs)

    """ ASSETS """

    def __base_add_asset(self, tagname, closing_tag=True, **kwargs):
        tag = ATag()
        tag.tagname = tagname
        tag.parameters = kwargs 
        tag.closing_tag = closing_tag
        self.html_builder.assets.append(tag)

    def add_image_asset(self, **kwargs):
        """Adds an image asset which can be accessed by the provided `id`.

        At minimum, you should provide `id` and `src` attributes.  

        See [A-Frame: 'Asset Management System'](https://aframe.io/docs/1.3.0/core/asset-management-system.html)
        for attributes, examples, and more information
        """
        self.__base_add_asset('img', closing_tag=False, **kwargs)

    def add_image_asset_by_search(
        self, 
        term: str, 
        id: str or None = None, 
        index: int = 0, 
        hq: bool = False, 
        as_texture: bool = True
    ) -> None:
        """Adds an Image asset by using Bing Image Search

        Args:
            term (str): The term to search for
            id (str or None, optional): provide an id to refer by. Defaults to None.
            index (int, optional): index of the image results. Defaults to 0.
            hq (bool, optional): High Quality or not. Defaults to False.
            as_texture (bool, optional): search for a texture. Defaults to True.
        """
        page_source = (f'https://www.bing.com/images/search?q='
                       f'{term}{" seamless texture jpg" if as_texture else ""}'
                       f'&first=1&tsc=ImageBasicHover')
        content = requests.get(page_source).content
        soup = BeautifulSoup(content, features="html.parser")
        image = soup.find_all('a', attrs={'class': 'iusc'})[index]
        url = json.loads(image.attrs['m'])['murl' if hq else 'turl']
        self.__base_add_asset('img', closing_tag=False, id=term if not id else id, src=url)

    def add_audio_asset(self, **kwargs):
        """Adds an audio asset which can be accessed by the provided `id`.

        At minimum, you should provide `id` and `src` attributes.  

        See [A-Frame: 'Asset Management System'](https://aframe.io/docs/1.3.0/core/asset-management-system.html)
        for attributes, examples, and more information
        """
        self.__base_add_asset('audio', **kwargs)

    def add_video_asset(self, **kwargs):
        """Adds a video asset which can be accessed by the provided `id`.

        At minimum, you should provide `id` and `src` attributes.  

        See [A-Frame: 'Asset Management System'](https://aframe.io/docs/1.3.0/core/asset-management-system.html)
        for attributes, examples, and more information
        """
        self.__base_add_asset('video', **kwargs)

    def add_asset_item(self, **kwargs):
        """Adds miscellaneous assets such as 3D models and materials which can be accessed by the provided `id`.

        At minimum, you should provide `id` and `src` attributes.  

        See [A-Frame: 'Asset Management System'](https://aframe.io/docs/1.3.0/core/asset-management-system.html)
        for attributes, examples, and more information
        """
        self.__base_add_asset('a-asset-item', **kwargs)

    def add_mixin(self, **kwargs):
        """Mixins provide a way to compose and reuse commonly-used sets of component properties.

        At minimum, you should provide `id` and `src` attributes.  

        See [A-Frame: 'Mixins'](https://aframe.io/docs/1.3.0/core/mixins.html)
        for attributes, examples, and more information
        """
        self.__base_add_asset('a-mixin', **kwargs)

    """ CONSTRUCTION """

    def set_scene(self, **kwargs):
        """ Sets the scene with any base attributes. 

        Check out [A-Frame: 'Scene'](https://aframe.io/docs/1.3.0/core/scene.html) for more info
        """
        tag = ATag()
        tag.tagname = 'a-scene'
        tag.parameters = kwargs
        tag.closing_tag = False
        self.html_builder.scene = tag


    def generate(self) -> str:
        """Generates the HTML document as described

        Args:
            asset_load_timeout (int, optional): time in milliseconds. Defaults to 7000.

        Returns:
            str: HTML document
        """
        return self.html_builder.build()

    def write(self, filename: str, content: str):
        """ Writes `content` to `filename`.html"""
        with open(f"{filename}.html", 'w+') as outfile:
            outfile.write(content)

    """ EXTRA FEATURES """

    def enable_environments(self):
        """Enables the 'environments' feature.

        For more information and options, see
        [aframe-environment-component](https://github.com/supermedium/aframe-environment-component/blob/master/README.md)
        """
        self.html_builder.scripts.append(
            '<script src="https://unpkg.com/aframe-environment-component/'
            'dist/aframe-environment-component.min.js"></script>')

    def enable_link_controls(self):
        self.html_builder.scripts.append("<script src=\"https://raw.githubusercontent.com/aframevr/aframe/"
                            "master/examples/showcase/link-traversal/js/components/link-controls.js\"></script>")
    
    def FUTURE_ADDITIONS(self):
        # TEXT GEOMETRY https://www.npmjs.com/package/aframe-text-geometry-component
        """
        <script src="https://unpkg.com/aframe-animation-component@3.2.1/dist/aframe-animation-component.min.js"></script>
        <script src="https://cdn.rawgit.com/delapuente/aframe-sharedspace-component/master/dist/aframe-sharedspace-component.min.js"></script>
        <script src="https://rawgit.com/feiss/aframe-environment-component/master/dist/aframe-environment-component.min.js"></script>
        <script src="https://cdn.jsdelivr.net/gh/donmccurdy/aframe-extras@v6.1.0/dist/aframe-extras.min.js"></script>
        <script src="https://supereggbert.github.io/aframe-htmlembed-component/dist/build.js"></script>
        <script src="https://unpkg.com/aframe-look-at-component@0.8.x/dist/aframe-look-at-component.min.js"></script>
        <script src="https://cdn.rawgit.com/donmccurdy/aframe-physics-system/v4.0.1/dist/aframe-physics-system.min.js"></script>
        :return:
        """
        pass
