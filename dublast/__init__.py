# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "DuBlast",
    "author" : "Nicolas 'Duduf' Dufresne",
    "blender" : (2, 81, 0),
    "version" : (2,1,2),
    "location" : "Properties > Output Properties > Playblast, 3D View > View menu",
    "description" : "Create playblasts: Quickly render and play viewport animation.",
    "warning" : "",
    "category" : "Animation",
    "wiki_url": "http://dublast-docs.rainboxlab.org"
}

import bpy # pylint: disable=import-error
import os
from datetime import datetime

class DUBLAST_settings( bpy.types.PropertyGroup ):
    """Playblast settings for a scene."""

    use_camera: bpy.props.BoolProperty( name= "Use scene camera", description= "Renders using either the scene camera or the current viewport.", default= False)

    resolution_percentage: bpy.props.FloatProperty( name= "Resolution %", description= "Overrides the rendering resolution percentage for the playblast", default = 25.0, min=0.0, max= 100.0, precision=0, subtype='PERCENTAGE')
    
    use_scene_frame_range: bpy.props.BoolProperty( name= "Use scene frame range", description= "Uses the frame range of the scene.", default= True)
    frame_start: bpy.props.IntProperty( name= "Frame Start", description= "Overrides the frame start for the playblast", default = 1, min=0 )
    frame_end: bpy.props.IntProperty( name= "Frame End", description= "Overrides the frame end for the playblast", default = 250, min=0 )
    frame_step: bpy.props.IntProperty( name= "Frame Step", description= "Overrides the frame step for the playblast", default = 1, min=1 )

    filepath: bpy.props.StringProperty( name="Output Path", description="Directory/name to save playblasts", subtype="FILE_PATH")
    use_scene_name: bpy.props.BoolProperty( name= "Use scene name", description= "Uses the name of the scene when saving file.", default= True)
    use_scene_path: bpy.props.BoolProperty( name= "Use scene path", description= "Saves the file next to the scene file.", default= True)

    file_format: bpy.props.EnumProperty(
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

    color_mode: bpy.props.EnumProperty(
        items = [
            ('BW', "BW", "Images get saved in 8 bits grayscale.", '', 1),
            ('RGB', "RGB", "Images are saved with RGB (color) data.", '', 2),
            ('RGBA', "RGBA", "Images are saved with RGB and Alpha data (if supported).", '', 3)
        ],
        name = "Color",
        description= "Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels",
        default= 'RGB'
        )

    color_mode_no_alpha: bpy.props.EnumProperty(
        items = [
            ('BW', "BW", "Images get saved in 8 bits grayscale.", '', 1),
            ('RGB', "RGB", "Images are saved with RGB (color) data.", '', 2)
        ],
        name = "Color",
        description= "Choose BW for saving grayscale images, RGB for saving red, green and blue channels.",
        default= 'RGB'
        )
    
    compression: bpy.props.IntProperty( name= "Compression", description= "Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output", default = 15, min=0, max = 100 )
    quality: bpy.props.IntProperty( name= "Quality", description= "Quality for image formats that support lossy compression", default = 50, min=0, max = 100 )

    use_stamp: bpy.props.BoolProperty( name= "Burn Metadata into image", description= "Render the stamp info text in the rendered image", default= True)

    use_stamp_date: bpy.props.BoolProperty( name= "Date", description= "Include the current date", default= True)
    use_stamp_time: bpy.props.BoolProperty( name= "Time", description= "Include the current time", default= False)
    use_stamp_render_time: bpy.props.BoolProperty( name= "Render Time", description= "Include the render time", default= False)
    use_stamp_frame: bpy.props.BoolProperty( name= "Frame", description= "Include the current frame", default= True)
    use_stamp_frame_range: bpy.props.BoolProperty( name= "Frame Range", description= "Include the frame range", default= False)
    use_stamp_memory: bpy.props.BoolProperty( name= "Memory", description= "Include memory usage", default= False)
    use_stamp_hostname: bpy.props.BoolProperty( name= "Hostname", description= "Include the name of the computer", default= True)
    use_stamp_camera: bpy.props.BoolProperty( name= "Camera", description= "Include the name of the camera", default= True)
    use_stamp_lens: bpy.props.BoolProperty( name= "Lens", description= "Include the focal length", default= True)
    use_stamp_scene: bpy.props.BoolProperty( name= "Scene", description= "Include the name of the scene", default= False)
    use_stamp_marker: bpy.props.BoolProperty( name= "Marker", description= "Include the name of the last marker.", default= False)
    use_stamp_filename: bpy.props.BoolProperty( name= "Filename", description= "Include the name of the file.", default= True)
    use_stamp_note: bpy.props.BoolProperty( name= "Note", description= "Include a custom note", default= False)
    stamp_note_text: bpy.props.StringProperty( name= "Stamp Note text", description="Custom text to appear in the stamp note", default="")

    include_annotations: bpy.props.BoolProperty( name= "Include Annotations", description= "Includes the annotations", default= True)

class DUBLAST_PT_playblast_settings(bpy.types.Panel):
    bl_label = "Playblast"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'BLENDER_RENDER'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        playblast_settings = bpy.context.scene.playblast
        layout.operator('render.playblast', text="Playblast (overwrite)", icon= 'FILE_MOVIE')
        layout.operator('render.playblast', text="Playblast (increment)", icon= 'FILE_MOVIE').overwrite = False
        layout.prop(playblast_settings, 'include_annotations')

class DUBLAST_PT_dimensions( bpy.types.Panel ):
    bl_label = "Dimensions"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_parent_id = "DUBLAST_PT_playblast_settings"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast

        layout.prop( playblast_settings, "use_camera" )

        layout.prop( playblast_settings, "resolution_percentage", slider = True )

        layout.prop( playblast_settings, "use_scene_frame_range" )
        if not playblast_settings.use_scene_frame_range:
            layout.prop( playblast_settings, "frame_start" )  
            layout.prop( playblast_settings, "frame_end" )       
            layout.prop( playblast_settings, "frame_step" )

class DUBLAST_PT_output( bpy.types.Panel ):
    bl_label = "Output"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_parent_id = "DUBLAST_PT_playblast_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast

        layout.prop( playblast_settings, "use_scene_path")
        if not playblast_settings.use_scene_path:
            layout.prop( playblast_settings, "use_scene_name")
            layout.prop( playblast_settings, "filepath" )
        layout.prop( playblast_settings, "file_format" )
        if playblast_settings.file_format == 'PNG':
            layout.prop( playblast_settings, "color_mode" )
            layout.prop( playblast_settings, "compression", slider = True )
        else:
            layout.prop( playblast_settings, "color_mode_no_alpha" )
            layout.prop( playblast_settings, "quality", slider = True )

class DUBLAST_PT_stamp( bpy.types.Panel ):
    bl_label = "Burn metadata into image"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_parent_id = "DUBLAST_PT_playblast_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self,context):
        layout = self.layout
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast
        layout.prop( playblast_settings, "use_stamp", text ="" )


    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        playblast_settings = bpy.context.scene.playblast
        
        if bpy.app.version[0] >= 2 and bpy.app.version[1] >= 90:
            col = layout.column(heading="Include")
        else:
            col = layout
        col.prop( playblast_settings, "use_stamp_date" )
        col.prop( playblast_settings, "use_stamp_render_time" )
        col.prop( playblast_settings, "use_stamp_time" )
        col.prop( playblast_settings, "use_stamp_frame" )
        col.prop( playblast_settings, "use_stamp_frame_range" )
        col.prop( playblast_settings, "use_stamp_memory" )
        col.prop( playblast_settings, "use_stamp_hostname" )
        col.prop( playblast_settings, "use_stamp_camera" )
        col.prop( playblast_settings, "use_stamp_lens" )
        col.prop( playblast_settings, "use_stamp_scene" )
        col.prop( playblast_settings, "use_stamp_marker" )
        col.prop( playblast_settings, "use_stamp_filename" )
        col.prop( playblast_settings, "use_stamp_note" )
        if playblast_settings.use_stamp_note:
            col.prop( playblast_settings, "stamp_note_text" )
     
class DUBLAST_OT_playblast( bpy.types.Operator ):
    """Renders and plays an animation playblast."""
    bl_idname = "render.playblast"
    bl_label = "Animation Playblast"
    bl_description = "Render and play an animation playblast."
    bl_option = {'REGISTER'}

    overwrite: bpy.props.BoolProperty(default = True)

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):

        scene = context.scene
        playblast = scene.playblast
        render = scene.render

        # Setup Annotations (convert to grease pencil)
        annotationsObj = None
        annotationsData = scene.grease_pencil
        # Blender 2.x : we need to convert annotations to actual grease pencil
        if playblast.include_annotations and bpy.app.version[0] < 3 and annotationsData:
                # Create object and add to scene
                annotationsObj = bpy.data.objects.new("Annotations", annotationsData)
                scene.collection.objects.link(annotationsObj)
                annotationsObj.show_in_front = True
                annotationsData = annotationsObj.data
                annotationsData.stroke_thickness_space = 'SCREENSPACE'
                for layer in annotationsData.layers:
                    if bpy.app.version[0] >= 0 and bpy.app.version[1] >= 90:
                        layer.use_lights = False
                    layer.tint_color = layer.channel_color
                    layer.tint_factor = 1.0
                    thickness = annotationsObj.grease_pencil_modifiers.new("Thickness", 'GP_THICK')
                    thickness.normalize_thickness = True
                    thickness.thickness = layer.thickness
                    thickness.layer = layer.info
        # Blender 3.x : annotations are visible by default, we need to hide them
        annotationLayersVisibility = []
        if not playblast.include_annotations and bpy.app.version[0] >= 3 and annotationsData:
            for layer in annotationsData.layers:
                annotationLayersVisibility.append(layer.annotation_hide)
                layer.annotation_hide = True


        # Keep previous values
        resolution_percentage = render.resolution_percentage
        resolution_x = render.resolution_x
        resolution_y = render.resolution_y
        frame_start = scene.frame_start
        frame_end = scene.frame_end
        frame_step = scene.frame_step
        filepath = render.filepath
        file_format = render.image_settings.file_format
        color_mode = render.image_settings.color_mode
        quality = render.image_settings.quality
        compression = render.image_settings.compression
        use_stamp = render.use_stamp
        stamp_font_size = render.stamp_font_size
        color_depth = render.image_settings.color_depth

        use_stamp_date = render.use_stamp_date
        use_stamp_render_time = render.use_stamp_render_time
        use_stamp_time = render.use_stamp_time
        use_stamp_frame = render.use_stamp_frame
        use_stamp_frame_range = render.use_stamp_frame_range
        use_stamp_memory = render.use_stamp_memory
        use_stamp_hostname = render.use_stamp_hostname
        use_stamp_camera = render.use_stamp_camera
        use_stamp_lens = render.use_stamp_lens
        use_stamp_scene = render.use_stamp_scene
        use_stamp_marker = render.use_stamp_marker
        use_stamp_filename = render.use_stamp_filename
        use_stamp_note = render.use_stamp_note
        stamp_note_text = render.stamp_note_text

        codec = render.ffmpeg.codec
        scformat = render.ffmpeg.format
        constant_rate_factor = render.ffmpeg.constant_rate_factor
        gopsize = render.ffmpeg.gopsize
        audio_codec = render.ffmpeg.audio_codec
        audio_bitrate = render.ffmpeg.audio_bitrate
        ffmpeg_preset = render.ffmpeg.ffmpeg_preset 

        # Set playblast settings
        render.resolution_percentage = 100
        render.resolution_x = int( playblast.resolution_percentage / 100 * render.resolution_x )
        render.resolution_y = int( playblast.resolution_percentage / 100 * render.resolution_y )
        if render.resolution_x % 4 != 0:
            render.resolution_x = render.resolution_x - (render.resolution_x % 4)
        if render.resolution_y % 4 != 0:
            render.resolution_y = render.resolution_y - (render.resolution_y % 4)

        if not playblast.use_scene_frame_range:
            scene.frame_start = playblast.frame_start
            scene.frame_end = playblast.frame_end
            scene.frame_step = playblast.frame_step

        blend_filepath = bpy.data.filepath
        blend_dir = os.path.dirname(blend_filepath)
        blend_file = bpy.path.basename(blend_filepath)
        blend_name = os.path.splitext(blend_file)[0]

        if playblast.use_scene_path and not blend_filepath == "":
            playblast.filepath = blend_dir + "/"
            playblast.use_scene_name = True
        if playblast.filepath == "":
            playblast.filepath = render.filepath
        
        if playblast.use_scene_name:
            if not scene.name == "Scene" or blend_name == "":
                name = scene.name + "_"
            else:
                name = blend_name + "_"
            if not playblast.filepath.endswith("/") and not playblast.filepath.endswith("\\"):
                playblast.filepath = playblast.filepath + "/"
            render.filepath = playblast.filepath + name
        else:
            render.filepath = playblast.filepath

        if not self.overwrite:
            # Let's just add the date in the name
            render.filepath = render.filepath + datetime.now().isoformat(sep=' ', timespec='seconds').replace(':', '-') + '_'
            
           
        if playblast.file_format == 'MP4':
            render.image_settings.file_format = 'FFMPEG'
            render.ffmpeg.format = 'MPEG4'
            render.ffmpeg.codec = 'H264'
            if playblast.quality < 17:
                render.ffmpeg.constant_rate_factor = 'LOWEST'
            elif playblast.quality < 33:
                render.ffmpeg.constant_rate_factor = 'VERYLOW'
            elif playblast.quality < 50:
                render.ffmpeg.constant_rate_factor = 'LOW'
            elif playblast.quality < 67:
                render.ffmpeg.constant_rate_factor = 'MEDIUM'
            elif playblast.quality < 85:
                render.ffmpeg.constant_rate_factor = 'HIGH'
            elif playblast.quality < 100:
                render.ffmpeg.constant_rate_factor = 'PERC_LOSSLESS'
            else:
                render.ffmpeg.constant_rate_factor = 'LOSSLESS'
            render.ffmpeg.ffmpeg_preset = 'REALTIME'
            render.ffmpeg.gopsize = 1
            render.ffmpeg.audio_codec = 'AAC'
            render.ffmpeg.audio_bitrate = 128
        else:
            render.image_settings.file_format = playblast.file_format
        if playblast.file_format == 'PNG':
            render.image_settings.color_mode = playblast.color_mode
        else:
            render.image_settings.color_mode = playblast.color_mode_no_alpha
        render.image_settings.quality = playblast.quality
        render.image_settings.compression = playblast.compression

        render.use_stamp = playblast.use_stamp
        render.stamp_font_size = int( render.stamp_font_size * playblast.resolution_percentage / 100 )

        render.use_stamp_date = playblast.use_stamp_date
        render.use_stamp_render_time = playblast.use_stamp_render_time
        render.use_stamp_time = playblast.use_stamp_time
        render.use_stamp_frame = playblast.use_stamp_frame
        render.use_stamp_frame_range = playblast.use_stamp_frame_range
        render.use_stamp_memory = playblast.use_stamp_memory
        render.use_stamp_hostname = playblast.use_stamp_hostname
        render.use_stamp_camera = playblast.use_stamp_camera
        render.use_stamp_lens = playblast.use_stamp_lens
        render.use_stamp_scene = playblast.use_stamp_scene
        render.use_stamp_marker = playblast.use_stamp_marker
        render.use_stamp_filename = playblast.use_stamp_filename
        render.use_stamp_note = playblast.use_stamp_note
        render.stamp_note_text = playblast.stamp_note_text
        
        # Render and play
        bpy.ops.render.opengl( animation = True, view_context = not playblast.use_camera )
        bpy.ops.render.play_rendered_anim( )

        # Re-set settings
        render.resolution_percentage = resolution_percentage
        render.resolution_x = resolution_x
        render.resolution_y = resolution_y
        scene.frame_start = frame_start
        scene.frame_end = frame_end
        scene.frame_step = frame_step
        render.filepath = filepath
        render.image_settings.file_format = file_format
        render.image_settings.color_mode = color_mode
        render.image_settings.quality = quality
        render.image_settings.compression = compression
        render.image_settings.color_depth = color_depth
        render.use_stamp = use_stamp
        render.stamp_font_size = stamp_font_size
        render.ffmpeg.format = scformat
        render.ffmpeg.codec = codec
        render.ffmpeg.constant_rate_factor = constant_rate_factor
        render.ffmpeg.ffmpeg_preset = ffmpeg_preset 
        render.ffmpeg.gopsize = gopsize
        render.ffmpeg.audio_codec = audio_codec
        render.ffmpeg.audio_bitrate = audio_bitrate

        render.use_stamp_date = use_stamp_date
        render.use_stamp_render_time = use_stamp_render_time
        render.use_stamp_time = use_stamp_time
        render.use_stamp_frame = use_stamp_frame
        render.use_stamp_frame_range = use_stamp_frame_range
        render.use_stamp_memory = use_stamp_memory
        render.use_stamp_hostname = use_stamp_hostname
        render.use_stamp_camera = use_stamp_camera
        render.use_stamp_lens = use_stamp_lens
        render.use_stamp_scene = use_stamp_scene
        render.use_stamp_marker = use_stamp_marker
        render.use_stamp_filename = use_stamp_filename
        render.use_stamp_note = use_stamp_note
        render.stamp_note_text = stamp_note_text

        # Remove annotations
        if annotationsObj:
            bpy.data.objects.remove(annotationsObj)

        # Reset annnotation visibility
        if not playblast.include_annotations and bpy.app.version[0] >= 3 and annotationsData:
            for i, layer in enumerate(annotationsData.layers):
                layer.annotation_hide = annotationLayersVisibility[i]

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.separator()
    self.layout.operator('render.playblast', text="Animation playblast (overwrite)", icon= 'FILE_MOVIE')
    self.layout.operator('render.playblast', text="Animation playblast (increment)", icon= 'FILE_MOVIE').overwrite = False

classes = (
    DUBLAST_settings,
    DUBLAST_PT_playblast_settings,
    DUBLAST_PT_dimensions,
    DUBLAST_PT_output,
    DUBLAST_PT_stamp,
    DUBLAST_OT_playblast,
)

addon_keymaps = []

def register():
    # register
    for cls in classes:
        bpy.utils.register_class(cls)

    # New playblast attribute in the scenes
    if not hasattr( bpy.types.Scene, 'playblast' ):
        bpy.types.Scene.playblast = bpy.props.PointerProperty( type=DUBLAST_settings )

    # menus
    bpy.types.VIEW3D_MT_view.append(menu_func)

    # keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Playblast', space_type='VIEW_3D')
        kmi = km.keymap_items.new('render.playblast', 'RET', 'PRESS', ctrl=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # unregister
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    # menu
    bpy.types.VIEW3D_MT_view.remove(menu_func)

    # keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # attributes
    del bpy.types.Scene.playblast

if __name__ == "__main__":
    register()
