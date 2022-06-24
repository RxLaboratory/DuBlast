import bpy
from bpy.types import Panel

class DUBLAST_PT_Playblast_Settings( Panel ):
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
        rows = layout.row(align=False)
        rows.operator('render.playblast', text="Playblast", icon= 'FILE_MOVIE')
        row = rows.row(align=True)
        row.prop(playblast_settings, 'increment', icon="LINENUMBERS_ON", toggle=True)
        row.prop(playblast_settings, 'use_stamp', icon="INFO", toggle=True)
        row.prop(playblast_settings, 'include_annotations', icon="TEXT", toggle=True)

class DUBLAST_PT_Scene( Panel ):
    bl_label = ""
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "DUBLAST_PT_Playblast_Settings"

    def draw_header(self,context):
        self.layout.label(text="Scene", icon="SCENE_DATA")

    def draw(self, context):
        layout = self.layout
        #layout.use_property_split = False
        layout.use_property_decorate = False  # No animation.
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast
        
        col = layout.column(align=False)
        col.use_property_split = True
        col.prop( playblast_settings, "use_camera") #, icon="VIEW_CAMERA"
        col.prop( playblast_settings, "use_scene_frame_range")  #, icon="PREVIEW_RANGE"
        layout.separator()
        row = col.row(align=True)

        if not playblast_settings.use_scene_frame_range:
            row = layout.row(align=True)
            row.label(text='Range')
            row.prop( playblast_settings, "frame_start" )  
            row.prop( playblast_settings, "frame_end" )
            row = layout.row(align=True)
            row.label(text='')
            row.prop( playblast_settings, "frame_step" )

class DUBLAST_PT_Shading( Panel ):
    bl_label = ""
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "DUBLAST_PT_Playblast_Settings"

    def draw_header(self,context):
        self.layout.label(text="Shading", icon="SHADING_TEXTURE")

    def draw_shading(self, layout, playblast_settings):
        layout.use_property_split = False
        layout.label(text='Lighting')
        layout.prop( playblast_settings, "light", expand=True )
        col = layout.column()
        col.label(text='Color')
        col.grid_flow(columns=3, align=True).prop(playblast_settings, "color_type", expand=True)
        if playblast_settings.color_type == 'SINGLE':
            col.row().prop(playblast_settings, "single_color") 

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = False
        layout.use_property_decorate = False  # No animation.
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast

        if playblast_settings.use_camera == False:
            layout.use_property_split = False
            layout.label(text='Viewport Shading')
            layout.prop( playblast_settings, "shading", expand=True )
            if playblast_settings.shading == "SOLID":
                self.draw_shading(layout,playblast_settings)
                col = layout.column()
                col.use_property_split = False
                col.label(text='Background')
                col.row().prop( playblast_settings, "background_type", expand=True )
                if playblast_settings.background_type == 'VIEWPORT':
                    col.row().prop(playblast_settings, "background_color")
        else:
            self.draw_shading(layout,playblast_settings)

class DUBLAST_PT_Output( Panel ):
    bl_label = ""
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_parent_id = "DUBLAST_PT_Playblast_Settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self,context):
        self.layout.label(text="Output", icon="OUTPUT")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        # Add settings for the current scene
        playblast_settings = bpy.context.scene.playblast

        layout.prop( playblast_settings, "resolution_percentage", slider = True )
        layout.prop( playblast_settings, "file_format" )
        if playblast_settings.file_format == 'PNG':
            layout.prop( playblast_settings, "color_mode" )
            layout.prop( playblast_settings, "compression", slider = True )
        else:
            layout.prop( playblast_settings, "color_mode_no_alpha" )
            layout.prop( playblast_settings, "quality", slider = True )

        #layout.use_property_split = False
        layout.prop(playblast_settings, "use_scene_path")
        col = layout.column()
        col.enabled = False
        if not playblast_settings.use_scene_path:
            col.enabled = True
        col.prop( playblast_settings, "filepath" )
        col.prop( playblast_settings, "use_scene_name")

class DUBLAST_PT_Metadata( Panel ):
    bl_label = ""
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"
    bl_parent_id = "DUBLAST_PT_Playblast_Settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self,context):
        self.layout.label(text="Metadata", icon="INFO")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        playblast_settings = bpy.context.scene.playblast
        
        layout.prop( playblast_settings, "auto_size_stamp_font" )
        row = layout.row()
        row.enabled = not playblast_settings.auto_size_stamp_font
        row.prop( playblast_settings, "font_size" )

        layout.prop( playblast_settings, "stamp_foreground" )
        layout.prop( playblast_settings, "stamp_background" )

        layout.separator()

        if bpy.app.version[0] >= 2 and bpy.app.version[1] >= 90:
            col = layout.column(heading="Include")
        else:
            col = layout

        metadata = [
            "use_stamp_camera",
            "use_stamp_date",
            "use_stamp_filename",
            "use_stamp_frame",
            "use_stamp_frame_range",
            "use_stamp_hostname",
            "use_stamp_lens",
            "use_stamp_marker",
            "use_stamp_memory",
            "use_stamp_render_time",
            "use_stamp_scene",
            "use_stamp_time",
            "use_stamp_note",
        ]

        row = None
        cf = layout.column_flow(columns=2, align=False)
        for m in metadata:
            cf.enabled = playblast_settings.use_stamp 
            cf.prop( playblast_settings, m )
            if m == "use_stamp_note" and playblast_settings.use_stamp_note == True:
                cf.enabled = playblast_settings.use_stamp
                cf.prop( playblast_settings, "stamp_note_text" )

classes = (
    DUBLAST_PT_Playblast_Settings,
    DUBLAST_PT_Scene,
    DUBLAST_PT_Shading,
    DUBLAST_PT_Output,
    DUBLAST_PT_Metadata,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)