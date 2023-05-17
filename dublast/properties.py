import bpy
from bpy.types import Scene, PropertyGroup
from bpy.props import (BoolProperty, IntProperty, FloatProperty,
                        StringProperty, EnumProperty,
                        FloatVectorProperty, PointerProperty)

class DUBLAST_settings( PropertyGroup ):
    """Playblast settings for a scene."""

    increment: BoolProperty( name= "", description= "Increment playblast with numbers", default=False)
    use_stamp: BoolProperty( name= "", description= "Render the metadata into the playblast", default= True)
    include_annotations: BoolProperty( name= "", description= "Include Annotations", default= True)

    use_camera: BoolProperty( name= "Scene Camera", description= "Use the scene camera", default= False)
    use_scene_frame_range: BoolProperty( name= "Scene Frame Range", description= "Use the scene frame range", default= True)
    frame_start: IntProperty( name= "Start", description= "Overrides the frame start for the playblast", default = 1, min=0 )
    frame_end: IntProperty( name= "End", description= "Overrides the frame end for the playblast", default = 250, min=0 )
    frame_step: IntProperty( name= "Step", description= "Overrides the frame step for the playblast", default = 1, min=1 )

    filepath: StringProperty( name="Output Path", description="Directory/name to save playblasts", subtype="FILE_PATH")
    use_scene_name: BoolProperty( name= "Scene Name", description= "Uses the name of the scene when saving file", default= True)
    use_scene_path: BoolProperty( name= "Scene Path", description= "Saves the file next to the scene file", default= True)
    resolution_percentage: FloatProperty( name= "Resolution %", description= "Overrides the rendering resolution percentage for the playblast", default = 25.0, min=0.0, max= 100.0, precision=0, subtype='PERCENTAGE')

    file_format: EnumProperty(
        items = [
            ('PNG', "PNG", "Output image in PNG format.", 'FILE_IMAGE', 1),
            ('JPEG', "JPEG", "Output image in JPEG format.", 'FILE_IMAGE', 2),
            ('AVI_JPEG', "AVI JPEG", "Output video in AVI JPEG format.", 'FILE_MOVIE', 3),
            ('MP4', "MP4", "Output video in MP4 format, but optimized for animation playblast.", 'FILE_MOVIE', 4)
        ],
        name = "File Format",
        description= "File format to save the playblasts",
        default= 'MP4'
        )

    color_mode: EnumProperty(
        items = [
            ('BW', "BW", "Images get saved in 8 bits grayscale", '', 1),
            ('RGB', "RGB", "Images are saved with RGB (color) data", '', 2),
            ('RGBA', "RGBA", "Images are saved with RGB and Alpha data (if supported)", '', 3)
        ],
        name = "Color",
        description= "Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels",
        default= 'RGB'
        )

    color_mode_no_alpha: EnumProperty(
        items = [
            ('BW', "BW", "Images get saved in 8 bits grayscale", '', 1),
            ('RGB', "RGB", "Images are saved with RGB (color) data", '', 2)
        ],
        name = "Color",
        description= "Choose BW for saving grayscale images, RGB for saving red, green and blue channels",
        default= 'RGB'
        )
    
    compression: IntProperty( name= "Compression", description= "Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output", default = 15, min=0, max = 100 )
    quality: bpy.props.IntProperty( name= "Quality", description= "Quality for image formats that support lossy compression", default = 50, min=0, max = 100 )

    auto_size_stamp_font: BoolProperty( name= "Auto-size Text", description= "Resize text overlay font size based on resolution", default= True)
    font_size: IntProperty( name= "Text Size", description= "Font size for text overlays", soft_min=1, soft_max=40, default= 14)

    use_stamp_date: BoolProperty( name= "Date", description= "Include the current date", default= True)
    use_stamp_time: BoolProperty( name= "Time", description= "Include the current time", default= False)
    use_stamp_render_time: BoolProperty( name= "Render Time", description= "Include the render time", default= False)
    use_stamp_frame: BoolProperty( name= "Frame", description= "Include the current frame", default= True)
    use_stamp_frame_range: BoolProperty( name= "Frame Range", description= "Include the frame range", default= False)
    use_stamp_memory: BoolProperty( name= "Memory", description= "Include memory usage", default= False)
    use_stamp_hostname: BoolProperty( name= "Hostname", description= "Include the name of the computer", default= True)
    use_stamp_camera: BoolProperty( name= "Camera", description= "Include the name of the camera", default= True)
    use_stamp_lens: BoolProperty( name= "Lens", description= "Include the focal length", default= True)
    use_stamp_scene: BoolProperty( name= "Scene", description= "Include the name of the scene", default= False)
    use_stamp_marker: BoolProperty( name= "Marker", description= "Include the name of the last marker", default= False)
    use_stamp_filename: BoolProperty( name= "Filename", description= "Include the name of the file", default= True)
    use_stamp_note: BoolProperty( name= "Note", description= "Include a custom note", default= False)

    stamp_foreground: FloatVectorProperty(
            name="Text Color",
            subtype="COLOR",
            default=(0.8, 0.8, 0.8, 1.0),
            size=4,
            min=0, max=1.0,
            description="Color to use for metadata text")

    stamp_background: FloatVectorProperty(
            name="Text Background Color",
            subtype="COLOR",
            default=(0.0, 0.0, 0.0, 0.25),
            size=4,
            min=0, max=1.0,
            description="Color to use behind metadata text")

    stamp_note_text: StringProperty( name= "Note Text", description="Custom text to appear in the stamp note", default="")

    shading: EnumProperty(
        items = [
            ('WIREFRAME', "", "Wireframe shading", 'SHADING_WIRE', 1),
            ('SOLID', "", "Solid shading", 'SHADING_SOLID', 2),
            ('MATERIAL', "", "Material shading", 'SHADING_TEXTURE', 3),
            ('RENDERED', "", "Rendered shading", 'SHADING_RENDERED', 4)
        ],
        name = "Shading",
        description= "Choose shading type for Playblast",
        default= 'RENDERED'
        )

    light: EnumProperty(
        items = [
            ('STUDIO', "Studio", "Render using studio lighting.", '', 1),
            ('MATCAP', "MatCap", "Render using matcap material and lighting.", '', 2),
            ('FLAT', "Flat", "Render using flat lighting.", '', 3),
        ],
        name = "Lighting",
        description= "Lighting Method for Solid/Texture Viewport Shading",
        default= 'STUDIO'
        )

    color_type: EnumProperty(
        items = [
            ('MATERIAL', "Material", "Render using material color.", '', 1),
            ('SINGLE', "Single", "Render using a single color.", '', 2),
            ('OBJECT', "Object", "Render using object color.", '', 3),
            ('RANDOM', "Random", "Render using random object color.", '', 4),
            ('VERTEX', "Vertex", "Render using vertex color.", '', 5),
            ('TEXTURE', "Texture", "Render using texture.", '', 6),
        ],
        name = "Color",
        description= "Color Type",
        default= 'MATERIAL'
        )
    
    wireframe_color_type: EnumProperty(
        items = [
            ('SINGLE', "Single", "Render using a single color.", '', 2),
            ('OBJECT', "Object", "Render using object color.", '', 3),
            ('RANDOM', "Random", "Render using random object color.", '', 4),
        ],
        name = "Color",
        description= "Color Type",
        default= 'SINGLE'
        )

    single_color: FloatVectorProperty(
            name="",
            subtype="COLOR",
            default=(1.0, 1.0, 1.0),
            size=3,
            min=0, max=1.0,
            description="Color for Single Mode")

    background_type: EnumProperty(
        items = [
            ('THEME', "Theme", "Use the theme for background color.", '', 1),
            ('WORLD', "World", "Use the world for background color.", '', 2),
            ('VIEWPORT', "Viewport", "Use a custom color limited to this viewport only.", '', 3),
        ],
        name = "Background",
        description= "Way to render the background",
        default= 'THEME'
        )

    background_color: FloatVectorProperty(
            name="",
            subtype="COLOR",
            default=(0.05, 0.05, 0.05),
            size=3,
            min=0, max=1.0,
            description="Color for custom background color")

def register():
    bpy.utils.register_class(DUBLAST_settings)

    # New playblast attribute in the scenes
    if not hasattr( Scene, 'playblast' ):
        Scene.playblast = PointerProperty( type=DUBLAST_settings )

def unregister():
    bpy.utils.unregister_class(DUBLAST_settings)

    del Scene.playblast