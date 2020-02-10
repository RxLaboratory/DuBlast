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

# The Duduf Blender Framework
# Useful tools to develop scripts in Blender

import bpy # pylint: disable=import-error
import time
import re
import json
import inspect
from . import rigging

# ========= UTILS ======================

class DUBLF_utils():
    """Utilitaries for Duduf's tools"""
    
    toolName = "Dublf"
    
    def log( self, log = "", time_start = 0 ):
        """Logs Duik activity"""
        t = time.time() - time_start
        print( " ".join( [ self.toolName , " (%.2f s):" % t , log ] ) )
        
    def showMessageBox( self, message = "", title = "Message Box", icon = 'INFO'):
        """Displays a simple message box"""
        def draw(self, context):
            self.layout.alert = True
            self.layout.label(text = message)
        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

# ========= STRING METHODS =============

class DUBLF_string():
    """Useful string methods"""

    @staticmethod
    def get_baseName( filename ):
        """Gets the name part of a filename without the extension"""
        fileBaseName = filename
        fileBaseNameList = filename.split('.')
        if len(fileBaseNameList) > 1:
            fileBaseName = '.'.join(fileBaseNameList[0:-1])
        return fileBaseName

# ========== JSON METHODS ==============

class DUBLF_json():
    """Useful json methods"""

    @staticmethod
    def isSerializable( val ):
        """Checks if the value is one of the type serializable as a JSON object"""
        t = type(val)
        return t is list or t is dict or t is str or t is float or t is int or t is bool

    @staticmethod
    def serialize( obj ):
        """Transform any python object to a JSON serializable pyhton object
        This method is not recursive, i.e. it will ignore nested objects and get only strings, numbers, booleans, lists"""
        serializedObj = {}
        for member in inspect.getmembers( obj ):
            if member[0].startswith("__"):
                continue
            if DUBLF_json.isSerializable( member[1] ):
                serializedObj[member[0]] = member[1] 
        return serializedObj

# ========= File System METHODS ========

class DUBLF_fs():
    """Useful File System methods"""

    @staticmethod
    def get_fileBaseName( file ):
        """Gets the name part of a file without the extension"""
        filename = ""
        if isinstance(file, bpy.types.OperatorFileListElement):
            filename = file.name
        else:
            try:
                filename = file.stem
            except:
                pass
        return DUBLF_string.get_baseName(filename)

# ========= HANDLERS METHODS ===========

class DUBLF_handlers():
    """Methods to help creating and removing Blender handlers"""

    @staticmethod
    def append_function_unique(fn_list, fn):
        """ Appending 'fn' to 'fn_list',
            Remove any functions from with a matching name & module.
        """
        DUBLF_handlers.remove_function(fn_list, fn)
        fn_list.append(fn)

    @staticmethod
    def remove_function(fn_list, fn):
        """Removes a function from the list, if it is there"""
        fn_name = fn.__name__
        fn_module = fn.__module__
        for i in range(len(fn_list) - 1, -1, -1):
            if fn_list[i].__name__ == fn_name and fn_list[i].__module__ == fn_module:
                del fn_list[i]

    @staticmethod
    def frame_change_pre_append( fn ):
        """Appends a function to frame_change_pre handler, taking care of duplicates"""
        DUBLF_handlers.append_function_unique( bpy.app.handlers.frame_change_pre, fn )

    @staticmethod
    def frame_change_pre_remove( fn ):
        """Removes a function from frame_change_pre handler"""
        DUBLF_handlers.remove_function( bpy.app.handlers.frame_change_pre, fn )

    @staticmethod
    def frame_change_post_append( fn ):
        """Appends a function to frame_change_pre handler, taking care of duplicates"""
        DUBLF_handlers.append_function_unique( bpy.app.handlers.frame_change_post, fn )

    @staticmethod
    def frame_change_post_remove( fn ):
        """Removes a function from frame_change_pre handler"""
        DUBLF_handlers.remove_function( bpy.app.handlers.frame_change_post, fn )

    @staticmethod
    def depsgraph_update_post_append( fn ):
        """Appends a function to frame_change_pre handler, taking care of duplicates"""
        DUBLF_handlers.append_function_unique( bpy.app.handlers.depsgraph_update_post, fn )

    @staticmethod
    def depsgraph_update_post_remove( fn ):
        """Removes a function from frame_change_pre handler"""
        DUBLF_handlers.remove_function( bpy.app.handlers.depsgraph_update_post, fn )

# ========= RNA ========================

class DuBLF_rna():
    """Methods to help rna paths"""

    @staticmethod
    def get_bpy_struct( obj_id, path):
        """ Gets a bpy_struct or property from an ID and an RNA path
            Returns None in case the path is invalid
            """
        try:
            # this regexp matches with two results: first word and what's in brackets if any
            # "prop['test']" -> [("prop", "'test'")]
            # "prop" -> [("prop","")]
            # "prop[12]" -> [("prop","12")]
            matches = re.findall( r'(\w+)?(?:\[([^\]]+)\])?' , path )
            print(matches)
            for i,match in enumerate(matches) :
                attr = match[0]
                arr = match[1]
                if i == len(matches) -2:
                    if attr != '' and  arr != '':
                        obj_id = getattr(obj_id, attr)
                        return obj_id, '[' + arr + ']'
                    elif attr != '':
                        return obj_id, attr
                    else:
                        return obj_id, '[' + arr + ']'
                if attr != '':
                    obj_id = getattr(obj_id, attr)
                if arr != '':
                    obj_id = obj_id[ eval(arr) ]
            return None           
        except:
            return None

# ========= ADDONS =====================

class DuBLF_addons():
    """Methods to work with addons"""

    @staticmethod
    def is_addon_enabled( moduleName ):
        addons = bpy.context.preferences.addons
        for addon in addons:
            if addon.module == moduleName:
                return True
        return False

def register():
    rigging.register()

def unregister():
    rigging.unregister()