import customtkinter as ctk

from views.app_view import criar_janela
from controllers.app_controller import iniciar_aplicacao

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

janela = criar_janela()

iniciar_aplicacao(janela)

janela.mainloop()