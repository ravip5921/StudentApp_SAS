#!/usr/bin/env python
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.utils import platform
from kivy.clock import mainthread
from kivy.logger import Logger
from kivy.properties import NumericProperty, ObjectProperty, StringProperty


def is_android():
    return platform == 'android'

if not is_android():
    Window.size = (540, 960)
'''
Runtime permissions:
'''

def check_camera_permission():
    """
    Android runtime `CAMERA` permission check.
    """
    if not is_android():
        return True
    from android.permissions import Permission, check_permission
    permission = Permission.CAMERA
    return check_permission(permission)


def check_request_camera_permission(callback=None):
    """
    Android runtime `CAMERA` permission check & request.
    """
    had_permission = check_camera_permission()
    Logger.info("CameraAndroid: CAMERA permission {%s}.", had_permission)
    if not had_permission:
        Logger.info("CameraAndroid: CAMERA permission was denied.")
        Logger.info("CameraAndroid: Requesting CAMERA permission.")
        from android.permissions import Permission, request_permissions
        permissions = [Permission.CAMERA]
        request_permissions(permissions, callback)
        had_permission = check_camera_permission()
        Logger.info("CameraAndroid: Returned CAMERA permission {%s}.", had_permission)
    else:
        Logger.info("CameraAndroid: Camera permission granted.")
    return had_permission


perm_denied = '''
BoxLayout:
    orientation: 'vertical'
    size: root.size

    canvas:
        Color:
            rgb: 0, 0, 0
        Rectangle:
            size: self.size

    Label:
        text:"DENIED CAMERA"

'''

class RollNoInput(Widget):
    field_id = ObjectProperty(None)
    field_text = StringProperty(None)
    field_placeholder = StringProperty(None)
    # text = ""

    def getText(self):
        return self.field_text

    def getPlaceHolder(self):
        return self.field_placeholder

    def process(self, app,txt):
        if txt.text != "":
            # self.text = txt.text
            app.rollNo = txt.text
            # print(self.text)
        else:
            print("text empty")
    pass


class MainWindow(Screen):
    stdRoll = RollNoInput()
    stdRoll.field_id = ObjectProperty(None)
    stdRoll.field_text = 'Roll No:'
    stdRoll.field_placeholder = 'Enter Roll no:'
    stdRoll.text = ""
    pass


class CameraWindow(Screen):
    # def picture_taken(self, obj, filename):
    #     print('Picture taken and saved to {}'.format(filename))

    pass

class DataProcessingWindow(Screen):
    pass
class AlertWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("style.kv")


class StudentApp(App):
    rollNo = ""
    saveSuccess = False
    def build(self):
        @mainthread
        def on_permissions_callback(permissions, grant_results):    
            if all(grant_results):
                return kv
        if check_request_camera_permission(callback=on_permissions_callback):
            return kv
        else:
            return Builder.load_string(perm_denied)
    
    
    def picture_taken(self, obj, filename):
        print('Picture taken and saved to {}'.format(filename))
        self.saveSuccess = True

def main():
    StudentApp().run()

if __name__ == "__main__":
    main()
