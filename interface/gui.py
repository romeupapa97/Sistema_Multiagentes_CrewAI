import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

# Função chamada ao clicar no botão "Gerar Artigo"
def gerar_artigo():
    tema = entry.get()
    if not tema:
        messagebox.showwarning("Aviso", "Informe um tema.")  # Alerta caso o campo esteja vazio
        return
    try:
        # Envia uma requisição POST para a API Flask com o tema informado
        resp = requests.post("http://127.0.0.1:5000/gerar_artigo", json={"tema": tema})
        data = resp.json()
        # Limpa o campo de texto e insere o artigo retornado
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, data.get("artigo", "Erro ao gerar artigo."))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar artigo: {e}")  # Exibe mensagem em caso de erro na requisição

# Interface gráfica com Tkinter
app = tk.Tk()
app.title("Sistema Multiagentes - Geração de Artigo")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Tema do Artigo:")
label.pack()

entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

# Botão que dispara a geração do artigo
button = tk.Button(frame, text="Gerar Artigo", command=gerar_artigo)
button.pack(pady=5)

# Área de texto rolável onde o artigo será exibido
text_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=25)
text_output.pack(padx=10, pady=10)

app.mainloop()
