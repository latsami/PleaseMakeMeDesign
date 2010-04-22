#! /usr/bin/env bash

# Usage:
# `echo "le chat est un gros matou" | ./clean.sh stopwords.txt`

# Créé une liste Bash de mots vides à partir du fichier passé en paramètre
# Voir http://fr.wikipedia.org/wiki/Mot_vide

if test -z "$1"
then
    echo "Veuillez passer un fichier contenant une liste de mots vides en argument."
    echo
    echo "Usage:"
    echo "echo \"voici un texte à nettoyer\" | ./clean.sh stopwords.txt"
    echo
  exit
fi

unset list
while read line; do 
    list+=($line); 
done < <(cat "$1")

# Fonction qui supprime les mots vides
f() { 
    while read input; do 
        for word in "$@"; do 
            input=$(sed "s/\b$word\b//g" <<<"$input"); 
        done; 
        echo "$input"; 
    done; 
}; 

# Appel de la fonction
f "${list[@]}" < <(cat -v)

