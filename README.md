# 🔐 Password Matcher – Teste la robustesse de tes mots de passe

Bienvenue dans **Password Matcher**, un outil graphique élégant, rassurant et amusant pour tester la sécurité de vos mots de passe en les comparant à une **wordlist** régulièrement mise à jour.

> 🛡️ « Un mot de passe testé, une conscience apaisée. »

---

## 🎯 À quoi sert ce programme ?

Password Matcher permet à n'importe quel utilisateur de :

- Vérifier si son mot de passe est **présent dans une base de mots de passe compromis** (type "rockyou", leaks, etc.)
- Recevoir un **retour visuel apaisant ou alertant** (smiley, couleur, message rassurant)
- Utiliser une interface **simple, moderne et agréable**

---

## 🧰 Fonctionnalités

✅ Interface graphique en Python (Tkinter stylisé)  
✅ Recherche ultra-rapide dans une wordlist  
✅ Retours visuels ludiques et pédagogiques  
✅ Wordlist incluse + **mises à jour automatiques chaque semaine** via GitHub  
✅ Cross-platform : fonctionne sous Windows, macOS et Linux  
✅ Respect de la vie privée : **aucune donnée n’est envoyée**

---

## 🔄 Mises à jour automatiques

🗓️ **Chaque semaine**, une mise à jour de la `wordlist.txt` est poussée ici sur GitHub.

Lors du lancement, le programme vérifie si une nouvelle version de la wordlist est disponible, la télécharge et l’utilise automatiquement.

📌 Pas besoin de réinstaller l'application manuellement.

---

## 🚀 Lancer le programme

### 📦 Version compilée :
- Téléchargez le fichier `PasswordMatcher.exe` (Windows) ou `PasswordMatcher.app` (macOS)
- Double-cliquez : c’est tout.

### 🐍 Version Python :
```bash
git clone https://github.com/votre-utilisateur/password-matcher.git
cd password-matcher
pip install -r requirements.txt
python gui.py
