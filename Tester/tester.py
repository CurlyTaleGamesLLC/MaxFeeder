import tkinter as tk
import tkinter.messagebox
import serial
from tkinter.scrolledtext import ScrolledText
import threading

class SerialCommunicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MAXFeeder Tester")
        self.serial_ports = self.list_serial_ports()
        
        # Create a frame for the serial port connection widgets
        serial_frame = tk.Frame(root)
        serial_frame.pack()
        
        tk.Label(serial_frame, text="Serial Port:").grid(row=0, column=0)
        self.serial_port_var = tk.StringVar(root)
        self.serial_port_var.set(self.serial_ports[0] if self.serial_ports else "")
        tk.OptionMenu(serial_frame, self.serial_port_var, *self.serial_ports).grid(row=0, column=1)
        
        tk.Label(serial_frame, text="Baud Rate (bps):").grid(row=0, column=2)
        self.baud_rate_var = tk.StringVar(root)
        self.baud_rate_var.set("115200")
        tk.Entry(serial_frame, textvariable=self.baud_rate_var).grid(row=0, column=3)
        
        tk.Button(serial_frame, text="Connect", command=self.connect_serial).grid(row=0, column=4)
        
        # Add space between sections
        tk.Label(root, text="").pack()
        
        self.create_buttons()
        
        # Create a frame for N0 to N31 buttons
        button_frame = tk.Frame(root)
        button_frame.pack()
        
        for i in range(34):
            button_text = f"N{i}"
            tk.Button(button_frame, text=button_text, command=lambda text=button_text: self.send_to_serial(text)).pack(side=tk.LEFT)
        
        # Add space between buttons and the text field
        tk.Label(root, text="").pack()
        
        # Create a scrolled text field to display serial messages
        self.message_text = ScrolledText(root)
        self.message_text.pack(fill=tk.BOTH, expand=True)
        self.message_text.config(state=tk.DISABLED)  # Disable editing
        
        self.serial_connection = None  # Serial connection will be established after connecting
        self.serial_thread = None  # Thread for serial reading
        
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
            self.start_serial_thread()  # Start the serial reading thread
        except serial.SerialException as e:
            tk.messagebox.showerror("Connection Error", str(e))
            
    def create_buttons(self):
        pass
            
    def send_to_serial(self, text):
        if self.serial_connection is not None:
            message = f"M600 {text} F4\n"
            self.serial_connection.write(message.encode())
            
            # Display the sent message in the text field
            self.message_text.config(state=tk.NORMAL)  # Enable editing
            self.message_text.insert(tk.END, message)
            self.message_text.config(state=tk.DISABLED)  # Disable editing
            
    def start_serial_thread(self):
        if self.serial_thread is None or not self.serial_thread.is_alive():
            self.serial_thread = threading.Thread(target=self.read_serial)
            self.serial_thread.daemon = True  # Thread will terminate when the application closes
            self.serial_thread.start()
            
    def read_serial(self):
        while True:
            try:
                data = self.serial_connection.readline().decode("utf-8", errors='replace')
                self.message_text.config(state=tk.NORMAL)  # Enable editing
                self.message_text.insert(tk.END, data)
                self.message_text.see(tk.END)
                self.message_text.config(state=tk.DISABLED)  # Disable editing
            except UnicodeDecodeError as e:
                self.message_text.config(state=tk.NORMAL)  # Enable editing
                self.message_text.insert(tk.END, "Invalid Character: " + repr(e.object[e.start:e.end]) + "\n")
                self.message_text.config(state=tk.DISABLED)  # Disable editing
                
if __name__ == "__main__":
    root = tk.Tk()
    app = SerialCommunicationApp(root)
    root.mainloop()
