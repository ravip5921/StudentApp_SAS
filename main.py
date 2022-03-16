from glob import escape
import server.client_student


import cv2
import face_recognition
import os

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
Window.top = 50
Window.size = (540, 960)
filePresent = True
pictureRemoved = False
try:
    fileP = open("./userData.txt", "r")
except:
    filePresent = False
    pass


class StudentApp(MDApp):
    rollNoSaved = ""

    def build(self):
        # app LOGO
        # self.imageObj = Image(source="./assets/logo.png")
        # # layout for image of logo
        # self.imageLayout = BoxLayout(size_hint=(0.2, 0.2),
        #                              pos_hint={'x': 0.05})
        # self.imageLayout.add_widget(self.imageObj)
        # widgets for input
        # self.rollNoL = MDLabel(text="Roll No:")
        # self.AttendanceCodeL = MDLabel(text="Attendance Code: ")

        # self.rollNoL = MDLabel(text=" ",
        #                        size_hint=(0.9, 0.1))
        # self.AttendanceCodeL = MDLabel(text=" ",
        #                                size_hint=(0.9, 0.25),
        #                                pos_hint={'center_x': 0.5, 'center_y': 0.25})

        self.rollNoT = MDTextField(hint_text="Enter Roll no :")  # ,
        # size_hint=(0.9, 0.5),
        # pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # self.AttendanceCodeT = MDTextField(
        #     hint_text="Enter Attendance Code : ",
        #     size_hint=(0.9, 0.25),
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5}
        # )

        inputLayout = BoxLayout(orientation="vertical")
        # size_hint=(0.8, 0.8),
        # pos_hint={'center_x': 0.5, 'center_y': 0.5}
        # )

        # setting text of roll no from saved file
        # if filePresent:
        #     self.rollNoT.text = fileP.readline()

        # Adding widgets for input to input layout
        # inputLayout.add_widget(self.rollNoL)
        inputLayout.add_widget(self.rollNoT)
        # inputLayout.add_widget(self.AttendanceCodeL)
        # inputLayout.add_widget(self.AttendanceCodeT)

        # Message label
        # self.messageL = MDLabel(text="Authenticate your face:")
        # # Layout for Message
        # messageLayout = BoxLayout(orientation="vertical",
        #                           size_hint=(1, 1),
        #                           pos_hint={'center_x': 0.5, 'center_y': 0.5}
        #                           )

        # messageLayout.add_widget(self.messageL)

        # cameraLayout = BoxLayout(size_hint=(0.9, 0.4),
        #                          pos_hint={'x': 0.05, 'y': 0.2}
        #                          )
        # Camera object
        # self.cameraObj = Camera()
        # self.cameraObj.resolution = (480, 480)
        # cameraLayout.add_widget(self.cameraObj)
        # # Capture Button
        # self.buttonObj = MDRaisedButton(text="Capture")
        # self.buttonObj.size_hint = (.2, .10)
        # self.buttonObj.pos_hint = {'x': .40, 'y': .2}
        # self.buttonObj.bind(on_press=self.takeImage)
        # layout for camera and capture button
        myBoxLayout = BoxLayout(orientation="vertical")
        # myBoxLayout.add_widget(self.imageLayout)
        # myBoxLayout.add_widget(inputLayout)
        # myBoxLayout.add_widget(messageLayout)
        # myBoxLayout.add_widget(cameraLayout)
        # myBoxLayout.add_widget(self.buttonObj)

        return inputLayout

    # def takeImage(self, *args):
    #     self.filename = str(self.rollNoT.text + "+" +
    #                         self.AttendanceCodeT.text+".png")
    #     self.rollNo = str(self.rollNoT.text)
    #     self.acode = self.AttendanceCodeT.text
    #     print(self.filename)

    #     try:
    #         self.cameraObj.export_to_png(self.filename)
    #         imag = face_recognition.load_image_file(self.filename)
    #         imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    #         self.encodingsData = face_recognition.face_encodings(imag)
    #         if len(self.encodingsData) > 0:
    #             self.encodingsData = self.encodingsData[0]
    #             self.encodingsData = self.encodingsData.tolist()

    #             dataFromServer = server.client_student.markAttendance(
    #                 self.rollNo, int(self.acode), self.encodingsData)
    #             # print(dataFromServer)
    #             if "error" in dataFromServer:
    #                 print(dataFromServer["error"])
    #                 self.messageL.text = str(dataFromServer["error"])
    #             else:
    #                 print(dataFromServer["success"])
    #                 self.messageL.text = str(dataFromServer["success"])
    #             os.remove(self.filename)
    #             pictureRemoved = True
    #             if filePresent:
    #                 os.remove("./userData.txt")

    #             fileP = open("./userData.txt", "w")
    #             fileP.write(self.rollNo)
    #         else:
    #             self.messageL.text = "No Face Detected. Try again!"
    #             os.remove(self.filename)
    #     except Exception as e:
    #         # print("No face detected.")
    #         print("error :", e)
    #         if not pictureRemoved:
    #             os.remove(self.filename)
    #         self.encodingsData = None


if __name__ == "__main__":
    StudentApp().run()
