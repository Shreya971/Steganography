import cv2
import tkinter as tk
from tkinter import filedialog

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Global variables
img_data = None
key = None

def encrypt_image():
    global img_data, key
    key = key_entry.get()
    text = message_entry.get()

    k1 = 0
    t1n = len(text)
    z = 0
    n = 0
    m = 0
    l = len(text)

    for i in range(l):
        img_data[n, m, z] = d[text[i]] ^ d[key[k1]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3
        k1 = (k1 + 1) % len(key)

    cv2.imwrite("encrypted-img.jpg", img_data)
    result_label.config(text="Encryption successful. Image saved as 'encrypted-img.jpg'.")

def select_image():
    global img_data
    global key

    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    img_data = cv2.imread(img_path)

    key = key_entry.get()

    image_label.config(text="Image Selected")

def decrypt_image():
    global img_data, key

    key1 = key_decrypt_entry.get()
    decrypt = ""

    if key == key1:
        k1 = 0
        t1n = len(message_entry.get())
        z = 0
        n = 0
        m = 0

        for i in range(t1n):
            decrypt += c[img_data[n, m, z] ^ d[key[k1]]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3
            k1 = (k1 + 1) % len(key)
        result_label_decrypt.config(text="Decrypted text: " + decrypt)
    else:
        result_label_decrypt.config(text="Key not matched.")

# Encryption GUI
encrypt_gui = tk.Tk()
encrypt_gui.title("Encryption")

key_label = tk.Label(encrypt_gui, text="Security Key:")
key_label.pack()

key_entry = tk.Entry(encrypt_gui)
key_entry.pack()

message_label = tk.Label(encrypt_gui, text="Message to Hide:")
message_label.pack()

message_entry = tk.Entry(encrypt_gui)
message_entry.pack()

encrypt_button = tk.Button(encrypt_gui, text="Encrypt", command=encrypt_image)
encrypt_button.pack()

select_image_button = tk.Button(encrypt_gui, text="Select Image", command=select_image)
select_image_button.pack()

image_label = tk.Label(encrypt_gui, text="")
image_label.pack()

result_label = tk.Label(encrypt_gui, text="")
result_label.pack()

# Decryption GUI
decrypt_gui = tk.Tk()
decrypt_gui.title("Decryption")

key_decrypt_label = tk.Label(decrypt_gui, text="Re-enter Key to Decrypt:")
key_decrypt_label.pack()

key_decrypt_entry = tk.Entry(decrypt_gui)
key_decrypt_entry.pack()

decrypt_button = tk.Button(decrypt_gui, text="Decrypt", command=decrypt_image)
decrypt_button.pack()

result_label_decrypt = tk.Label(decrypt_gui, text="")
result_label_decrypt.pack()

encrypt_gui.mainloop()
decrypt_gui.mainloop()
