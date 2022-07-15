#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#======================= END GPL LICENSE BLOCK ========================

# <pep8 compliant>

import bpy

class DUBLAST_Preferences( bpy.types.AddonPreferences ):
    bl_idname = __package__

    check_updates: bpy.props.BoolProperty(
        name="Daily check for updates",
        default=1,
        description="DuBlast will check once a day if an update is available for the add-on"
    )

    last_update_check: bpy.props.IntProperty(
        default=0
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "check_updates")
        layout.operator("dublf.updatebox", text="Check for updates now").addonModuleName = __package__

def register():
    bpy.utils.register_class(DUBLAST_Preferences)

def unregister():
    bpy.utils.unregister_class(DUBLAST_Preferences)