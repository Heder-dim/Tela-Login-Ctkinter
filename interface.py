import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("900x700")


txtLogin = customtkinter.CTkLabel(janela, text="Login")
txtLogin.pack(padx=10, pady=10)

txtUser = customtkinter.CTkLabel(janela, text="Usuario")
txtUser.pack()

EntUser = customtkinter.CTkEntry(janela, placeholder_text="Usuario")
EntUser.pack()

txtSenha = customtkinter.CTkLabel(janela, text="Senha")
txtSenha.pack()


Entsenha = customtkinter.CTkEntry(janela, placeholder_text="Senha")
Entsenha.pack()

btn = customtkinter.CTkButton(janela, text="a")
btn.pack(padx=10, pady=10)


janela.mainloop()
