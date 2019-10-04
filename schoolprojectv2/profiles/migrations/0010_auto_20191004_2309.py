# Generated by Django 2.2.5 on 2019-10-04 21:09

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20191004_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Information, documentation', 'Information, documentation'), ('Actuariat', 'Actuariat'), ('Didactique des sciences', 'Didactique des sciences'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Arts', 'Arts'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Aéronautique et espace', 'Aéronautique et espace'), ('Santé', 'Santé'), ('Arts du spectacle', 'Arts du spectacle'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Droit civil', 'Droit civil'), ('Ergonomie', 'Ergonomie'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Droit public des affaires', 'Droit public des affaires'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Tourisme', 'Tourisme'), ('Management', 'Management'), ('Chimie', 'Chimie'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit des affaires', 'Droit des affaires'), ('Création artistique', 'Création artistique'), ('Droit du patrimoine', 'Droit du patrimoine'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Sciences du médicament', 'Sciences du médicament'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Information, communication', 'Information, communication'), ('Economie des organisations', 'Economie des organisations'), ('Langues et sociétés', 'Langues et sociétés'), ('Logique', 'Logique'), ('Science politique', 'Science politique'), ('Sciences du vivant', 'Sciences du vivant'), ('Génie industriel', 'Génie industriel'), ('Economie internationale', 'Economie internationale'), ('Droit comparé', 'Droit comparé'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Biologie', 'Biologie'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Economie appliquée', 'Economie appliquée'), ('Théologie catholique', 'Théologie catholique'), ('Energétique, thermique', 'Energétique, thermique'), ('Mécanique', 'Mécanique'), ('Management et commerce international', 'Management et commerce interna'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Management stratégique', 'Management stratégique'), ('Sciences du langage', 'Sciences du langage'), ('Bio-géosciences', 'Bio-géosciences'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Droit des assurances', 'Droit des assurances'), ('Psychologie', 'Psychologie'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Théologie', 'Théologie'), ('Lettres et humanités', 'Lettres et humanités'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Politiques publiques', 'Politiques publiques'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mode', 'Mode'), ('Humanités numériques', 'Humanités numériques'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Géographie', 'Géographie'), ('Génie civil', 'Génie civil'), ('Ethologie', 'Ethologie'), ('Communication des organisations', 'Communication des organisation'), ('Droit des libertés', 'Droit des libertés'), ('Physique', 'Physique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Géopolitique', 'Géopolitique'), ('Management public', 'Management public'), ('Physique du vivant', 'Physique du vivant'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Informatique', 'Informatique'), ('Communication publique et politique', 'Communication publique et poli'), ('Théologie protestante', 'Théologie protestante'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Arts plastiques', 'Arts plastiques'), ("Histoire de l'art", "Histoire de l'art"), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Mondes contemporains', 'Mondes contemporains'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Création littéraire', 'Création littéraire'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Energie', 'Energie'), ('Création numérique', 'Création numérique'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Danse', 'Danse'), ('Droit de la santé', 'Droit de la santé'), ('Humanités', 'Humanités'), ('Sciences de la vie', 'Sciences de la vie'), ('Physique, chimie', 'Physique, chimie'), ('Journalisme', 'Journalisme'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Management sectoriel', 'Management sectoriel'), ('Droit privé', 'Droit privé'), ('Anthropologie', 'Anthropologie'), ('Droit public', 'Droit public'), ('Etudes culturelles', 'Etudes culturelles'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Traduction et interprétation', 'Traduction et interprétation'), ("Sciences de l'eau", "Sciences de l'eau"), ('Démographie', 'Démographie'), ('Marketing, vente', 'Marketing, vente'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Sciences et technologies', 'Sciences et technologies'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Information-communication', 'Information-communication'), ('Théâtre', 'Théâtre'), ('Acoustique', 'Acoustique'), ('Administration publique', 'Administration publique'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Design', 'Design'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Intelligence économique', 'Intelligence économique'), ('Droit fiscal', 'Droit fiscal'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Psychanalyse', 'Psychanalyse'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Sciences de la mer', 'Sciences de la mer'), ('Lettres', 'Lettres'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Finance', 'Finance'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Musicologie', 'Musicologie'), ('Economie', 'Economie'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Droit européen', 'Droit européen'), ('Droit international', 'Droit international'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Industries culturelles', 'Industries culturelles'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Littérature générale et comparée', 'Littérature générale et compar'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Gestion', 'Gestion'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Automatique, robotique', 'Automatique, robotique'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Administration économique et sociale', 'Administration économique et s'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Economie de la santé', 'Economie de la santé'), ('Ethnologie', 'Ethnologie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Risques et environnement', 'Risques et environnement'), ('Biologie du développement', 'Biologie du développement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences cognitives', 'Sciences cognitives'), ('Droit du numérique', 'Droit du numérique'), ('Droit administratif', 'Droit administratif'), ('Biomécanique', 'Biomécanique'), ('Didactique des langues', 'Didactique des langues'), ('Droit notarial', 'Droit notarial'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Sociologie', 'Sociologie'), ("Management de l'innovation", "Management de l'innovation"), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Microbiologie', 'Microbiologie'), ('Archives', 'Archives'), ('Etudes du développement', 'Etudes du développement'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Biologie-santé', 'Biologie-santé'), ('Relations internationales', 'Relations internationales'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Mondes anciens', 'Mondes anciens'), ('Esthétique', 'Esthétique'), ('Ethique', 'Ethique'), ('Biotechnologies', 'Biotechnologies'), ('Politiques comparées', 'Politiques comparées'), ('Economie et management publics', 'Economie et management publics'), ('Communication, publicité', 'Communication, publicité'), ('Santé publique', 'Santé publique'), ('Biologie végétale', 'Biologie végétale'), ('Mondes modernes', 'Mondes modernes'), ('Philosophie', 'Philosophie'), ('Culture et communication', 'Culture et communication'), ('Pharmacologie', 'Pharmacologie'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Génie mécanique', 'Génie mécanique'), ('Bio-informatique', 'Bio-informatique'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Français langue étrangère', 'Français langue étrangère'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Immunologie', 'Immunologie'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Finances publiques', 'Finances publiques'), ('Economie du développement', 'Economie du développement'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Génétique', 'Génétique'), ('Droit', 'Droit'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Neurosciences', 'Neurosciences'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences de la matière', 'Sciences de la matière'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Géomatique', 'Géomatique'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Economie et gestion', 'Economie et gestion'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Management et administration des entreprises', 'Management et administration d'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ("Droit de l'économie", "Droit de l'économie"), ('Droit social', 'Droit social'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Mathématiques', 'Mathématiques'), ('Lettres, langues', 'Lettres, langues'), ('Economie du droit', 'Economie du droit'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Histoire', 'Histoire'), ('Sciences sociales', 'Sciences sociales'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur")], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Information, documentation', 'Information, documentation'), ('Actuariat', 'Actuariat'), ('Didactique des sciences', 'Didactique des sciences'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Arts', 'Arts'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Aéronautique et espace', 'Aéronautique et espace'), ('Santé', 'Santé'), ('Arts du spectacle', 'Arts du spectacle'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Droit civil', 'Droit civil'), ('Ergonomie', 'Ergonomie'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Droit public des affaires', 'Droit public des affaires'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Tourisme', 'Tourisme'), ('Management', 'Management'), ('Chimie', 'Chimie'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit des affaires', 'Droit des affaires'), ('Création artistique', 'Création artistique'), ('Droit du patrimoine', 'Droit du patrimoine'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Sciences du médicament', 'Sciences du médicament'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Information, communication', 'Information, communication'), ('Economie des organisations', 'Economie des organisations'), ('Langues et sociétés', 'Langues et sociétés'), ('Logique', 'Logique'), ('Science politique', 'Science politique'), ('Sciences du vivant', 'Sciences du vivant'), ('Génie industriel', 'Génie industriel'), ('Economie internationale', 'Economie internationale'), ('Droit comparé', 'Droit comparé'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Biologie', 'Biologie'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Economie appliquée', 'Economie appliquée'), ('Théologie catholique', 'Théologie catholique'), ('Energétique, thermique', 'Energétique, thermique'), ('Mécanique', 'Mécanique'), ('Management et commerce international', 'Management et commerce interna'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Management stratégique', 'Management stratégique'), ('Sciences du langage', 'Sciences du langage'), ('Bio-géosciences', 'Bio-géosciences'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Droit des assurances', 'Droit des assurances'), ('Psychologie', 'Psychologie'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Théologie', 'Théologie'), ('Lettres et humanités', 'Lettres et humanités'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Politiques publiques', 'Politiques publiques'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mode', 'Mode'), ('Humanités numériques', 'Humanités numériques'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Géographie', 'Géographie'), ('Génie civil', 'Génie civil'), ('Ethologie', 'Ethologie'), ('Communication des organisations', 'Communication des organisation'), ('Droit des libertés', 'Droit des libertés'), ('Physique', 'Physique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Géopolitique', 'Géopolitique'), ('Management public', 'Management public'), ('Physique du vivant', 'Physique du vivant'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Informatique', 'Informatique'), ('Communication publique et politique', 'Communication publique et poli'), ('Théologie protestante', 'Théologie protestante'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Arts plastiques', 'Arts plastiques'), ("Histoire de l'art", "Histoire de l'art"), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Mondes contemporains', 'Mondes contemporains'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Création littéraire', 'Création littéraire'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Energie', 'Energie'), ('Création numérique', 'Création numérique'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Danse', 'Danse'), ('Droit de la santé', 'Droit de la santé'), ('Humanités', 'Humanités'), ('Sciences de la vie', 'Sciences de la vie'), ('Physique, chimie', 'Physique, chimie'), ('Journalisme', 'Journalisme'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Management sectoriel', 'Management sectoriel'), ('Droit privé', 'Droit privé'), ('Anthropologie', 'Anthropologie'), ('Droit public', 'Droit public'), ('Etudes culturelles', 'Etudes culturelles'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Traduction et interprétation', 'Traduction et interprétation'), ("Sciences de l'eau", "Sciences de l'eau"), ('Démographie', 'Démographie'), ('Marketing, vente', 'Marketing, vente'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Sciences et technologies', 'Sciences et technologies'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Information-communication', 'Information-communication'), ('Théâtre', 'Théâtre'), ('Acoustique', 'Acoustique'), ('Administration publique', 'Administration publique'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Design', 'Design'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Intelligence économique', 'Intelligence économique'), ('Droit fiscal', 'Droit fiscal'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Psychanalyse', 'Psychanalyse'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Sciences de la mer', 'Sciences de la mer'), ('Lettres', 'Lettres'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Finance', 'Finance'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Musicologie', 'Musicologie'), ('Economie', 'Economie'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Droit européen', 'Droit européen'), ('Droit international', 'Droit international'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Industries culturelles', 'Industries culturelles'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Littérature générale et comparée', 'Littérature générale et compar'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Gestion', 'Gestion'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Automatique, robotique', 'Automatique, robotique'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Administration économique et sociale', 'Administration économique et s'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Economie de la santé', 'Economie de la santé'), ('Ethnologie', 'Ethnologie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Risques et environnement', 'Risques et environnement'), ('Biologie du développement', 'Biologie du développement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences cognitives', 'Sciences cognitives'), ('Droit du numérique', 'Droit du numérique'), ('Droit administratif', 'Droit administratif'), ('Biomécanique', 'Biomécanique'), ('Didactique des langues', 'Didactique des langues'), ('Droit notarial', 'Droit notarial'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Sociologie', 'Sociologie'), ("Management de l'innovation", "Management de l'innovation"), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Microbiologie', 'Microbiologie'), ('Archives', 'Archives'), ('Etudes du développement', 'Etudes du développement'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Biologie-santé', 'Biologie-santé'), ('Relations internationales', 'Relations internationales'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Mondes anciens', 'Mondes anciens'), ('Esthétique', 'Esthétique'), ('Ethique', 'Ethique'), ('Biotechnologies', 'Biotechnologies'), ('Politiques comparées', 'Politiques comparées'), ('Economie et management publics', 'Economie et management publics'), ('Communication, publicité', 'Communication, publicité'), ('Santé publique', 'Santé publique'), ('Biologie végétale', 'Biologie végétale'), ('Mondes modernes', 'Mondes modernes'), ('Philosophie', 'Philosophie'), ('Culture et communication', 'Culture et communication'), ('Pharmacologie', 'Pharmacologie'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Génie mécanique', 'Génie mécanique'), ('Bio-informatique', 'Bio-informatique'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Français langue étrangère', 'Français langue étrangère'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Immunologie', 'Immunologie'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Finances publiques', 'Finances publiques'), ('Economie du développement', 'Economie du développement'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Génétique', 'Génétique'), ('Droit', 'Droit'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Neurosciences', 'Neurosciences'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences de la matière', 'Sciences de la matière'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Géomatique', 'Géomatique'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Economie et gestion', 'Economie et gestion'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Management et administration des entreprises', 'Management et administration d'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ("Droit de l'économie", "Droit de l'économie"), ('Droit social', 'Droit social'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Mathématiques', 'Mathématiques'), ('Lettres, langues', 'Lettres, langues'), ('Economie du droit', 'Economie du droit'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Histoire', 'Histoire'), ('Sciences sociales', 'Sciences sociales'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur")], max_length=271, null=True),
        ),
    ]
