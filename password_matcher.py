def is_password_in_wordlist(password: str, wordlist_path: str) -> bool:
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if line.strip() == password:
                    return True
        return False
    except FileNotFoundError:
        print(f"Wordlist introuvable : {wordlist_path}")
        return False
    except Exception as e:
        print(f"Erreur lors de la lecture de la wordlist : {e}")
        return False
