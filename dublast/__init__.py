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
    "author" : "Nicolas 'Duduf' Dufresne, Kevin C. Burke (@blastframe)",
    "blender" : (2, 81, 0),
    "version" : (3,2,0),
    "location" : "Properties > Output Properties > Playblast, 3D View > View menu",
    "description" : "Create playblasts: Quickly render and play viewport animation.",
    "warning" : "",
    "category" : "Animation",
    "wiki_url": "http://dublast.rxlab.guide"
}

import bpy

if "bpy" in locals():
    import importlib

    if "dublf" in locals():
        importlib.reload(dublf)
    if "preferences" in locals():
        importlib.reload(preferences)
    if "properties" in locals():
        importlib.reload(properties)
    if "playblast" in locals():
        importlib.reload(playblast)
    if "panels" in locals():
        importlib.reload(panels)

from . import (dublf, properties, preferences, panels, playblast)

def menu_func(self, context):
    self.layout.separator()
    self.layout.operator('render.playblast', text="Playblast (overwrite)", icon= 'FILE_MOVIE')
    self.layout.operator('render.playblast', text="Playblast (increment)", icon= 'FILE_MOVIE').overwrite = False

def view_header_func(self, context):
    self.layout.operator('render.playblast', text="", icon= 'FILE_MOVIE')

addon_keymaps = []

modules = (
    properties,
    preferences,
    panels,
    playblast
)

def register():
    # register
    for mod in modules:
        mod.register()

    # menus
    bpy.types.VIEW3D_HT_header.append(view_header_func)
    bpy.types.VIEW3D_MT_view.append(menu_func)

    # keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Playblast', space_type='VIEW_3D')
        kmi = km.keymap_items.new('render.playblast', 'RET', 'PRESS', ctrl=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # unregister
    for mod in reversed(modules):
        mod.unregister()

    # menu
    bpy.types.VIEW3D_HT_header.remove(view_header_func)
    bpy.types.VIEW3D_MT_view.remove(menu_func)

    # keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
