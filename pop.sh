#Config

#Csv, Hdfs, Db
#Crédentials des différents plugins. Les plugins doivent demander les crédentials à l'installation
#

#Package Managment

mlh plugin -ls 'toto'
#liste les plugins téléchargeables au nom de toto

mlh plugin -install 'tutu'
#Télécharge le plugin tutu qui devient accessible avec 'mlh tutu' ou importe plusieurs commandes (mlh data-analyse, mlh data-science, mlh server)

mlh plugin -uninstall 'tutu'

#====================================================================

mlh config
#Configure le dossier principal
	mlh config 'tutu'
	#Configure la transformation tutu

mlh home
#Retourne au dossier principal

mlh go 'tutu'
#Reviens dans le dossier principal de tutu 

mlh init 'tutu'
#Créer une nouvelle transformation du nom de tutu
#Créer un nouveau répertoire dans le dossier principal
#Créer un fichier de config

mlh catch 'tutu'
#Ouvre une fenêtre qui permet de déposer le fichier
#Ferme ensuite la fénêtre et reviens à la fenêtre de terminal dans le bon dossier

#====================================================================

#Data Analyse

mlh doctor
#Remplace les valeurs manquantes
#Convertit toutes les dates dans le même format
	
mlh sanitize
#Convertit les noms de donnée (minuscule, underscore)
#Transforme le format des dates, 
#remplace les autres séparateurs par des virgules, 
	mlh sanitize -convert -transform -replace

mlh checkup
#Informe sur le type de donnée dans chaque catégorie
#Informe sur des erreurs de parsing et affiche les valeurs qui font défaut

mlh stats
#cf cvsstat

mlh keep
#garde certaines colonnes

mlh ipython

mlh cut 
#supprime certaine colonne

mlh look
#affiche les données sous forme de tableau
	mlh look -plot
	#affiche les données sous forme de graphique #Quid des dates ? 
	mlh look -hist
	#affiche un histogramme des données
	mlh look -tail
	mlh look -head
	mlh look -columns
	mlh look -tableau
	#Lance tableau avec le csv en source de donnée
	mlh look -excel
	mlh look -numbers

mlh replace
#Remplace les caractères
	mlh replace -h
	#Remplace uniquement le header

mlh ext -size -q
#Génère des données d'un échantillon fixé par size
#-q permet de fixer la taille de la queue entrante
mlh step -q
mlh load -q
#Appelle un extracteur dans un dossier d'extracteur
#Idem dans un dossier de step et de loader
	mlh ext new 'ext_name'
	mlh step new 'step_name'
	mlh load new 'load_name'
	mlh ext save 'type_transformer'
	#Ouvre sublime text avec deux onglets
	#Fichier python momo.py
	#Fichier config pour l'étape
	mlh ext publish 'ext_name'

#Example d'utilisation
mlh ext 'google_installs' | step 'tutu' -h -c -n -p | replace | cut | load 'big_query'

#mlh appelle le fichier le plus récent dans un dossier temporaire si aucun fichier ou extracteur n'est spécifié
#chaque étape est enregistrer en csv (hdfs ?) => fichier de config mlh
#mlh peut être appelé de n'importe quel dossier
#Double pipe pour marquer un checkpoint ?
#Donne toujours le temps estimé, plus un visuel pour chaque étape

mlh 'toto.csv' | grep 'pantalon'

mlh filter
#Garde uniquement les lignes. Cf grep

mlh join
#Cf csvjoin

mlh sql
#Execute une requête sql sur les données

mlh schema -l
#Édite un schema de donnée avec un label spécifié et/ou des types pour les colonnes
#Infère automatiquement si aucune colonne n'est spécifiée.

mlh check
#Enregistre le dernier fichier en tant que nouveau fichier principal de travail

#==================================================================

#Data Science
#Les commandes s'executent toujours par rapport à un schema (label, type) qui doit être construit avec mlh schema 

mlh split -training 0.75
#Splitte le dataset avec 75% en training ou 30% trai

mlh split -test 0.3
#Idem en se basant sur le pourcentage de test

mlh k-means -k 4
#Réalise un k-mean sur le dataset

mlh reduce -p 3
#Réduit le nombre de dimension du dataset
	mlh reduce -i
	#Information sur la réduction

mlh random-forest -grid-search
#Lance un random-forest avec grid search

mlh pca
#Trouve les composantes principales d'un dataset en fonction de son label
	mlh pca -plot

mlh scale

mlh predict
#Prédit les labels en se basant sur le model courant

mlh check
#Enregistre le modele

mlh build -s -a -n 'toto'
#Construit le pipeline complet avant qu'il ne soit pushé
#Donne un nom au pipeline

mlh run -a -n 'user@domain.com'
#Lance le pipeline de manière asynchrone (-a)
#Notifie l'utilisateur user que la transformation est terminée ou a échoué

mlh destroy 'toto'
#Détruit le pipeline

mlh schedule -c '0 0 0 0'
#Schedule prédiodiquement le pipeline avec une string cron

mlh sync -hostname -user -password
#Synchronise le pipeline sur un serveur
#Push le pipeline de data vers un serveur d'execution 
#Dans un premier temps => se connecte en ssh au serveur et copie les fichiers et modifie le cron en fonction des fichiers locaux
#Push la destruction du pipeline aussi

#======================================================================

#Web UI
#Permet de modifier la date d'execution des scripts
#Permet de consulter les erreurs dans les transformations
#Permet de relancer certaines transformations

mlh server config
#Permet de modifier la configuration du serveur de manière intéractive

mlh server start -p
#Lance un serveur d'execution qui écoute sur le port ...

mlh server stop
#Arrête le server

mlh server restart
#Restart le serveur