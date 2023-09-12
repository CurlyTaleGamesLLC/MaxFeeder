import tkinter as tk
import serial
from tkinter.scrolledtext import ScrolledText
import threading
import keyboard

class SerialCommunicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MAXFeeder Tester")
        self.serial_ports = self.list_serial_ports()
        
        # Create a frame for the serial port connection widgets
        serial_frame = tk.Frame(root)
        serial_frame.grid(row=0, column=0, sticky="ew")
        
        tk.Label(serial_frame, text="Serial Port:").grid(row=0, column=0)
        self.serial_port_var = tk.StringVar(root)
        self.serial_port_var.set(self.serial_ports[0] if self.serial_ports else "")
        tk.OptionMenu(serial_frame, self.serial_port_var, *self.serial_ports).grid(row=0, column=1)
        
        tk.Label(serial_frame, text="Baud Rate (bps):").grid(row=0, column=2)
        self.baud_rate_var = tk.StringVar(root)
        self.baud_rate_var.set("115200")
        tk.Entry(serial_frame, textvariable=self.baud_rate_var).grid(row=0, column=3)
        
        self.connect_button = tk.Button(serial_frame, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=0, column=4)
        
        self.disconnect_button = tk.Button(serial_frame, text="Disconnect", command=self.disconnect_serial, state=tk.DISABLED)
        self.disconnect_button.grid(row=0, column=5)
        
        self.serial_status_label = tk.Label(serial_frame, text="Serial Status: Not Connected", fg="red")
        self.serial_status_label.grid(row=0, column=6)
        
        # Add space between sections
        tk.Label(root, text="").grid(row=1)
        
        # Create a frame for N0 to N33 buttons with space between the buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=2, column=0, sticky="ew")
        
        self.fx_menus = {}  # Dictionary to store Fx value menus for each button
        self.buttons = {}  # Dictionary to store buttons
        self.key_assign_buttons = {}  # Dictionary to store "Assign Key" buttons
        
        self.assigned_keys = {}  # Dictionary to store assigned keys
        for i in range(34):
            button_text = f"N{i}"
            row, col = divmod(i, 8)
            
            # Create a frame for each button and menu
            button_menu_frame = tk.Frame(button_frame, padx=10, pady=10)
            button_menu_frame.grid(row=row, column=col, sticky="nsew")
            
            # Create an outline around each frame
            button_menu_frame.config(borderwidth=2, relief=tk.RAISED)
            
            # Create a button with a callback to assign a key
            self.buttons[button_text] = tk.Button(button_menu_frame, text=button_text, command=lambda text=button_text: self.send_to_serial(text))
            self.buttons[button_text].pack(fill=tk.BOTH)
            self.buttons[button_text].pack(fill=tk.BOTH)
            
            # Create a menu for Fx values
            fx_var = tk.StringVar(root)
            fx_var.set("F4")  # Default value is F4
            fx_menu = tk.OptionMenu(button_menu_frame, fx_var, "F4", "F8", "F12", "F16", "F20", "F24")
            fx_menu.pack(fill=tk.BOTH)
            
            # Create a button to assign a key
            self.key_assign_buttons[button_text] = tk.Button(button_menu_frame, text="Assign Key", command=lambda text=button_text: self.assign_key(text))
            self.key_assign_buttons[button_text].pack(fill=tk.BOTH)
            
            # Store the menu associated with the button in the dictionary
            self.fx_menus[button_text] = fx_var
        
        # Add space between buttons and the text field
        tk.Label(root, text="").grid(row=3)
        
        # Create a scrolled text field to display serial messages
        self.message_text = ScrolledText(root)
        self.message_text.grid(row=4, column=0, sticky="nsew")
        self.message_text.config(state=tk.DISABLED)
        self.message_text.config(height=10)
        
        self.serial_connection = None
        self.serial_thread = None
        
        # Configure grid weights for column resizing
        root.grid_rowconfigure(4, weight=1)
        root.grid_columnconfigure(0, weight=1)
        


    def list_serial_ports(self):
        try:
            import serial.tools.list_ports
            return [port.device for port in serial.tools.list_ports.comports()]
        except ImportError:
            return []
        
    def connect_serial(self):
        port = self.serial_port_var.get()
        baud_rate = int(self.baud_rate_var.get())
        
        try:
            self.serial_connection = serial.Serial(port, baud_rate)
            self.serial_status_label.config(text="Serial Status: Connected", fg="green")
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
            self.start_serial_thread()
        except serial.SerialException as e:
            tk.messagebox.showerror("Connection Error", str(e))
            
    def disconnect_serial(self):
        if self.serial_connection is not None:
            self.serial_connection.close()
            self.serial_status_label.config(text="Serial Status: Disconnected", fg="red")
            self.connect_button.config(state=tk.NORMAL)
            self.disconnect_button.config(state=tk.DISABLED)
            
    def send_to_serial(self, text):
        if self.serial_connection is not None:
            fx_value = self.fx_menus[text].get()
            message = f"M600 {text} {fx_value}\n"
            self.serial_connection.write(message.encode())
            
            #self.message_text.config(state=tk.NORMAL)
            #self.message_text.insert(tk.END, message)
            #self.message_text.see(tk.END)
            #self.message_text.config(state=tk.DISABLED)
   
   


    def assign_key(self, text):
        current_assigned_key = self.assigned_keys.get(text, "")

        if current_assigned_key:
            # Key is already assigned, unassign it
            self.assigned_keys[text] = ""
            self.key_assign_buttons[text].config(text="Assign Key")
            keyboard.remove_hotkey(current_assigned_key)
        else:
            # Assign a new key
            # Replace the button text with "Press a Key..." for indication
            self.key_assign_buttons[text].config(text="Press a Key...")
            self.root.update()  # Update the interface to display the new text

            # Wait for the user to press a keyboard key
            selected_key = keyboard.read_event(suppress=True).name

            # Update the button text with the assigned key
            self.key_assign_buttons[text].config(text=selected_key)

            # Create a callback function for the button to send serial data associated with the key
            def send_on_key_press():
                self.send_to_serial(text)

            # Assign the callback function to the button and the keyboard key
            keyboard.add_hotkey(selected_key, send_on_key_press)
            self.assigned_keys[text] = selected_key

    def reset_assigned_keys(self):
        for text in self.buttons.keys():
            self.assigned_keys[text] = ""
            
            
    def start_serial_thread(self):
        if self.serial_thread is None or not self.serial_thread.is_alive():
            self.serial_thread = threading.Thread(target=self.read_serial)
            self.serial_thread.daemon = True
            self.serial_thread.start()
               
    def read_serial(self):
        while True:
            try:
                data = self.serial_connection.readline().decode("utf-8", errors='replace')
                self.message_text.config(state=tk.NORMAL)
                self.message_text.insert(tk.END, data)
                self.message_text.see(tk.END)
                self.message_text.config(state=tk.DISABLED)
            except UnicodeDecodeError as e:
                self.message_text.config(state=tk.NORMAL)
                self.message_text.insert(tk.END, "Invalid Character: " + repr(e.object[e.start:e.end]) + "\n")
                self.message_text.config(state=tk.DISABLED)                


if __name__ == "__main__":
    root = tk.Tk()
    app = SerialCommunicationApp(root)
    root.mainloop()