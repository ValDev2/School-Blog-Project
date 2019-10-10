# Generated by Django 2.2.5 on 2019-10-09 06:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20191009_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Droit des libertés', 'Droit des libertés'), ('Géopolitique', 'Géopolitique'), ('Logique', 'Logique'), ('Psychologie', 'Psychologie'), ("Management des systèmes d'information", "Management des systèmes d'info"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Sciences de la vie', 'Sciences de la vie'), ('Actuariat', 'Actuariat'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences de la mer', 'Sciences de la mer'), ("Management de l'innovation", "Management de l'innovation"), ('Droit international', 'Droit international'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Histoire', 'Histoire'), ('Biologie', 'Biologie'), ('Acoustique', 'Acoustique'), ('Création numérique', 'Création numérique'), ('Géomatique', 'Géomatique'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Management sectoriel', 'Management sectoriel'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Communication publique et politique', 'Communication publique et poli'), ('Information, documentation', 'Information, documentation'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Lettres, langues', 'Lettres, langues'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Droit social', 'Droit social'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Didactique des sciences', 'Didactique des sciences'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Droit de la santé', 'Droit de la santé'), ('Bio-géosciences', 'Bio-géosciences'), ('Santé', 'Santé'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Finance', 'Finance'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Création artistique', 'Création artistique'), ('Marketing, vente', 'Marketing, vente'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Histoire de l'art", "Histoire de l'art"), ('Economie appliquée', 'Economie appliquée'), ('Humanités', 'Humanités'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Géographie', 'Géographie'), ('Droit administratif', 'Droit administratif'), ("Sciences de l'eau", "Sciences de l'eau"), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit public', 'Droit public'), ('Sciences cognitives', 'Sciences cognitives'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Lettres', 'Lettres'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences et technologies', 'Sciences et technologies'), ('Biomécanique', 'Biomécanique'), ('Droit', 'Droit'), ('Bio-informatique', 'Bio-informatique'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Etudes culturelles', 'Etudes culturelles'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Etudes du développement', 'Etudes du développement'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Management et administration des entreprises', 'Management et administration d'), ('Politiques comparées', 'Politiques comparées'), ('Archives', 'Archives'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Sciences sociales', 'Sciences sociales'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Français langue étrangère', 'Français langue étrangère'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Culture et communication', 'Culture et communication'), ('Informatique', 'Informatique'), ('Arts', 'Arts'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Santé publique', 'Santé publique'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Microbiologie', 'Microbiologie'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Arts du spectacle', 'Arts du spectacle'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Anthropologie', 'Anthropologie'), ('Danse', 'Danse'), ('Information, communication', 'Information, communication'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Génie mécanique', 'Génie mécanique'), ('Information-communication', 'Information-communication'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Ethologie', 'Ethologie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Sciences du vivant', 'Sciences du vivant'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Economie du développement', 'Economie du développement'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Théologie protestante', 'Théologie protestante'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ethnologie', 'Ethnologie'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mondes anciens', 'Mondes anciens'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Droit notarial', 'Droit notarial'), ('Droit européen', 'Droit européen'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Droit comparé', 'Droit comparé'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Physique, chimie', 'Physique, chimie'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Démographie', 'Démographie'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Communication des organisations', 'Communication des organisation'), ('Droit des assurances', 'Droit des assurances'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Administration publique', 'Administration publique'), ('Humanités numériques', 'Humanités numériques'), ('Sciences de la matière', 'Sciences de la matière'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Management public', 'Management public'), ('Immunologie', 'Immunologie'), ('Communication, publicité', 'Communication, publicité'), ('Sociologie', 'Sociologie'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Design', 'Design'), ('Ergonomie', 'Ergonomie'), ('Musicologie', 'Musicologie'), ('Biologie végétale', 'Biologie végétale'), ('Biologie-santé', 'Biologie-santé'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Science politique', 'Science politique'), ('Economie et gestion', 'Economie et gestion'), ('Théologie', 'Théologie'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Finances publiques', 'Finances publiques'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Economie du droit', 'Economie du droit'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Gestion', 'Gestion'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ("Droit de l'économie", "Droit de l'économie"), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Economie des organisations', 'Economie des organisations'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Mondes contemporains', 'Mondes contemporains'), ('Journalisme', 'Journalisme'), ('Biologie du développement', 'Biologie du développement'), ('Management stratégique', 'Management stratégique'), ('Philosophie', 'Philosophie'), ('Didactique des langues', 'Didactique des langues'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Langues et sociétés', 'Langues et sociétés'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Biotechnologies', 'Biotechnologies'), ('Mécanique', 'Mécanique'), ('Arts plastiques', 'Arts plastiques'), ('Chimie', 'Chimie'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Relations internationales', 'Relations internationales'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Politiques publiques', 'Politiques publiques'), ('Droit civil', 'Droit civil'), ('Neurosciences', 'Neurosciences'), ('Sciences du langage', 'Sciences du langage'), ('Théologie catholique', 'Théologie catholique'), ('Economie et management publics', 'Economie et management publics'), ('Risques et environnement', 'Risques et environnement'), ('Automatique, robotique', 'Automatique, robotique'), ('Physique', 'Physique'), ('Lettres et humanités', 'Lettres et humanités'), ('Energétique, thermique', 'Energétique, thermique'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Energie', 'Energie'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Génétique', 'Génétique'), ('Droit du numérique', 'Droit du numérique'), ('Tourisme', 'Tourisme'), ('Economie', 'Economie'), ('Physique du vivant', 'Physique du vivant'), ('Ethique', 'Ethique'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Management', 'Management'), ('Industries culturelles', 'Industries culturelles'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Esthétique', 'Esthétique'), ('Génie civil', 'Génie civil'), ('Psychanalyse', 'Psychanalyse'), ('Droit privé', 'Droit privé'), ('Economie internationale', 'Economie internationale'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Droit fiscal', 'Droit fiscal'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Economie de la santé', 'Economie de la santé'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Intelligence économique', 'Intelligence économique'), ('Sciences du médicament', 'Sciences du médicament'), ('Droit public des affaires', 'Droit public des affaires'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Droit des affaires', 'Droit des affaires'), ('Génie industriel', 'Génie industriel'), ('Mode', 'Mode'), ('Création littéraire', 'Création littéraire'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Mondes modernes', 'Mondes modernes'), ('Management et commerce international', 'Management et commerce interna'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Pharmacologie', 'Pharmacologie'), ('Mathématiques', 'Mathématiques'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Administration économique et sociale', 'Administration économique et s'), ('Théâtre', 'Théâtre')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Droit des libertés', 'Droit des libertés'), ('Géopolitique', 'Géopolitique'), ('Logique', 'Logique'), ('Psychologie', 'Psychologie'), ("Management des systèmes d'information", "Management des systèmes d'info"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Sciences de la vie', 'Sciences de la vie'), ('Actuariat', 'Actuariat'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences de la mer', 'Sciences de la mer'), ("Management de l'innovation", "Management de l'innovation"), ('Droit international', 'Droit international'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Histoire', 'Histoire'), ('Biologie', 'Biologie'), ('Acoustique', 'Acoustique'), ('Création numérique', 'Création numérique'), ('Géomatique', 'Géomatique'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Management sectoriel', 'Management sectoriel'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Communication publique et politique', 'Communication publique et poli'), ('Information, documentation', 'Information, documentation'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Lettres, langues', 'Lettres, langues'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Droit social', 'Droit social'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Didactique des sciences', 'Didactique des sciences'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Droit de la santé', 'Droit de la santé'), ('Bio-géosciences', 'Bio-géosciences'), ('Santé', 'Santé'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Finance', 'Finance'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Création artistique', 'Création artistique'), ('Marketing, vente', 'Marketing, vente'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Histoire de l'art", "Histoire de l'art"), ('Economie appliquée', 'Economie appliquée'), ('Humanités', 'Humanités'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Géographie', 'Géographie'), ('Droit administratif', 'Droit administratif'), ("Sciences de l'eau", "Sciences de l'eau"), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit public', 'Droit public'), ('Sciences cognitives', 'Sciences cognitives'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Lettres', 'Lettres'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences et technologies', 'Sciences et technologies'), ('Biomécanique', 'Biomécanique'), ('Droit', 'Droit'), ('Bio-informatique', 'Bio-informatique'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Etudes culturelles', 'Etudes culturelles'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Etudes du développement', 'Etudes du développement'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Management et administration des entreprises', 'Management et administration d'), ('Politiques comparées', 'Politiques comparées'), ('Archives', 'Archives'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Sciences sociales', 'Sciences sociales'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Français langue étrangère', 'Français langue étrangère'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Culture et communication', 'Culture et communication'), ('Informatique', 'Informatique'), ('Arts', 'Arts'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Santé publique', 'Santé publique'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Microbiologie', 'Microbiologie'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Arts du spectacle', 'Arts du spectacle'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Anthropologie', 'Anthropologie'), ('Danse', 'Danse'), ('Information, communication', 'Information, communication'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Génie mécanique', 'Génie mécanique'), ('Information-communication', 'Information-communication'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Ethologie', 'Ethologie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Sciences du vivant', 'Sciences du vivant'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Economie du développement', 'Economie du développement'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Théologie protestante', 'Théologie protestante'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ethnologie', 'Ethnologie'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mondes anciens', 'Mondes anciens'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Droit notarial', 'Droit notarial'), ('Droit européen', 'Droit européen'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Droit comparé', 'Droit comparé'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Physique, chimie', 'Physique, chimie'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Démographie', 'Démographie'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Communication des organisations', 'Communication des organisation'), ('Droit des assurances', 'Droit des assurances'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Administration publique', 'Administration publique'), ('Humanités numériques', 'Humanités numériques'), ('Sciences de la matière', 'Sciences de la matière'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Management public', 'Management public'), ('Immunologie', 'Immunologie'), ('Communication, publicité', 'Communication, publicité'), ('Sociologie', 'Sociologie'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Design', 'Design'), ('Ergonomie', 'Ergonomie'), ('Musicologie', 'Musicologie'), ('Biologie végétale', 'Biologie végétale'), ('Biologie-santé', 'Biologie-santé'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Science politique', 'Science politique'), ('Economie et gestion', 'Economie et gestion'), ('Théologie', 'Théologie'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Finances publiques', 'Finances publiques'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Economie du droit', 'Economie du droit'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Gestion', 'Gestion'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ("Droit de l'économie", "Droit de l'économie"), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Economie des organisations', 'Economie des organisations'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Mondes contemporains', 'Mondes contemporains'), ('Journalisme', 'Journalisme'), ('Biologie du développement', 'Biologie du développement'), ('Management stratégique', 'Management stratégique'), ('Philosophie', 'Philosophie'), ('Didactique des langues', 'Didactique des langues'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Langues et sociétés', 'Langues et sociétés'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Biotechnologies', 'Biotechnologies'), ('Mécanique', 'Mécanique'), ('Arts plastiques', 'Arts plastiques'), ('Chimie', 'Chimie'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Relations internationales', 'Relations internationales'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Politiques publiques', 'Politiques publiques'), ('Droit civil', 'Droit civil'), ('Neurosciences', 'Neurosciences'), ('Sciences du langage', 'Sciences du langage'), ('Théologie catholique', 'Théologie catholique'), ('Economie et management publics', 'Economie et management publics'), ('Risques et environnement', 'Risques et environnement'), ('Automatique, robotique', 'Automatique, robotique'), ('Physique', 'Physique'), ('Lettres et humanités', 'Lettres et humanités'), ('Energétique, thermique', 'Energétique, thermique'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Energie', 'Energie'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Génétique', 'Génétique'), ('Droit du numérique', 'Droit du numérique'), ('Tourisme', 'Tourisme'), ('Economie', 'Economie'), ('Physique du vivant', 'Physique du vivant'), ('Ethique', 'Ethique'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Management', 'Management'), ('Industries culturelles', 'Industries culturelles'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Esthétique', 'Esthétique'), ('Génie civil', 'Génie civil'), ('Psychanalyse', 'Psychanalyse'), ('Droit privé', 'Droit privé'), ('Economie internationale', 'Economie internationale'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Droit fiscal', 'Droit fiscal'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Economie de la santé', 'Economie de la santé'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Intelligence économique', 'Intelligence économique'), ('Sciences du médicament', 'Sciences du médicament'), ('Droit public des affaires', 'Droit public des affaires'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Droit des affaires', 'Droit des affaires'), ('Génie industriel', 'Génie industriel'), ('Mode', 'Mode'), ('Création littéraire', 'Création littéraire'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Mondes modernes', 'Mondes modernes'), ('Management et commerce international', 'Management et commerce interna'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Pharmacologie', 'Pharmacologie'), ('Mathématiques', 'Mathématiques'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Administration économique et sociale', 'Administration économique et s'), ('Théâtre', 'Théâtre')], max_length=271, null=True),
        ),
    ]
