import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import ttkbootstrap as tb 

DB = "pessoas.db"

# Banco de dados
class Banco:
    def _init_(self):
        self.conn = sqlite3.connect(DB)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    profissao TEXT NOT NULL
                )
            ''')

    def inserir(self, nome, idade, profissao):
        with self.conn:
            self.conn.execute("INSERT INTO pessoas (nome, idade, profissao) VALUES (?, ?, ?)", (nome, idade, profissao))

    def atualizar(self, pid, nome, idade, profissao):
        with self.conn:
            self.conn.execute("UPDATE pessoas SET nome=?, idade=?, profissao=? WHERE id=?", (nome, idade, profissao, pid))

    def excluir(self, pid):
        with self.conn:
            self.conn.execute("DELETE FROM pessoas WHERE id=?", (pid,))

    def buscar(self, termo, ordenar):
        cursor = self.conn.cursor()
        consulta = f"SELECT * FROM pessoas WHERE nome LIKE ? OR profissao LIKE ? ORDER BY {ordenar}"
        cursor.execute(consulta, (f"%{termo}%", f"%{termo}%"))
        return cursor.fetchall()

# App principal
class CadastroApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Cadastro de Pessoas")
        self.db = Banco()
        self.pessoa_editando = None

        self.criar_widgets()
        self.atualizar_lista()

    def criar_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        ttk.Label(frame, text="Nome").grid(row=0, column=0, sticky="w")
        self.entry_nome = ttk.Entry(frame)
        self.entry_nome.grid(row=0, column=1, sticky="ew")

        ttk.Label(frame, text="Idade").grid(row=1, column=0, sticky="w")
        self.entry_idade = ttk.Entry(frame)
        self.entry_idade.grid(row=1, column=1, sticky="ew")

        ttk.Label(frame, text="Profissão").grid(row=2, column=0, sticky="w")
        self.entry_profissao = ttk.Entry(frame)
        self.entry_profissao.grid(row=2, column=1, sticky="ew")

        ttk.Button(frame, text="Salvar", command=self.salvar_pessoa).grid(row=3, columnspan=2, pady=5)

        ttk.Label(frame, text="Ordenar por:").grid(row=4, column=0)
        self.ordenar_por = tk.StringVar(value="nome")
        ttk.Combobox(frame, textvariable=self.ordenar_por,
                     values=["nome", "idade", "profissao"], state="readonly").grid(row=4, column=1)

        ttk.Label(frame, text="Buscar:").grid(row=5, column=0)
        self.entry_busca = ttk.Entry(frame)
        self.entry_busca.grid(row=5, column=1)

        ttk.Button(frame, text="Atualizar Lista", command=self.atualizar_lista).grid(row=6, columnspan=2, pady=5)

        self.tabela = ttk.Treeview(frame, columns=("ID", "Nome", "Idade", "Profissão"), show="headings")
        for col in ("ID", "Nome", "Idade", "Profissão"):
            self.tabela.heading(col, text=col)
        self.tabela.grid(row=7, column=0, columnspan=2, pady=5)
        self.tabela.bind("<Double-1>", self.selecionar_pessoa)

        ttk.Button(frame, text="Editar Selecionado", command=self.editar_pessoa).grid(row=8, column=0, pady=5)
        ttk.Button(frame, text="Excluir Selecionado", command=self.excluir_pessoa).grid(row=8, column=1, pady=5)

    def salvar_pessoa(self):
        nome = self.entry_nome.get().strip()
        idade = self.entry_idade.get().strip()
        profissao = self.entry_profissao.get().strip()

        if not nome or not idade or not profissao:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        try:
            idade = int(idade)
        except ValueError:
            messagebox.showerror("Idade inválida", "Idade precisa ser um número.")
            return

        if self.pessoa_editando:
            self.db.atualizar(self.pessoa_editando, nome, idade, profissao)
            self.pessoa_editando = None
        else:
            self.db.inserir(nome, idade, profissao)

        self.limpar_campos()
        self.atualizar_lista()

    def atualizar_lista(self):
        termo = self.entry_busca.get().lower()
        ordenar = self.ordenar_por.get()
        pessoas = self.db.buscar(termo, ordenar)

        self.tabela.delete(*self.tabela.get_children())
        for p in pessoas:
            self.tabela.insert("", "end", values=p)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_profissao.delete(0, tk.END)

    def selecionar_pessoa(self, event):
        item = self.tabela.selection()
        if item:
            dados = self.tabela.item(item)["values"]
            self.pessoa_editando = dados[0]
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, dados[1])
            self.entry_idade.delete(0, tk.END)
            self.entry_idade.insert(0, dados[2])
            self.entry_profissao.delete(0, tk.END)
            self.entry_profissao.insert(0, dados[3])

    def editar_pessoa(self):
        if self.pessoa_editando:
            self.salvar_pessoa()
        else:
            messagebox.showinfo("Editar", "Clique duas vezes em um item da lista.")

    def excluir_pessoa(self):
        item = self.tabela.selection()
        if item:
            dados = self.tabela.item(item)["values"]
            self.db.excluir(dados[0])
            self.atualizar_lista()
        else:
            messagebox.showinfo("Excluir", "Selecione um item.")

# Iniciar app
if __name__ == "_main_":
    root = tb.Window(themename="darkly")
    app = CadastroApp(root)
    root.mainloop()