# sort_by_extension

# Français

# Trieur de Fichiers par Extension

## Description
Ce script Python trie automatiquement les fichiers sur le bureau de l'utilisateur en fonction de leur extension. Il déplace chaque fichier dans un répertoire nommé selon la catégorie de l'extension du fichier (par exemple, "Audio", "Images", "Vidéos", etc.).

## Comment ça marche
Le script utilise `pathlib` pour interagir avec le système de fichiers. Il crée des répertoires pour chaque catégorie d'extension et déplace les fichiers correspondants dans ces répertoires.

## Utilisation
1. Placez le script sur votre ordinateur.
2. Exécutez le script avec Python.
3. Vos fichiers sur le bureau seront triés dans des répertoires appropriés.

Si vous souhaitez trier d'autres parties de votre ordinateur, veuillez modifier la partie suivante : `tri_dir = Path.home() / "Desktop"`.

_____________________________________________________________________________________________________

# English

# File Sorter by Extension

## Description
This Python script automatically sorts files on the user's desktop based on their extension. It moves each file into a directory named after the file's extension category (e.g., "Sounds", "Pictures", "Movies", etc.).

## How It Works
The script uses `pathlib` to interact with the file system. It creates directories for each category of extension and moves the corresponding files into these directories.

## Usage
1. Place the script on your computer.
2. Run the script using Python.
3. Your files on the desktop will be sorted into appropriate directories.

If you wish to organize other parts of your computer, please modify the following section: `tri_dir = Path.home() / "Desktop"`.
