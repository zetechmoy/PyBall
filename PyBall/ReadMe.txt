Bonjour à tous les développeurs !

Je suis Théo Guidoux (zeTechMoy). Pendant mes études j'ai était passionné par la programmation.
Pendant le lycée j'ai programmé des applications sur Android.
J'ai voulu me lancer dans les jeux et voici mon premier jeu !
Une balle qui doit éviter des cubes ! Wouaw !

C'est un jeu qui a d'abord été développer sur Android, disponible ici : https://play.google.com/store/apps/details?id=in.olympe.zetechmoy.ball&hl=fr
J'ai ensuite développé le jeu sur Windows à l'aide de python 3.0+ et pygame pendant mon année de 1ere au lycée.

Voici le résultat ! 

Ce programme peut-être utilisé à des fins pédagogiques, mais pas à la vente.
Je vous demanderai s'il vous plait de faire allusion à mon nom si vous utilisez ce projet en présentation.

Le principe n'est pas si compliqué.

Le jeu commence par Main.py qui initialise tous les composants et en particulier le GamePanel.
GamePanel est le "moteur" du jeu c'est peut être la classe la plus importante. 
Il va appeler à chaque frame du jeu les fonctions update() puis draw() de la Scene en cours.
update() calcul tous les changements appliqués pendant la frame et draw() les dessinent sur la Scene.

"Euh..C'est quoi une Scene ??" J'y viens justement ! La Scene est la 2e classe la importante ! 
GamePanel possède une Scene qu'il affiche en continu tant que le jeu tourne. 
Si la scene change dans GamePanel, alors l'affichage change.
En implémentant les fonctions de Scene dans une classe dans le même genre que GameScene/MainMenuScene/BallScene, vous créez une interface graphique !

MainMenuScene est la première scene affichée lorsqu'on lance le jeu.
Elle permet de choisir soit de lancer le jeu (GameScene), lancer le choix des balles (BallScene) ou de quitter.

Intéressons-nous maintenant plus à la GameScene.
GameScene est une classe de type Scene. Elle est donc affichée par GamePanel.
GameScene contient un Player et des Platforms. Le Player doit éviter les plateformes.

Les plateformes apparaissent à droite de l'écran et se déplacent à vitesse constante vers la gauche.
Les plateformes sont simplement des cubes de couleurs.

Le Player quant à lui est un peu plus complexe. En effet il contient une Ball, une Animation...
Les fonctions update() et draw() de Ball sont appelées par Player qui elle même est appelée par GameScene puis GamePanel.

La Ball permet de changer de ball, par le même principe que les scenes. Si on change la Ball, l'affichage sera différent.
Animation.py permet de gérer plus simplement le systeme de rotation de la balle en fonction du temps.

Voilà des explications TRÈS suintent ! 

Je pourrais développer plus ici, mais le mieux est quand même de regarder le code est de comprendre comment il fonctionne !
N'hésitez pas à me contacter par mail : theoguidoux@gmail.com pour plus d'informations ! 
OU sur Twitter @TGuidoux
MERCI BEAUCOUP !