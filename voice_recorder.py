import tkinter as tk
from tkinter import filedialog
import pyaudio
import wave
import os

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder App")

        self.record_button = tk.Button(master, text="Record", command=self.start_recording,height=1,width=8,font=13)
        self.record_button.place(x=30,y=30)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_recording, state=tk.DISABLED,height=1,width=8,font=13,fg='red')
        self.stop_button.place(x=270,y=30)

        self.save_button = tk.Button(master, text="Save", command=self.save_recording, state=tk.DISABLED,height=1,width=8,font=13)
        self.save_button.place(x=150,y=180)
        self.filename_label = tk.Label(master, text="File Name:",font=14)
        self.filename_label.place(x=75,y=100)

        self.filename_entry = tk.Entry(master,width=20,font=12)
        self.filename_entry.place(x=75,y=140)

        self.frames = []

        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)

        self.frames = []
        self.filename_entry.delete(0, tk.END)

        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=44100,
                                      input=True,
                                      frames_per_buffer=1024)
        self.master.update()
        self.record()

    def record(self):
        try:
            data = self.stream.read(1024)
            self.frames.append(data)
            self.master.after(1, self.record)
        except Exception as e:
            print("Recording error:", e)
            self.stop_recording()

    def stop_recording(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.record_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL)

    def save_recording(self):
        filename = self.filename_entry.get()
        if not filename:
            filename = "untitled"
        filename += ".wav"

        file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Wave files", "*.wav")],
                                                   initialfile=filename)

        if file_path:
            wf = wave.open(file_path, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            self.filename_label.config(text=f"File saved as: {os.path.basename(file_path)}")
            self.frames = []

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="grey")
    root.geometry("400x300")
    app = VoiceRecorderApp(root)
    root.mainloop()
