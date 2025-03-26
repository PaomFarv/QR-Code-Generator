import customtkinter as ctk
import qrcode
from tkinter import filedialog

ctk.set_appearance_mode("light")
ctk.set_default_color_theme('blue')

def save_qr_image(img):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        img.save(save_path)

def qr_gen():
    guide_label.destroy()
    
    data = data_inp.get()
    if not data:
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img = img.resize((240, 240))

    qr_ctk_img = ctk.CTkImage(light_image=img, size=(240, 240))

    qr_label.configure(image=qr_ctk_img)
    qr_label.image = qr_ctk_img

    gen_button.configure(text="Regenerate")

    save_button.pack(pady=10)

def save_btn():
    data = data_inp.get()
    if not data:
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img = img.resize((240, 240))  
    save_qr_image(img)

app = ctk.CTk()
app.title("QR Code Generator")
app.geometry("400x570")

main_frame = ctk.CTkFrame(master=app,border_width=1,fg_color="#00a2ff")
main_frame.pack(fill="x",pady=10,padx=10)

header = ctk.CTkLabel(master=main_frame, text="CreateQR", font=("Fixedsys", 60),text_color="white")
header.pack(pady=10)

data_inp = ctk.CTkEntry(master=app,placeholder_text="Insert the Data",width=350,height=40,font=("Arial",18))
data_inp.pack(pady=10)

gen_button = ctk.CTkButton(master=app,text="Generate",width=100,height=20,font=("Arial",18),command=qr_gen,text_color="white")
gen_button.pack(pady=10)

guide_label = ctk.CTkLabel(master=app,text="QR Code will appear here.")
guide_label.pack(pady=100)

qr_label = ctk.CTkLabel(master=app,text="")
qr_label.pack(pady=15)

save_button = ctk.CTkButton(master=app,text="Save Image",width=100,height=20,font=("Arial",18),command=save_btn,text_color="white")
save_button.pack_forget()

app.mainloop()