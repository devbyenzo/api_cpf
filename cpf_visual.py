import customtkinter as ctk
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def consultar_cpf():
    cpf = entrada_cpf.get().strip()

    if not cpf:
        resultado.configure(text="Digite um CPF primeiro.")
        return

    if not API_KEY:
        resultado.configure(text="API Key não encontrada no arquivo .env.")
        return

    url = f"https://api.cpfhub.io/cpf/{cpf}"

    headers = {
        "x-api-key": API_KEY,
        "Accept": "application/json"
    }

    try:
        resultado.configure(text="Consultando...")

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            resultado.configure(
                text=f"Erro na consulta.\nStatus: {response.status_code}\n{response.text}"
            )
            return

        data = response.json()

        texto_formatado = ""

        for chave, valor in data.items():
            texto_formatado += f"{chave}: {valor}\n"

        resultado.configure(text=texto_formatado)

    except requests.exceptions.RequestException as erro:
        resultado.configure(text=f"Erro de conexão:\n{erro}")

    except Exception as erro:
        resultado.configure(text=f"Erro inesperado:\n{erro}")


janela = ctk.CTk()
janela.title("Consulta CPF")
janela.geometry("500x550")
janela.resizable(False, False)

container = ctk.CTkFrame(janela, corner_radius=20)
container.pack(padx=25, pady=25, fill="both", expand=True)

titulo = ctk.CTkLabel(
    container,
    text="Consulta de CPF",
    font=("Arial", 26, "bold")
)
titulo.pack(pady=(30, 10))

subtitulo = ctk.CTkLabel(
    container,
    text="Sistema integrado com API via Key",
    font=("Arial", 14),
    text_color="gray"
)
subtitulo.pack(pady=(0, 25))

entrada_cpf = ctk.CTkEntry(
    container,
    placeholder_text="Digite o CPF",
    width=330,
    height=45,
    font=("Arial", 15),
    corner_radius=12
)
entrada_cpf.pack(pady=10)

botao = ctk.CTkButton(
    container,
    text="Consultar",
    width=330,
    height=45,
    font=("Arial", 15, "bold"),
    corner_radius=12,
    command=consultar_cpf
)
botao.pack(pady=15)

resultado_box = ctk.CTkFrame(container, corner_radius=15)
resultado_box.pack(padx=20, pady=20, fill="both", expand=True)

resultado = ctk.CTkLabel(
    resultado_box,
    text="O resultado aparecerá aqui.",
    font=("Consolas", 13),
    justify="left",
    anchor="nw",
    wraplength=390
)
resultado.pack(padx=20, pady=20, fill="both", expand=True)

janela.mainloop()