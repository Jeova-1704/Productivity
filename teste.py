import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Janela Maximizada")
        self.root.state('zoomed')  # Define o estado da janela como maximizado

        self.label = tk.Label(root, text="Janela Maximizada", font=("Helvetica", 24))
        self.label.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)  # Expande para preencher a janela


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
