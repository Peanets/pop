#Config

#Csv, Hdfs, Db
#Crédentials des différents plugins. Les plugins doivent demander les crédentials à l'installation

#Package Managment

pop push
#Commit toutes les modifications dans .pop et push au serveur

pop pull
#git pull tous les changements

pop plugin -ls 'toto'
#liste les plugins téléchargeables au nom de toto

pop plugin -install 'tutu'
#Télécharge le plugin tutu qui devient accessible avec 'pop tutu' ou importe plusieurs commandes (pop data-analyse, pop data-science, pop server)

pop plugin -uninstall 'tutu'

#====================================================================

pop config
#Configure le dossier principal
	pop config 'tutu'
	#Configure la transformation tutu

pop home
#Retourne au dossier principal

pop go 'tutu'
#Reviens dans le dossier principal de tutu 

pop init 'tutu'
#Créer une nouvelle transformation du nom de tutu
#Créer un nouveau répertoire dans le dossier principal
#Créer un fichier de config

pop catch 'tutu'
#Ouvre une fenêtre qui permet de déposer le fichier
#Ferme ensuite la fénêtre et reviens à la fenêtre de terminal dans le bon dossier

#====================================================================

#Data Analyse

pop doctor
#Remplace les valeurs manquantes
#Convertit toutes les dates dans le même format

pop sanitize
#Convertit les noms de donnée (minuscule, underscore)
#Transforme le format des dates,
#remplace les autres séparateurs par des virgules, 
	pop sanitize -convert -transform -replace

pop checkup
#Informe sur le type de donnée dans chaque catégorie
#Informe sur des erreurs de parsing et affiche les valeurs qui font défaut

pop stats
#cf cvsstat

pop keep
#garde certaines colonnes

pop ipython

pop cut
#supprime certaine colonne

pop do bidule.py
#Execute une transformation sur la donnée en donnant un dataframe en input

pop 
pop make
#Construit le pipeline

#Affiche les différents source de données accessibles.
#Extrait depuis une source de donnée et stocke le résultat en csv
	pop extract csv -s schema.json
	#Si aucun schema n'est spécifié, demander de manière interactive
	pop extract big_query -q toto.sql
	pop extract my_sql -q tutu.sql
	pop extract elastic -q machin.json
	#Demande le nom à donner à cette source de donnée si besoin.
	#Génére un schema directement et stocke la donnée dans un dossier spécifique avec son schema et sa requête

pop load
#Charge les données vers différentes destination
	pop load hdfs
	pop load big_query -table ...
	pop load sql -table ...
	pop load storage path
	pop mail
	#La donnée est toujours accessible après le load. Plusieurs load possible.

pop use a
#Utilise cette source de donnée pour les transformations suivantes

pop join a b
#Join des source de donnée

pop tee a b
#Copie la source de donnée avec le nom b

pop mail -s 'Sujet' toto@domain.com
#Envois le csv par mail

pop download '/*.xlsx'
#Download tous les fichiers dans google cloud storage avec le pattern demandé

pop upload 'tutu'
#upload dans google storage le fichier avec le nom spécifié

pop look
#affiche les données sous forme de tableau
	pop look -plot
	#affiche les données sous forme de graphique #Quid des dates ? 
	pop look -hist
	#affiche un histogramme des données
	pop look -tail
	pop look -head
	pop look -columns
	pop look -tableau
	#Lance tableau avec le csv en source de donnée
	pop look -excel
	pop look -numbers

pop replace
#Remplace les caractères
	pop replace -h
	#Remplace uniquement le header

pop ext -limit
#Génère des données d'un échantillon fixé par size
#-q permet de fixer la taille de la queue entrante
pop step -q
pop load -q
#Appelle un extracteur dans un dossier d'extracteur
#Idem dans un dossier de step et de loader
	pop ext new 'ext_name'
	pop step new 'step_name'
	pop load new 'load_name'
	pop ext save 'type_transformer'
	#Ouvre sublime text avec deux onglets
	#Fichier python momo.py
	#Fichier config pour l'étape
	pop ext publish 'ext_name'

#Example d'utilisation
pop step 'google_ext' | step 'tutu' -h -c -n -p | replace | cut | step 'big_query'

#pop appelle le fichier le plus récent dans un dossier temporaire si aucun fichier ou extracteur n'est spécifié
#chaque étape est enregistrer en csv (hdfs ?) => fichier de config pop
#pop peut être appelé de n'importe quel dossier
#Double pipe pour marquer un checkpoint ?
#Donne toujours le temps estimé, plus un visuel pour chaque étape

pop 'toto.csv' | grep 'pantalon'

pop filter
#Garde uniquement les lignes. Cf grep

pop join
#Cf csvjoin

pop sql
#Execute une requête sql sur les données

pop schema
#Édite un schema de donnée avec un label spécifié et/ou des types pour les colonnes
#Infère automatiquement si aucune colonne n'est spécifiée.

pop check
#Enregistre le dernier fichier en tant que nouveau fichier principal de travail

#==================================================================

#Data Science
#Les commandes s'executent toujours par rapport à un schema (label, type) qui doit être construit avec pop schema 

pop split -training 0.75
#Splitte le dataset avec 75% en training ou 30% trai

pop split -test 0.3
#Idem en se basant sur le pourcentage de test

pop k-means -k 4
#Réalise un k-mean sur le dataset

pop reduce -p 3
#Réduit le nombre de dimension du dataset
	pop reduce -i
	#Information sur la réduction

pop random-forest -grid-search
#Lance un random-forest avec grid search

pop pca
#Trouve les composantes principales d'un dataset en fonction de son label
	pop pca -plot

pop scale

pop predict
#Prédit les labels en se basant sur le model courant

pop check
#Enregistre le modele

pop build -s -a -n 'toto'
#Construit le pipeline complet avant qu'il ne soit pushé
#Donne un nom au pipeline

pop run -a -n 'user@domain.com'
#Lance le pipeline de manière asynchrone (-a)
#Notifie l'utilisateur user que la transformation est terminée ou a échoué

pop destroy 'toto'
#Détruit le pipeline

pop schedule -c '0 0 0 0'
#Schedule prédiodiquement le pipeline avec une string cron

pop sync -hostname -user -password
#Synchronise le pipeline sur un serveur
#Push le pipeline de data vers un serveur d'execution 
#Dans un premier temps => se connecte en ssh au serveur et copie les fichiers et modifie le cron en fonction des fichiers locaux
#Push la destruction du pipeline aussi

#======================================================================

#Web UI
#Permet de modifier la date d'execution des scripts
#Permet de consulter les erreurs dans les transformations
#Permet de relancer certaines transformations

pop server config
#Permet de modifier la configuration du serveur de manière intéractive

pop server start -p
#Lance un serveur d'execution qui écoute sur le port ...

pop server stop
#Arrête le server

pop server restart
#Restart le serveur