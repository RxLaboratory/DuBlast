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

#TODO include in DuRPresets
#TODO add operator for create (and play) playblast

bl_info = {
    "name" : "DuBlast",
    "author" : "Nicolas 'Duduf' Dufresne",
    "blender" : (2, 81, 0),
    "version" : (0, 0, 1),
    "location" : "Render Properties, 3D View > View menu, 3D View > Sidebar (N) > Tool tab",
    "description" : "Create playblasts: Quickly render and play viewport animation.",
    "warning" : "",
    "category" : "Animation",
    "wiki_url": "http://dublast-docs.rainboxlab.org"
}

import bpy # pylint: disable=import-error

from . import (
    dublf,
)

class DUBLAST_settings( bpy.types.PropertyGroup ):
    """Playblast settings for a scene."""

    resolution_percentage: bpy.props.FloatProperty( name= "Resolution %", description= "Overrides the rendering resolution percentage for the playblast", default = 25.0, min=0.0, max= 100.0, precision=0, subtype='PERCENTAGE')
    frame_start: bpy.props.IntProperty( name= "Frame Start", description= "Overrides the frame start for the playblast", default = 1, min=0 )
    frame_end: bpy.props.IntProperty( name= "Frame End", description= "Overrides the frame end for the playblast", default = 250, min=0 )
    frame_step: bpy.props.IntProperty( name= "Frame Step", description= "Overrides the frame step for the playblast", default = 1, min=1 )

    filepath: bpy.props.StringProperty( name="Output Path", description="Directory/name to save playblasts")

    file_format: bpy.props.EnumProperty(
        items = [
            ('PNG', "PNG", "Output image in PNG format.", 'FILE_IMAGE', 1),
            ('JPEG', "JPEG", "Output image in JPEG format.", 'FILE_IMAGE', 2),
            ('AVI_JPEG', "AVI JPEG", "Output video in AVI JPEG format.", 'FILE_MOVIE', 3)
        ],
        name = "File Format",
        description= "File format to save the playblasts",
        default= 'AVI_JPEG'
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
    
    compression: bpy.props.IntProperty( name= "Compression", description= "Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output", default = 15, min=0, max = 100 )
    quality: bpy.props.IntProperty( name= "Quality", description= "Quality for image formats that support lossy compression", default = 50, min=0, max = 100 )

    use_stamp: bpy.props.BoolProperty( name= "Burn Metadata into image", description= "Render the stamp info text in the rendered image.", default= True)

class DUBLAST_PT_playblast_settings(bpy.types.Panel):
    bl_label = "Playblast Settings"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'BLENDER_RENDER'}

    def draw(self, context):
        layout = self.layout

        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast


        b = layout.box()
        b.prop( playblast_settings, "resolution_percentage", slider = True )

        b = layout.box()

        b.prop( playblast_settings, "frame_start" )  
        b.prop( playblast_settings, "frame_end" )       
        b.prop( playblast_settings, "frame_step" ) 

        b = layout.box()

        b.prop( playblast_settings, "filepath" )
        b.prop( playblast_settings, "file_format" )
        b.prop( playblast_settings, "color_mode" )
        if playblast_settings.file_format == 'PNG':
            b.prop( playblast_settings, "compression", slider = True )
        else:
            b.prop( playblast_settings, "quality", slider = True )

        b = layout.box()

        b.prop( playblast_settings, "use_stamp" )

classes = (
    DUBLAST_settings,
    DUBLAST_PT_playblast_settings,
)

addon_keymaps = []

def register():
    # register
    for cls in classes:
        bpy.utils.register_class(cls)

    if not hasattr( bpy.types.Scene, 'playblast' ):
        bpy.types.Scene.playblast = bpy.props.PointerProperty( type=DUBLAST_settings )

def unregister():
    # unregister
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.playblast

if __name__ == "__main__":
    register()
