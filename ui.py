import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SnifferApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Cyber Sniffer // Raw Packet Monitor")
        self.geometry("950x650")
        self.resizable(False, False)
        
        self.log_box = ctk.CTkTextbox(self, width=880, 
            height=430, 
            font=("Consolas", 12),
            fg_color="#121212",
            text_color="#00ff66"
        )
        
        self.log_box.pack(pady=5)
        self.log_box.insert("0.0", "[INIT] UI successfully loaded. Ready to bind with backend Engine ...\n")
        
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=15)
        
        self.start_btn = ctk.CTkButton(self.btn_frame, 
            text="START SNIFFING", 
            fg_color="#2b8a3e", 
            hover_color="#237032",
            font=("Consolas", 14, "bold"),
            command=self.start_sniffer
        )
        
        self.start_btn.grid(row=0, column=0, padx=15)
        
        self.stop_btn = ctk.CTkButton(self.btn_frame, 
            text="STOP", 
            fg_color="#c92a2a", 
            hover_color="#a61e1e",
            font=("Consolas", 14, "bold"),
            command=self.stop_sniffer
        )
        
        self.stop_btn.grid(row=0, column=1, padx=15)
        
    def start_sniffer(self) -> None:
        self.log_box.insert("end", "[ENGINE] Starting packet capture session...\n")
        self.log_box.see("end")
        
    def stop_sniffer(self) -> None:
        self.log_box.insert("end", "[!] Sniffer session stopped by user.\n")
        self.log_box.see("end")
        
app = SnifferApp()
app.mainloop()
        
        
        