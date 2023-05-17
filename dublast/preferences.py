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
from bpy.app.handlers import persistent
from dublast import dublf

class DUBLAST_OpenURL(dublf.ops.OpenURL):
    bl_idname = "dublast.openurl"

class DUBLAST_UpdateBox(dublf.ops.UpdateBox):
    bl_idname = "dublast.updatebox"
    bl_label = "Update available"
    bl_icon = "INFO"

    discreet: bpy.props.BoolProperty(
        default=False
    )

    addonName = __package__
    openURLOp = DUBLAST_OpenURL.bl_idname

class DUBLAST_OT_ReportIssue( dublf.ops.DUBLF_OT_ReportIssue ):
    bl_idname = "dublast.reportissue"
    addonName = __package__

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
        layout.operator("dublast.updatebox", text="Check for updates now")
        layout.operator("dublast.reportissue")

@persistent
def checkUpdateHandler(arg1, arg2):
    bpy.ops.dublast.updatebox('INVOKE_DEFAULT', discreet = True)

classes = (
    DUBLAST_OpenURL,
    DUBLAST_UpdateBox,
    DUBLAST_OT_ReportIssue,
    DUBLAST_Preferences,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Check for updates after loading a blend file
    if not checkUpdateHandler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(checkUpdateHandler)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    if checkUpdateHandler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(checkUpdateHandler)
