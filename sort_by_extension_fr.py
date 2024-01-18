# Importation de la classe Path depuis le module pathlib pour manipuler les chemins de fichiers
from pathlib import Path

# Création d'un dictionnaire pour classer les fichiers selon leur extension
# Chaque extension de fichier est associée à un type (par exemple, '.mp3' est associé à 'Audio')
dirs = {".aac": "Audio",
        ".ai": "Images",
        ".avi": "Vidéos",
        ".bat": "Scripts",
        ".bmp": "Images",
        ".c": "Code source",
        ".csv": "Texte",
        ".css": "Texte",
        ".cpp": "Code source",
        ".dll": "Exécutables",
        ".doc": "Texte",
        ".docx": "Texte",
        ".exe": "Exécutables",
        ".flac": "Audio",
        ".flv": "Vidéos",
        ".gif": "Images",
        ".gz": "Archives",
        ".html": "Texte",
        ".java": "Scripts",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".js": "Texte",
        ".json": "Texte",
        ".mkv": "Vidéos",
        ".mov": "Vidéos",
        ".mp3": "Audio",
        ".mp4": "Vidéos",
        ".odp": "Présentations",
        ".ods": "Texte",
        ".odt": "Texte",
        ".pdf": "Texte",
        ".png": "Images",
        ".ppt": "Présentations",
        ".pptx": "Présentations",
        ".psd": "Images",
        ".py": "Scripts",
        ".rar": "Archives",
        ".rtf": "Texte",
        ".sh": "Scripts",
        ".svg": "Images",
        ".tar": "Archives",
        ".tiff": "Images",
        ".txt": "Texte",
        ".wav": "Audio",
        ".webp": "Images",
        ".wmv": "Vidéos",
        ".xls": "Texte",
        ".xlsx": "Texte",
        ".xlsm": "Texte",
        ".xml": "Texte",
        ".zip": "Archives"
        ".lnk": "Raccourcis"}

# Définition du répertoire de travail, ici le bureau (Desktop) de l'utilisateur (a modifier suivant l'endroit où vous voulez trier)
tri_dir = Path.home() / "Desktop"

# Récupération de tous les fichiers dans le répertoire de travail
files = [f for f in tri_dir.iterdir() if f.is_file()]

# Parcours de chaque fichier dans le répertoire
for file in files:
    try:
        # Détermination du sous-répertoire de destination basé sur l'extension du fichier
        # Si l'extension n'est pas dans le dictionnaire, le fichier est classé dans 'Autres'
        output_dir = tri_dir / dirs.get(file.suffix.lower(), "Autres")

        # Création du sous-répertoire s'il n'existe pas déjà
        output_dir.mkdir(exist_ok=True)

        # Déplacement du fichier vers le sous-répertoire approprié
        file.rename(output_dir / file.name)
    except Exception as erreur:
        # Affichage d'une erreur si le déplacement du fichier échoue
        print(f"Erreur lors du déplacement du fichier {file}: {erreur}")
