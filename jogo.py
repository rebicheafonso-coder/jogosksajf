import tkinter as tk
from tkinter import ttk, messagebox
import random

# Lista simples de seleções
TEAMS = [
    "Brasil", "Argentina", "França", "Alemanha", "Espanha",
    "Inglaterra", "Portugal", "Holanda", "Itália", "Uruguai"
]

# Função para simular a partida
def simulate_match(team1, team2, result_label):
    try:
        if not team1 or not team2:
            raise ValueError("Selecione duas seleções.")
        if team1 == team2:
            raise ValueError("As seleções devem ser diferentes.")

        # Gera placares aleatórios realistas
        goals_team1 = random.randint(0, 5)
        goals_team2 = random.randint(0, 5)

        result = f"{team1} {goals_team1} x {goals_team2} {team2}"

        # Exibe resultado
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Configuração da janela principal
def main():
    window = tk.Tk()
    window.title("Mini Copa do Mundo • Python")
    window.geometry("420x300")
    window.resizable(False, False)

    title = tk.Label(window, text="Simulador da Copa do Mundo", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Combobox de Seleções
    tk.Label(frame, text="Seleção 1:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
    cb_team1 = ttk.Combobox(frame, values=TEAMS, state="readonly")
    cb_team1.grid(row=0, column=1)

    tk.Label(frame, text="Seleção 2:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
    cb_team2 = ttk.Combobox(frame, values=TEAMS, state="readonly")
    cb_team2.grid(row=1, column=1)

    # Resultado
    result_label = tk.Label(window, text="", font=("Arial", 18, "bold"))
    result_label.pack(pady=20)

    # Botão de simular
    simulate_btn = tk.Button(
        window,
        text="Simular Partida",
        font=("Arial", 12, "bold"),
        bg="#28a745",
        fg="white",
        width=20,
        command=lambda: simulate_match(cb_team1.get(), cb_team2.get(), result_label)
    )
    simulate_btn.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
