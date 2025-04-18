import tkinter as tk
from tkinter import ttk, filedialog
from pynput.mouse import Listener, Button
from ListAction import ListAction
from LeftMousePress import LeftMousePress
from RightMousePress import RightMousePress
from Node import Node
from LeftMouseRelease import LeftMouseRelease
from RightMouseRelease import RightMouseRelease
from KeyboardPress import KeyboardPress
from KeyboardRelease import KeyboardRelease
from Delay import Delay
import pickle
from MouseMove import MouseMove
from ControllerSingleton import ControllerSingleton
from MouseScroll import MouseScroll
import ctypes
import threading
from datetime import datetime
from pynput.keyboard import Listener as KeyboardListener, Key
from PIL import Image, ImageTk

PROCESS_PER_MONITOR_DPI_AWARE=2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


class MacroRecorderApp:
    def __init__(self, root):
        self.root = root
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.delay_var = tk.BooleanVar(value=True)
        self.root.title("MACROMORPH")
        self.root.geometry("800x400")
        
        self.instruction_label = tk.Label(self.root, text="If you want to stop the playback, press ESC", font=("Arial", 40), fg="red")
        self.list_thread = None

        self.record_img = ImageTk.PhotoImage(Image.open("images/record.png").resize((60, 60)))
        self.stop_img = ImageTk.PhotoImage(Image.open("images/stop.png").resize((60, 60)))
        self.play_img = ImageTk.PhotoImage(Image.open("images/start.png").resize((60, 60)))
        self.save_img = ImageTk.PhotoImage(Image.open("images/save.png").resize((60, 60)))
        self.load_img = ImageTk.PhotoImage(Image.open("images/load.png").resize((60, 60)))

        # Setup UI
        self.create_buttons()
        self.create_table()
      


        self.listener = Listener(
            on_click=self.on_click,
            on_move=self.on_move,
            on_scroll=self.on_scroll
        )

        self.keyboard_listener = KeyboardListener(
            on_press=self.on_key_press,
            on_release=self.on_release
        )
       

        
        self.recording = False
        self.controller = ControllerSingleton().get_controller()
        self.listAction = ListAction()


    def on_closing(self):
        print("Window is closing!")
        self.listener.stop()
        self.keyboard_listener.stop()
        root.destroy()  

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        record_button = tk.Button(button_frame, image=self.record_img, command=self.on_record, borderwidth=0)
        record_button.grid(row=0, column=0, padx=15)

        stop_button = tk.Button(button_frame, image=self.stop_img, command=self.on_stop, borderwidth=0)
        stop_button.grid(row=0, column=1, padx=15)

        play_button = tk.Button(button_frame, image=self.play_img, command=self.on_play, borderwidth=0)
        play_button.grid(row=0, column=2, padx=15)


        save_button = tk.Button(button_frame, image=self.save_img, command=self.on_save, borderwidth=0)
        save_button.grid(row=0, column=3, padx=15)

        load_button = tk.Button(button_frame, image=self.load_img, command=self.on_load, borderwidth=0)
        load_button.grid(row=0, column=4, padx=15)


        delay_checkbox = tk.Checkbutton(button_frame, text="Delay", variable=self.delay_var)
        delay_checkbox.grid(row=0, column=5, padx=15)

    def create_table(self):
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=("Action", "Value"), show="headings", height=15)
        self.tree.heading("Action", text="Action")
        self.tree.heading("Value", text="Value")

        self.tree.column("Action", anchor="center", width=200)
        self.tree.column("Value", anchor="center", width=300)
        self.tree.pack(fill="both", expand=True)

    def on_record(self):
        self.clear_table()
        self.tree.insert("", "end", values=("Record", "Started"))
        self.recording = True
        self.listAction = ListAction()
        start_pos = self.controller.position
        self.listAction.append(MouseMove(start_pos[0], start_pos[1]))
        self.listAction.append(MouseScroll(start_pos[0], start_pos[1]))
            

    def on_stop(self):
        self.listAction.stop()
        if self.list_thread:
            self.list_thread.join()
        self.recording = False
        

    
    def load_tree(self):
        _head = self.listAction.head
       
        while _head:
            if isinstance(_head.data, LeftMousePress):
                self.tree.insert("", tk.END, values=("Mouse left click", f"({_head.data.x}, {_head.data.y})"))

            if isinstance(_head.data, RightMousePress):
                self.tree.insert("", tk.END, values=("Mouse left click", f"({_head.data.x}, {_head.data.y})"))

            if isinstance(_head.data, KeyboardPress):
                self.tree.insert("", tk.END, values=("Key press", f"({_head.data.key})"))

            _head = _head.next
            



    def on_save(self):
        
        _head = self.listAction.head
        if not _head:
            return
        action_arr = list()
        file_path = filedialog.asksaveasfilename(
        defaultextension=".pkl",
        filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")],
        title="Save your macro"
        )


        if file_path:
            while _head:
                action_arr.append(_head.data)
                _head = _head.next
            with open(file_path, 'wb') as f:
                pickle.dump(action_arr, f)
                print(f"List saved to: {file_path}")
        else:
            print("Save canceled")
    

    def on_load(self):
        file_path = filedialog.askopenfilename(
        defaultextension=".pkl",
        filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")],
        title="Open a Pickle File"
        )

        if not file_path:
            return

        self.clear_table()
        self.listAction = ListAction()
        self.listAction.load_from_pickel_file(file_path)
        self.load_tree()

        

        
        

    def clear_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

    def on_play(self):
        self.listAction.stop()
        print("Playing back the recorded Macro")
        self.listAction.traverse(self.delay_var.get())
        self.instruction_label.pack(pady=(0, 40))
        print("finished")



    
    def create_treeview(self):
        columns = ("Action", "Value")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)

       

        self.tree.pack(fill=tk.BOTH, expand=True)


    def on_click(self, x, y, button, pressed):
        if self.recording:
            if pressed:
                if button == Button.left:
                    self.listAction.append(LeftMousePress())
                    self.tree.insert("", tk.END, values=("Mouse left click", f"({x}, {y})"))
                if button == Button.right:
                    self.tree.insert("", tk.END, values=("Mouse right click", f"({x}, {y})"))
                    self.listAction.append(RightMousePress())
            else:
                if button == Button.left:
                    self.listAction.append(LeftMouseRelease())
                if button == Button.right:
                    self.listAction.append(RightMouseRelease())


    def on_key_press(self, key):
        if key == Key.esc:
            self.listAction.stop()
            if self.list_thread:
                self.list_thread.join()
        if not self.recording:
            if key == Key.f2: #start
                print("Recording Started")
                self.tree.insert("", "end", values=("Record", "Started"))
                self.listAction = ListAction()
                start_pos = self.controller.position
                self.listAction.append(MouseMove(start_pos[0], start_pos[1]))
                self.listAction.append(MouseScroll(start_pos[0], start_pos[1]))
                self.recording = True
            if key == Key.f10: #play
                self.instruction_label.pack()
                self.listAction.stop()
                if self.list_thread:
                    self.list_thread = None
                self.list_thread = threading.Thread(target=self.listAction.traverse, args=[self.delay_var.get()])
                self.list_thread.start()
                print("finished the playback")
                self.tree.insert("", "end", values=("Record", "Ended"))

           
        else:
            if key == Key.f12: #end
                self.recording = False
           
            else:
                self.tree.insert("", tk.END, values=("Key press", key))
                last_start_time = self.listAction.tail.data.start_time
                _delay = datetime.now() - last_start_time
                self.listAction.append(Delay(_delay))
                self.listAction.append(KeyboardPress(key))
        
    
    def on_scroll(self, x, y, dx, dy):
        if self.recording:
            last_start_time = self.listAction.tail.data.start_time
            _delay = datetime.now() - last_start_time
            self.listAction.append(Delay(_delay))
            self.listAction.append(MouseScroll(dx, dy))
        
    

    def on_release(self, key):
        if self.recording:
            last_start_time = self.listAction.tail.data.start_time
            _delay = datetime.now() - last_start_time
            self.listAction.append(Delay(_delay))
            self.listAction.append(KeyboardRelease(key))


    
    def on_move(self, x, y):
        if self.recording:
            last_start_time = self.listAction.tail.data.start_time
            _delay = datetime.now() - last_start_time
            self.listAction.append(Delay(_delay))
            self.listAction.append(MouseMove(x, y))

    def start(self):
        print("Event Listener Started!")
        self.listener.start()
        self.keyboard_listener.start()
        self.listener.join()
        self.keyboard_listener.join()

# Run the app
if __name__ == "__main__":
    import threading
    root = tk.Tk()
    
    app = MacroRecorderApp(root)
    appThread = threading.Thread(target = app.start, daemon=True)
    appThread.start()
    root.mainloop()
    appThread.join()
    
