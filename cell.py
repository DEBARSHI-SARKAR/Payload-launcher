import tkinter as tk
from tkinter import filedialog
import threading
from core_engine import payload

class pcell:
    def __init__(self, parent, data=None, on_delete=None, on_update=None):
        self.parent = parent
        self.on_delete = on_delete
        self.on_update = on_update

        self.file_path = ""

        # Frame
        self.frame = tk.Frame(parent, bd=2, relief="groove", padx=10, pady=10)

        # Name
        self.name = tk.Entry(self.frame, width=40)
        self.name.pack()

        # IP / Port
        ip_frame = tk.Frame(self.frame)
        ip_frame.pack()

        tk.Label(ip_frame, text="192.168.1.").pack(side="left")

        self.ip_last = tk.Entry(ip_frame, width=5)
        self.ip_last.pack(side="left")

        self.port_entry = tk.Entry(ip_frame, width=6)
        self.port_entry.pack(side="left")

        # Payload buttons
        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="1GB VRAM",
                  command=lambda: self.set_payload("payloads/payload-1200-1gb-pro.bin")).pack(side="left")

        tk.Button(btn_frame, text="3GB VRAM",
                  command=lambda: self.set_payload("payloads/payload-1200-3gb-pro.bin")).pack(side="left")

        tk.Button(btn_frame, text="4GB VRAM",
                  command=lambda: self.set_payload("payloads/payload-1200-4gb-pro.bin")).pack(side="left")

        tk.Button(btn_frame, text="Custom-Payload",
                  command=self.select_file).pack(side="left")

        # Actions
        action_frame = tk.Frame(self.frame)
        action_frame.pack(pady=5)

        tk.Button(action_frame, text="SEND", command=self.send).pack(side="left")
        tk.Button(action_frame, text="DELETE", command=self.delete).pack(side="left")

        # Status
        self.status = tk.Label(self.frame, text="Idle")
        self.status.pack()

        self.frame.pack(fill="x", pady=5)

        # -------- LOAD DATA --------
        if data:
            self.name.insert(0, data.get("name", ""))

            self.ip_last.insert(0, data.get("ip_last", "7"))
            self.port_entry.insert(0, data.get("port", "9090"))

            self.file_path = data.get("file", "")
            if self.file_path:
                self.status.config(text=f"Loaded: {self.file_path}")

        # -------- AUTOSAVE --------
        self.name.bind("<KeyRelease>", lambda e: self.update())
        self.ip_last.bind("<KeyRelease>", lambda e: self.update())
        self.port_entry.bind("<KeyRelease>", lambda e: self.update())

    # ---------- Payload ----------
    def set_payload(self, path):
        self.file_path = path
        self._set_status(f"Selected: {path}")
        self.update()

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
        if path:
            self.file_path = path
            self._set_status(f"Selected: {path}")
            self.update()

    # ---------- Send ----------
    def send(self):
        if not self.file_path:
            self._set_status("No payload selected")
            return

        ip = "192.168.1." + self.ip_last.get()
        port = int(self.port_entry.get())

        threading.Thread(target=self._send_thread, args=(ip, port), daemon=True).start()

    def _send_thread(self, ip, port):
        try:
            self._set_status("Sending...")
            payload(ip, port, self.file_path)
            self._set_status("Done")
        except Exception as e:
            self._set_status(f"Error: {e}")

    def _set_status(self, text):
        self.frame.after(0, lambda: self.status.config(text=text))

    # ---------- Delete ----------
    def delete(self):
        self.frame.destroy()
        if self.on_delete:
            self.on_delete(self)

    def update(self):
        if self.on_update:
            self.on_update()
