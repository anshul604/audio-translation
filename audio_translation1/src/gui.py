import tkinter as tk
from tkinter import filedialog, messagebox
from audio_translation import translate_audio_after_6pm

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
    if file_path:
        result = translate_audio_after_6pm(file_path)
        result_text.set(result)

app = tk.Tk()
app.title("Audio Translation from English to Hindi")

upload_button = tk.Button(app, text="Upload Audio File", command=upload_file)
upload_button.pack(pady=20)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=400)
result_label.pack(pady=20)

app.geometry("500x300")
app.mainloop()
