# Gestion-de-Bibliotheque
#Description de l'application : 
L'application de gestion de bibliothèque, vous permet de gérer les livres de la bibliothèque, d'enregistrer les emprunts et retours de livres, 
ainsi que de les modifier et les supprimer. Il facilite la gestion de la bibliothèque et permet une meilleure organisation des tâches.

#Les fonctionnalités de gestionnaire de l'application :
  -créer un compte
  -Se connecter puis accéder à l'application
  -Ajouter un livre
  -Modifier un livre
  -Supprimer un livre 
  
#Les technologies :
  -PyCharm est un environnement de développement intégré (IDE) utilisé principalement pour la programmation en Python. Il est développé par JetBrains et 
  fournit des fonctionnalités avancées telles que l'analyse de code, la refactoring, le débogage, l'intégration avec des outils de gestion de version,
  la création d'interfaces graphiques utilisateur et bien plus encore. PyCharm est disponible en version gratuite et payante avec des fonctionnalités 
  supplémentaires.
  
  -Python 3.8.8 est une version spécifique de Python, qui est un langage de programmation de haut niveau interprété et orienté objet. Cette version 
  particulière a été publiée en février 2021 et comprend des améliorations de sécurité et des corrections de bugs par rapport aux versions précédentes
  de Python 3.8. Il est souvent utilisé pour le développement de logiciels, la science des données, l'analyse de données, l'automatisation des tâches 
  et le développement web, entre autres applications.
  
  -MySQL est un système de gestion de base de données relationnelle (SGBDR) open source, c'est-à-dire un logiciel qui permet de stocker, d'organiser et 
  de gérer des données dans une base de données. Il est souvent utilisé pour des applications web, des systèmes de gestion de contenu, des applications 
  de gestion d'entreprise et d'autres projets nécessitant une gestion de données efficace. MySQL est développé et maintenu par Oracle Corporation et est 
  disponible en version gratuite et payante avec des fonctionnalités supplémentaires.
  
  -Tkinter est un module Python intégré qui permet de créer des interfaces graphiques utilisateur (GUI) pour des applications de bureau. Il fournit un 
  ensemble de widgets graphiques pré-conçus tels que des boutons, des champs de texte, des cases à cocher et des listes déroulantes, que l'on peut utiliser 
  pour construire des interfaces utilisateur interactives. Tkinter est basé sur la bibliothèque graphique Tcl/Tk et est disponible avec toutes les 
  installations standard de Python, ce qui en fait un choix populaire pour la création de GUI en Python.
  -Custom Tkinter, ou personnalisation de Tkinter, fait référence à la création de widgets personnalisés pour les interfaces graphiques utilisateur (GUI) 
  créées à l'aide de Tkinter, un module Python intégré pour la création de GUI. Les widgets personnalisés peuvent être conçus pour répondre à des besoins 
  spécifiques de l'application et permettent aux développeurs de créer des interfaces utilisateur plus adaptées et plus conviviales pour leurs utilisateurs. 
  La personnalisation de Tkinter peut être effectuée en utilisant les outils de personnalisation fournis par Tkinter, tels que les options de configuration, 
  les variables Tkinter, et en utilisant le langage de programmation Python pour personnaliser le comportement des widgets.
  
  -PIL (Python Imaging Library) est une bibliothèque Python qui permet de manipuler des images de manière efficace. Elle fournit des fonctions pour ouvrir, 
  manipuler et enregistrer des images dans différents formats tels que JPEG, PNG, BMP, GIF, etc.
  

#l'utilité de l'application :
   Pour lancer cette application , il faut lancer main.py 
   Ensuite un interface graphique de login s'affiche , si vous aurez un compte déja vous pouvez l'accéder en entrant votre username et password , sinon
   vous clickez sur sign up .
   
   dans cette interface sign up nous avons fait toutes les conditions , si par exemple les inputs sont vides , nous affichons un message d'erreur avec un 
   qui explique l'erreur a partir messagebox , le même cas si le password n'est pas le même que repeat password , ainsi que si email ou utilisateur a créer 
   déja exist ...
   
   Si vous créez votre compte , vous l'accedez a sign in , dans lequel vous entrez votre username and password , nous avons fait aussi des conditions , si
   par exemple email ou password n'existe pas dans la base de donnée en affichant un messagebox . Vous aurez juste 3 chance d'entrer le correct username et 
   password , par la suite , le boutton login destroy .
   
   Aprés le correct username et password , vous l'accédez au champ livre .
   
   Vous pouvez ajouter, modifier ainsi que supprimer les livre ,Avec des conditions pour chaque champs .
   Pour l'ajout , il faut entrer tous les inputs .
   Le même cas pour modfier , en entrant le nom de livre dans lequel vous voulez le modifier .
   Pour la supprission , il faut entrer le nom du livre , sur input Title , puis cliquer sur delete , sans entrer les autres inputs .
   
 
  
  
  
  
  
  
  
