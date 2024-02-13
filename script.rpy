# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Nina', color="#c8ffc8")
define m = Character ('Moi', color="#ffffff")

# Le jeu commence ici
label start:
    show my_character
    with dissolve

    n "Salut. Je crois pas t'avoir déjà rencontré, non ?"

    menu: 
        m "Salut."
        "Si, on s'est vu aux journées portes ouvertes !":
            jump jpo
        "Hum, je crois pas effectivement...":
            jump jcroispas

label jpo:
    n "Ah... c'est quoi ton nom déjà ?"
    m "Je m'appelle Sucrette."
    n "Oh je vois."
    hide my_character
    show my_character2 
    n "..."
    m "..."
    n "Super, super tout ça..."
    m "Et toi c'est quoi ton nom ?"
    hide my_character2
    show my_character
    n "Je pensais que tu le savais !"
    m "J'ai menti on s'est jamais vu !"
    n "Pfft... T'es rigolote mais putain j'ai cru avoir oublié quelqu'un en si peu de temps."
    m "Hahaha, t'aurais dû voir ta tête."
    n "Plus jamais, plus jamais."
    m "Maintenant tu me connais ça va être compliqué de le refaire..."
    n "Hm, c'est vrai."
    play music "sonnerie ecole.mp3" noloop
    n "Oh c'est l'heure. On se revoit plus tard... ton nom déjà ?"
    m "EH !!!"

    "Nina partit en direction de la salle de classe en rigolant"
    return 

label jcroispas:
    n "Moi c'est Nina, et toi ?"


    return
