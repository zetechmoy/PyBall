Bonjour � tous les d�veloppeurs !

Je suis Th�o Guidoux (zeTechMoy). Pendant mes �tudes j'ai �tait passionn� par la programmation.
Pendant le lyc�e j'ai programm� des applications sur Android.
J'ai voulu me lancer dans les jeux et voici mon premier jeu !
Une balle qui doit �viter des cubes ! Wouaw !

C'est un jeu qui a d'abord �t� d�velopper sur Android, disponible ici : https://play.google.com/store/apps/details?id=in.olympe.zetechmoy.ball&hl=fr
J'ai ensuite d�velopp� le jeu sur Windows � l'aide de python 3.0+ et pygame pendant mon ann�e de 1ere au lyc�e.

Voici le r�sultat ! 

Ce programme peut-�tre utilis� � des fins p�dagogiques, mais pas � la vente.
Je vous demanderai s'il vous plait de faire allusion � mon nom si vous utilisez ce projet en pr�sentation.

Le principe n'est pas si compliqu�.

Le jeu commence par Main.py qui initialise tous les composants et en particulier le GamePanel.
GamePanel est le "moteur" du jeu c'est peut �tre la classe la plus importante. 
Il va appeler � chaque frame du jeu les fonctions update() puis draw() de la Scene en cours.
update() calcul tous les changements appliqu�s pendant la frame et draw() les dessinent sur la Scene.

"Euh..C'est quoi une Scene ??" J'y viens justement ! La Scene est la 2e classe la importante ! 
GamePanel poss�de une Scene qu'il affiche en continu tant que le jeu tourne. 
Si la scene change dans GamePanel, alors l'affichage change.
En impl�mentant les fonctions de Scene dans une classe dans le m�me genre que GameScene/MainMenuScene/BallScene, vous cr�ez une interface graphique !

MainMenuScene est la premi�re scene affich�e lorsqu'on lance le jeu.
Elle permet de choisir soit de lancer le jeu (GameScene), lancer le choix des balles (BallScene) ou de quitter.

Int�ressons-nous maintenant plus � la GameScene.
GameScene est une classe de type Scene. Elle est donc affich�e par GamePanel.
GameScene contient un Player et des Platforms. Le Player doit �viter les plateformes.

Les plateformes apparaissent � droite de l'�cran et se d�placent � vitesse constante vers la gauche.
Les plateformes sont simplement des cubes de couleurs.

Le Player quant � lui est un peu plus complexe. En effet il contient une Ball, une Animation...
Les fonctions update() et draw() de Ball sont appel�es par Player qui elle m�me est appel�e par GameScene puis GamePanel.

La Ball permet de changer de ball, par le m�me principe que les scenes. Si on change la Ball, l'affichage sera diff�rent.
Animation.py permet de g�rer plus simplement le systeme de rotation de la balle en fonction du temps.

Voil� des explications TR�S suintent ! 

Je pourrais d�velopper plus ici, mais le mieux est quand m�me de regarder le code est de comprendre comment il fonctionne !
N'h�sitez pas � me contacter par mail : theoguidoux@gmail.com pour plus d'informations ! 
OU sur Twitter @TGuidoux
MERCI BEAUCOUP !