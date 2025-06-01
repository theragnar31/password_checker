import tkinter as tk
from tkinter import messagebox, filedialog
from password_matcher import is_password_in_wordlist
import random
from tkinter import ttk

# Messages positifs et négatifs
SAFE_MESSAGES = [
    "✅ Mot de passe introuvable : c'est bon signe !",
    "🌈 Ce mot de passe est unique comme toi.",
    "🧘 Respire, ton mot de passe semble sûr.",
    "🎉 Aucun match trouvé, tu peux être fier !",
]

UNSAFE_MESSAGES = [
    "❌ Ce mot de passe est bien trop commun...",
    "⚠️ Match trouvé ! Il est temps de le changer.",
    "🔓 Ce mot de passe circule déjà sur Internet.",
    "😱 Ton mot de passe est vulnérable, pense à le renforcer.",
]

SAFE_COLOR = "#e0fff4"
UNSAFE_COLOR = "#ffecec"
BG_COLOR = "#f4f7fa"
TITLE_COLOR = "#2e3a59"
ACCENT_COLOR = "#4e94f3"
BUTTON_COLOR = "#4e94f3"
BUTTON_HOVER = "#3c7fe0"

FONT_TITLE = ("Poppins", 22, "bold")
FONT_TEXT = ("Poppins", 12)
FONT_RESULT = ("Poppins", 14, "bold")

class PasswordCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 SécuriPass | Teste ton mot de passe")
        self.root.geometry("700x600")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.wordlist_path = "wordlist.txt"

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=FONT_TEXT, padding=10, background=BUTTON_COLOR, foreground="white")
        style.map("TButton",
                  background=[('active', BUTTON_HOVER), ('disabled', '#cccccc')])

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root,
            text="🛡️ Bienvenue sur SécuriPass",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TITLE_COLOR
        )
        self.title_label.pack(pady=(30, 10))

        self.subtitle_label = tk.Label(
            self.root,
            text="Teste ton mot de passe et vois s'il figure dans une wordlist connue",
            font=FONT_TEXT,
            bg=BG_COLOR,
            fg="#555"
        )
        self.subtitle_label.pack(pady=(0, 20))

        self.input_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.input_frame.pack(pady=10)

        self.entry_label = tk.Label(self.input_frame, text="Entrez votre mot de passe :", font=FONT_TEXT, bg=BG_COLOR)
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.input_frame, show="*", font=FONT_TEXT, width=35, bd=2, relief="solid", justify="center")
        self.entry.pack(pady=10)

        self.check_button = ttk.Button(
            self.root,
            text="🔍 Vérifier le mot de passe",
            command=self.check_password
        )
        self.check_button.pack(pady=20)

        self.result_frame = tk.Frame(self.root, bg=BG_COLOR, padx=20, pady=20)
        self.result_frame.pack(pady=10)

        self.result_icon = tk.Label(self.result_frame, text="", font=("Poppins", 40), bg=BG_COLOR)
        self.result_icon.pack(pady=(10, 5))

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=FONT_RESULT,
            bg=BG_COLOR,
            fg=TITLE_COLOR,
            wraplength=600,
            justify="center"
        )
        self.result_label.pack()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="📂 Changer la wordlist", command=self.load_wordlist)
        self.menu.add_cascade(label="Options", menu=file_menu)

        self.footer = tk.Label(
            self.root,
            text="✨ Protégez vos données avec des mots de passe sûrs ✨",
            font=("Poppins", 10),
            bg=BG_COLOR,
            fg="#888"
        )
        self.footer.pack(side="bottom", pady=20)

    def check_password(self):
        password = self.entry.get()
        if not password:
            messagebox.showwarning("Attention", "Veuillez entrer un mot de passe.")
            return

        found = is_password_in_wordlist(password, self.wordlist_path)

        if found:
            self.root.configure(bg=UNSAFE_COLOR)
            self.result_frame.configure(bg=UNSAFE_COLOR)
            self.result_icon.configure(text="❌", bg=UNSAFE_COLOR)
            self.result_label.configure(text=random.choice(UNSAFE_MESSAGES), bg=UNSAFE_COLOR, fg="#a33")
        else:
            self.root.configure(bg=SAFE_COLOR)
            self.result_frame.configure(bg=SAFE_COLOR)
            self.result_icon.configure(text="✅", bg=SAFE_COLOR)
            self.result_label.configure(text=random.choice(SAFE_MESSAGES), bg=SAFE_COLOR, fg="#2a7")

    def load_wordlist(self):
        path = filedialog.askopenfilename(title="Choisir une wordlist", filetypes=[("Fichiers texte", "*.txt")])
        if path:
            self.wordlist_path = path
            messagebox.showinfo("Wordlist chargée", f"Wordlist sélectionnée : {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerGUI(root)
    root.mainloop()
