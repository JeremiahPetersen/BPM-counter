import tkinter as tk
import time
import keyboard

class BPMCounterClick:
    def __init__(self, master):
        self.master = master
        self.master.title("BPM Counter Click")
        self.master.geometry("350x300")

        self.bpm_label = tk.Label(self.master, text="BPM: 0", font=("Arial", 24))
        self.bpm_label.pack(pady=20)

        self.tap_button = tk.Button(self.master, text="Tap", command=self.record_timestamp, height=2, width=10)
        self.tap_button.pack(pady=10)

        self.option_var = tk.StringVar()
        self.option_var.set("both")

        self.space_option = tk.Radiobutton(self.master, text="Spacebar", variable=self.option_var, value="spacebar")
        self.space_option.pack(pady=5)

        self.mouse_option = tk.Radiobutton(self.master, text="Mouse", variable=self.option_var, value="mouse")
        self.mouse_option.pack(pady=5)

        self.both_option = tk.Radiobutton(self.master, text="Both", variable=self.option_var, value="both")
        self.both_option.pack(pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

        self.pressed = False
        self.timestamps = []

        self.master.bind("<space>", self.space_pressed)
        self.master.bind("<KeyRelease-space>", self.space_released)

    def space_pressed(self, event):
        if not self.pressed and (self.option_var.get() == "spacebar" or self.option_var.get() == "both"):
            self.pressed = True
            self.record_timestamp()

    def space_released(self, event):
        self.pressed = False

    def record_timestamp(self):
        current_time = time.time()
        self.timestamps.append(current_time)
        if len(self.timestamps) > 1:
            interval_sum = 0
            for i in range(len(self.timestamps) - 1):
                interval_sum += (self.timestamps[i + 1] - self.timestamps[i])
            average_interval = interval_sum / (len(self.timestamps) - 1)
            bpm = 60 / average_interval
            self.bpm_label.config(text=f"BPM: {bpm:.2f}")

    def reset(self):
        self.timestamps = []
        self.bpm_label.config(text="BPM: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = BPMCounterClick(root)
    root.mainloop()