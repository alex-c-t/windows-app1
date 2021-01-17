import glob
import os
import platform
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

Builder.load_string('''

#________________button_________________________
#________________button_________________________

<RoundedButton@Button>
    background_color: (0,0,0,0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (40/255,74/255,140/255,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10]

<RoundedButton1@Button>
    background_color: (0,0,0,0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (25/255,71/255,68/255,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10]

#________________button_________________________
#________________button_________________________

<SpeedUpChoice>:
    BoxLayout:
        orientation:"vertical"
        padding:15
        spacing:5
        canvas:
            Color:
                rgba:(14/255, 42/255, 74/255,1)
            Rectangle:
                pos:self.pos
                size:self.size
        BoxLayout:
            size_hint_y:.1
            orientation: "vertical"
        BoxLayout:
            size_hint_y:.4
            orientation:"vertical"
            padding:0,0,0,0
            Label:
                size_hint_y:.1
                text: "System Specification"
                text_size: self.size
                bold:True
                valign: "middle"
                padding_x:5
            BoxLayout:
                size_hint_y:.9
                orientation:"vertical"
                

                Label:
                    id:sys_info
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                   
                Label:
                    id:sys_node
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                    
                Label:
                    id:sys_release
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                    
                Label:
                    id:sys_version
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                   
                Label:
                    id:sys_machine
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                   
                Label:
                    id:sys_processor
                    text: "Name"
                    text_size: self.size
                    valign: "middle"
                    padding_x:20
                   
        BoxLayout:
            size_hint_y:.5
            orientation: "vertical"
            BoxLayout:
            GridLayout:
                padding:150,0
                spacing:5
                cols: 2
                row_default_height: '40dp'

                Button:
                    text:"Clean Temp Files"
                    on_press:
                        root.manager.transition.direction = "left"
                        root.selected_choice(1)

                Button:
                    text:"choice4"
                    on_press:
                        root.manager.transition.direction = "left"
                        root.selected_choice(2)

                Button:
                    text:"choice4"
                    on_press:
                        root.manager.transition.direction = "left"
                        root.selected_choice(3)

                Button:
                    id: log_in_out_btn
                    text: "choice4"
                    on_press:
                        root.manager.transition.direction = "left"
                        root.selected_choice(4)
            BoxLayout:
        

            
<RecycleViewRow>:
    BoxLayout:
        spacing:40
        Label:
            id:clean_size
            text:root.text 
            text_size: self.size
            valign: "middle"
        Label:
            id:clean_size
            text:root.text1
        BoxLayout:
            padding:13
            RoundedButton:
                id:clean_button
                text:"clean"
                on_release:root.button_press(root.text,root.path1)

                
<TempFiles>:
    rv:rv
    BoxLayout:
        orientation: "vertical"
        spacing:5
        padding:15
        canvas:
            Color:
                rgba:(14/255, 42/255, 74/255,1)
            Rectangle:
                pos:self.pos
                size:self.size

        BoxLayout:
            size_hint_y:.1
            orientation:"horizontal"
            spacing:10
            padding:0,50,0,0

            Label:
                text: ""
                underline: True

            Label:
                text: ""
                underline: True



            Label:
                text: ""
                underline: True

            Label:
                text: ""
                underline: True

            BoxLayout:
                size_hint_x:1.3


        BoxLayout:
            size_hint_y:.7
            orientation:"vertical"
            padding:200,0
            Label:
                size_hint_y:.1
                text: "Clear Temp Files"
                text_size: self.size
                bold:True
                valign: "middle"
                padding_x:5
            BoxLayout:
                size_hint_y:.5
                orientation:"vertical"
                RecycleView:
                    id: rv
                    viewclass: 'RecycleViewRow'
                    orientation: "vertical"
                    spacing: 15
                    padding:30
                    space_x: self.size[0]/3
                    SelectRecycleBoxLayout:
                        default_size: None, dp(50)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
                BoxLayout:
                    orientation:"vertical"
                    RoundedButton1:
                        text: 'Clean All'
                        size_hint:1,.2
                        on_press:
                            root.manager.transition.direction = "right"
                    BoxLayout:
                            
        BoxLayout:
            size_hint_y:.05
            orientation:"horizontal"
            Button:
                text: 'back'
                on_press:
                    root.manager.transition.direction = "right"
                    root.go_back()


''')
my_system = platform.uname()


class MainClass:
    def __init__(self):
        self.users_name = []
        self.temp_folder = []
        self.temp_folder_size = []
        users = glob.glob("C:\\Users\\*")
        # print(users)
        for items in users:
            if items == "C:\\Users\\public" or items == "C:\\Users\\All Users":
                users.remove(items)
            elif os.path.isfile(items):
                users.remove(items)
            else:
                self.users_name.append(items.split('\\')[-1])
                self.temp_folder.append(items + "\\AppData\\Local\\Temp")
        for usr_folder in self.temp_folder:
            self.temp_folder_size.append(format_bytes(getFolderSize(usr_folder)))


class SpeedUpChoice(Screen):
    def on_pre_enter(self, *args):
        self.ids.sys_info.text = f"System: {my_system.system}"
        self.ids.sys_node.text = f"Node Name: {my_system.node}"
        self.ids.sys_release.text = f"Release: {my_system.release}"
        self.ids.sys_version.text = f"Version: {my_system.version}"
        self.ids.sys_machine.text = f"Machine: {my_system.machine}"
        self.ids.sys_processor.text = f"Processor: {my_system.processor}"

    @staticmethod
    def selected_choice(choice):
        if choice == 1:
            sm.current = "scr_temp"
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass


class TempFiles(Screen):
    rv = ObjectProperty()

    def on_pre_enter(self, *args):
        # print(self.temp_folder)
        # for usr_folder in mc.temp_folder:
        #     mc.temp_folder_size.append(format_bytes(getFolderSize(usr_folder)))
        # print(self.users_name)
        self.rv.data = [{'text': str(user), 'text1': str(size), 'path1': str(path1)} for user, size, path1 in
                        zip(mc.users_name, mc.temp_folder_size, mc.temp_folder)]

    @staticmethod
    def delete_temp_files(usr_nm):
        del_items = glob.glob(usr_nm + "\\*")
        # print(del_items)
        for item in del_items:
            try:
                if os.path.isfile(item):
                    # os.unlink(del_item)
                    print(item, 'file')

                elif os.path.isdir(item):
                    # shutil.rmtree(del_item)
                    print(item, "dir")

            except Exception as e:
                print(e)

    @staticmethod
    def go_back():
        sm.current = "scr_home"


class SelectRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """ Adds selection and focus behaviour to the view. """


class RecycleViewRow(BoxLayout):
    text = StringProperty()
    text1 = StringProperty()
    path1 = StringProperty()

    @staticmethod
    def button_press(selected_user_temp, path1):
        proceed_popup("Clean Temp", f"Clean the Temporary files of user {selected_user_temp}", clean_confirmation=True,
                      user_name=selected_user_temp, path_to_fold=path1)


def proceed_popup_rt(clean_confirmation, user_name, path_to_fold):
    if clean_confirmation:
        sm.screens[1].delete_temp_files(path_to_fold)
        # sm.screens[4].on_enter()
        # if not delete_confirm: # info- check is the signed in user is admin.
        #     ErrorForm("Not Deleted", "Not Authorized")
    else:
        pass


def proceed_popup(title="Proceed Message", content1="Are you sure you want to proceed?", clean_confirmation=False,
                  user_name=False, path_to_fold=False):
    box = BoxLayout(orientation='vertical')
    box.add_widget(Label(text=content1))
    mybutton = Button(text='YES', size_hint=(1, 0.25))
    mybutton1 = Button(text='NO', size_hint=(1, 0.25))
    box.add_widget(mybutton)
    box.add_widget(mybutton1)
    popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
    mybutton.bind(on_release=lambda x: proceed_popup_rt(clean_confirmation, user_name, path_to_fold))
    mybutton.bind(on_release=popup.dismiss)
    mybutton1.bind(on_release=popup.dismiss)
    popup.open()


# users_name = []
# temp_folder = []
# users = glob.glob("C:\\Users\\*")
#
# for items in users:
#     if items == "C:\\Users\\public":
#         users.remove(items)
#     elif os.path.isfile(items):
#         users.remove(items)
#     else:
#         users_name.append(items.split('\\')[-1])
#         temp_folder.append(items + "\\AppData\\Local\\Temp")
#
# # give folder path to clear Temp
# # clear_fold = temp_folder[1]
# print(users_name)
# for del_item in temp_folder:
#
#     if del_item == "C:\\Users\\Admin\\AppData\\Local\\Temp":
#         del_items = glob.glob(del_item + "\\*")
#         # print(del_items)
#         for item in del_items:
#             try:
#                 if os.path.isfile(item):
#                     # os.unlink(del_item)
#                     print(item, 'file')
#
#                 elif os.path.isdir(del_item):
#                     # shutil.rmtree(del_item)
#                     print(item, "dir")
#
#             except Exception as e:
#                 print(e)

# info- convert bytes into kb,mb,gb, etc.

def format_bytes(size):
    power = 2 ** 10
    n = 0
    power_labels = {0: 'bytes', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB', 5: 'PB'}
    while size > power:
        size /= power
        n += 1
    size = round(size, 3)
    return str(size) + " " + power_labels[n]


def getFolderSize(start_path):
    total_size = 0
    # To get size of current directory
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size


class WindowManager(ScreenManager):
    pass


sm = WindowManager()

screens = [SpeedUpChoice(name="scr_home"), TempFiles(name="scr_temp")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "scr_home"

mc = MainClass()


# print(os.environ['ALLUSERSPROFILE'])
class StartApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    StartApp().run()
