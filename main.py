import tkinter as tk
import json
import os

FILE_NAME = "memory.json"

if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
    # file sudah ada dan berisi: baca data
    with open(FILE_NAME) as f:
        data = json.load(f)
else:
    # file belum ada atau kosong: tanya lalu simpan
    data = {
        "petName": input("Masukkan nama Pet : "),
        "ownerName": input("Masukkan nama Anda : "),
    }
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

print("nama pet : ", data["petName"])
print("nama owner : ", data["ownerName"])

font = ("Arial", 14)

window = tk.Tk()
window.title(data["petName"])
window.geometry("400x300")

tk.Label(window, text="Hello ", font=font).pack()

window.mainloop()