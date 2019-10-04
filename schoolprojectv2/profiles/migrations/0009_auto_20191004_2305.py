# Generated by Django 2.2.5 on 2019-10-04 21:05

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20191004_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Droit civil', 'Droit civil'), ('Humanités', 'Humanités'), ('Droit des affaires', 'Droit des affaires'), ('Théâtre', 'Théâtre'), ('Philosophie', 'Philosophie'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Management', 'Management'), ('Mondes anciens', 'Mondes anciens'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Didactique des langues', 'Didactique des langues'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Immunologie', 'Immunologie'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Psychologie', 'Psychologie'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Management public', 'Management public'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Ville et environnements urbains', 'Ville et environnements urbain'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Mécanique', 'Mécanique'), ('Langues et sociétés', 'Langues et sociétés'), ('Economie du développement', 'Economie du développement'), ("Management de l'innovation", "Management de l'innovation"), ('Géomatique', 'Géomatique'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Biomécanique', 'Biomécanique'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Droit administratif', 'Droit administratif'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Français langue étrangère', 'Français langue étrangère'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Théologie protestante', 'Théologie protestante'), ('Information, communication', 'Information, communication'), ('Information, documentation', 'Information, documentation'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Logique', 'Logique'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Mathématiques', 'Mathématiques'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Journalisme', 'Journalisme'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Microbiologie', 'Microbiologie'), ('Physique, chimie', 'Physique, chimie'), ('Arts du spectacle', 'Arts du spectacle'), ('Administration économique et sociale', 'Administration économique et s'), ('Création artistique', 'Création artistique'), ('Danse', 'Danse'), ('Energétique, thermique', 'Energétique, thermique'), ('Droit de la santé', 'Droit de la santé'), ('Ethique', 'Ethique'), ('Droit social', 'Droit social'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Etudes culturelles', 'Etudes culturelles'), ('Droit du numérique', 'Droit du numérique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Droit public', 'Droit public'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Economie du droit', 'Economie du droit'), ('Géographie', 'Géographie'), ('Sciences de la vie', 'Sciences de la vie'), ('Lettres et humanités', 'Lettres et humanités'), ('Economie de la santé', 'Economie de la santé'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Droit des assurances', 'Droit des assurances'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Arts', 'Arts'), ('Sociologie', 'Sociologie'), ('Culture et communication', 'Culture et communication'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Lettres, langues', 'Lettres, langues'), ('Sciences de la mer', 'Sciences de la mer'), ('Génétique', 'Génétique'), ('Psychanalyse', 'Psychanalyse'), ('Management et administration des entreprises', 'Management et administration d'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Economie internationale', 'Economie internationale'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Sciences sociales', 'Sciences sociales'), ('Droit des libertés', 'Droit des libertés'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Management et commerce international', 'Management et commerce interna'), ('Finance', 'Finance'), ('Arts plastiques', 'Arts plastiques'), ('Mondes modernes', 'Mondes modernes'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Droit privé', 'Droit privé'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Economie et management publics', 'Economie et management publics'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Ergonomie', 'Ergonomie'), ('Economie appliquée', 'Economie appliquée'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Génie civil', 'Génie civil'), ('Science politique', 'Science politique'), ('Pharmacologie', 'Pharmacologie'), ('Sciences cognitives', 'Sciences cognitives'), ('Didactique des sciences', 'Didactique des sciences'), ('Génie industriel', 'Génie industriel'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Création numérique', 'Création numérique'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Communication des organisations', 'Communication des organisation'), ('Physique', 'Physique'), ('Economie des organisations', 'Economie des organisations'), ('Chimie', 'Chimie'), ('Marketing, vente', 'Marketing, vente'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Archives', 'Archives'), ('Création littéraire', 'Création littéraire'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Droit', 'Droit'), ('Physique du vivant', 'Physique du vivant'), ('Droit notarial', 'Droit notarial'), ('Sciences et technologies', 'Sciences et technologies'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Sciences du vivant', 'Sciences du vivant'), ('Santé', 'Santé'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Génie mécanique', 'Génie mécanique'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Santé publique', 'Santé publique'), ('Mode', 'Mode'), ("Histoire de l'art", "Histoire de l'art"), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Esthétique', 'Esthétique'), ('Musicologie', 'Musicologie'), ('Management stratégique', 'Management stratégique'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Droit fiscal', 'Droit fiscal'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Energie', 'Energie'), ('Biologie-santé', 'Biologie-santé'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Théologie', 'Théologie'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Sciences économiques et sociales', 'Sciences économiques et social'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit comparé', 'Droit comparé'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Communication publique et politique', 'Communication publique et poli'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Design', 'Design'), ('Acoustique', 'Acoustique'), ('Actuariat', 'Actuariat'), ('Tourisme', 'Tourisme'), ('Démographie', 'Démographie'), ('Industries culturelles', 'Industries culturelles'), ('Mondes contemporains', 'Mondes contemporains'), ('Sciences du langage', 'Sciences du langage'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Humanités numériques', 'Humanités numériques'), ('Ethnologie', 'Ethnologie'), ('Géopolitique', 'Géopolitique'), ('Bio-géosciences', 'Bio-géosciences'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Intelligence économique', 'Intelligence économique'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Informatique', 'Informatique'), ('Etudes du développement', 'Etudes du développement'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Economie et gestion', 'Economie et gestion'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Géographie et aménagement', 'Géographie et aménagement'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Droit européen', 'Droit européen'), ('Politiques comparées', 'Politiques comparées'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Neurosciences', 'Neurosciences'), ('Risques et environnement', 'Risques et environnement'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Relations internationales', 'Relations internationales'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Lettres', 'Lettres'), ("Droit de l'économie", "Droit de l'économie"), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Communication, publicité', 'Communication, publicité'), ('Biotechnologies', 'Biotechnologies'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Droit constitutionnel', 'Droit constitutionnel'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ("Sciences de l'eau", "Sciences de l'eau"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Economie', 'Economie'), ('Biologie', 'Biologie'), ('Droit public des affaires', 'Droit public des affaires'), ('Gestion', 'Gestion'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Anthropologie', 'Anthropologie'), ('Sciences de la matière', 'Sciences de la matière'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Administration publique', 'Administration publique'), ('Biologie végétale', 'Biologie végétale'), ('Automatique, robotique', 'Automatique, robotique'), ('Histoire', 'Histoire'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Bio-informatique', 'Bio-informatique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Finances publiques', 'Finances publiques'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Théologie catholique', 'Théologie catholique'), ('Intervention et développement social', 'Intervention et développement '), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences du médicament', 'Sciences du médicament'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Ethologie', 'Ethologie'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Information-communication', 'Information-communication'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Politiques publiques', 'Politiques publiques'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Biologie du développement', 'Biologie du développement'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Droit international', 'Droit international'), ('Management sectoriel', 'Management sectoriel')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Droit civil', 'Droit civil'), ('Humanités', 'Humanités'), ('Droit des affaires', 'Droit des affaires'), ('Théâtre', 'Théâtre'), ('Philosophie', 'Philosophie'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Management', 'Management'), ('Mondes anciens', 'Mondes anciens'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Didactique des langues', 'Didactique des langues'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Immunologie', 'Immunologie'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Psychologie', 'Psychologie'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Management public', 'Management public'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Ville et environnements urbains', 'Ville et environnements urbain'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Mécanique', 'Mécanique'), ('Langues et sociétés', 'Langues et sociétés'), ('Economie du développement', 'Economie du développement'), ("Management de l'innovation", "Management de l'innovation"), ('Géomatique', 'Géomatique'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Biomécanique', 'Biomécanique'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Droit administratif', 'Droit administratif'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Français langue étrangère', 'Français langue étrangère'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Théologie protestante', 'Théologie protestante'), ('Information, communication', 'Information, communication'), ('Information, documentation', 'Information, documentation'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Logique', 'Logique'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Mathématiques', 'Mathématiques'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Journalisme', 'Journalisme'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Microbiologie', 'Microbiologie'), ('Physique, chimie', 'Physique, chimie'), ('Arts du spectacle', 'Arts du spectacle'), ('Administration économique et sociale', 'Administration économique et s'), ('Création artistique', 'Création artistique'), ('Danse', 'Danse'), ('Energétique, thermique', 'Energétique, thermique'), ('Droit de la santé', 'Droit de la santé'), ('Ethique', 'Ethique'), ('Droit social', 'Droit social'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Etudes culturelles', 'Etudes culturelles'), ('Droit du numérique', 'Droit du numérique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Droit public', 'Droit public'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Economie du droit', 'Economie du droit'), ('Géographie', 'Géographie'), ('Sciences de la vie', 'Sciences de la vie'), ('Lettres et humanités', 'Lettres et humanités'), ('Economie de la santé', 'Economie de la santé'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Droit des assurances', 'Droit des assurances'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Arts', 'Arts'), ('Sociologie', 'Sociologie'), ('Culture et communication', 'Culture et communication'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Lettres, langues', 'Lettres, langues'), ('Sciences de la mer', 'Sciences de la mer'), ('Génétique', 'Génétique'), ('Psychanalyse', 'Psychanalyse'), ('Management et administration des entreprises', 'Management et administration d'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Economie internationale', 'Economie internationale'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Sciences sociales', 'Sciences sociales'), ('Droit des libertés', 'Droit des libertés'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Management et commerce international', 'Management et commerce interna'), ('Finance', 'Finance'), ('Arts plastiques', 'Arts plastiques'), ('Mondes modernes', 'Mondes modernes'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Droit privé', 'Droit privé'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Economie et management publics', 'Economie et management publics'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Ergonomie', 'Ergonomie'), ('Economie appliquée', 'Economie appliquée'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Génie civil', 'Génie civil'), ('Science politique', 'Science politique'), ('Pharmacologie', 'Pharmacologie'), ('Sciences cognitives', 'Sciences cognitives'), ('Didactique des sciences', 'Didactique des sciences'), ('Génie industriel', 'Génie industriel'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Création numérique', 'Création numérique'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Communication des organisations', 'Communication des organisation'), ('Physique', 'Physique'), ('Economie des organisations', 'Economie des organisations'), ('Chimie', 'Chimie'), ('Marketing, vente', 'Marketing, vente'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Archives', 'Archives'), ('Création littéraire', 'Création littéraire'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Droit', 'Droit'), ('Physique du vivant', 'Physique du vivant'), ('Droit notarial', 'Droit notarial'), ('Sciences et technologies', 'Sciences et technologies'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Sciences du vivant', 'Sciences du vivant'), ('Santé', 'Santé'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Génie mécanique', 'Génie mécanique'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Santé publique', 'Santé publique'), ('Mode', 'Mode'), ("Histoire de l'art", "Histoire de l'art"), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Esthétique', 'Esthétique'), ('Musicologie', 'Musicologie'), ('Management stratégique', 'Management stratégique'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Droit fiscal', 'Droit fiscal'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Energie', 'Energie'), ('Biologie-santé', 'Biologie-santé'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Théologie', 'Théologie'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Sciences économiques et sociales', 'Sciences économiques et social'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit comparé', 'Droit comparé'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Communication publique et politique', 'Communication publique et poli'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Design', 'Design'), ('Acoustique', 'Acoustique'), ('Actuariat', 'Actuariat'), ('Tourisme', 'Tourisme'), ('Démographie', 'Démographie'), ('Industries culturelles', 'Industries culturelles'), ('Mondes contemporains', 'Mondes contemporains'), ('Sciences du langage', 'Sciences du langage'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Humanités numériques', 'Humanités numériques'), ('Ethnologie', 'Ethnologie'), ('Géopolitique', 'Géopolitique'), ('Bio-géosciences', 'Bio-géosciences'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Intelligence économique', 'Intelligence économique'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Informatique', 'Informatique'), ('Etudes du développement', 'Etudes du développement'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Economie et gestion', 'Economie et gestion'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Géographie et aménagement', 'Géographie et aménagement'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Droit européen', 'Droit européen'), ('Politiques comparées', 'Politiques comparées'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Neurosciences', 'Neurosciences'), ('Risques et environnement', 'Risques et environnement'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Relations internationales', 'Relations internationales'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Lettres', 'Lettres'), ("Droit de l'économie", "Droit de l'économie"), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Communication, publicité', 'Communication, publicité'), ('Biotechnologies', 'Biotechnologies'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Droit constitutionnel', 'Droit constitutionnel'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ("Sciences de l'eau", "Sciences de l'eau"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Economie', 'Economie'), ('Biologie', 'Biologie'), ('Droit public des affaires', 'Droit public des affaires'), ('Gestion', 'Gestion'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Anthropologie', 'Anthropologie'), ('Sciences de la matière', 'Sciences de la matière'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Administration publique', 'Administration publique'), ('Biologie végétale', 'Biologie végétale'), ('Automatique, robotique', 'Automatique, robotique'), ('Histoire', 'Histoire'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Bio-informatique', 'Bio-informatique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Finances publiques', 'Finances publiques'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Théologie catholique', 'Théologie catholique'), ('Intervention et développement social', 'Intervention et développement '), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences du médicament', 'Sciences du médicament'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Ethologie', 'Ethologie'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Information-communication', 'Information-communication'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Politiques publiques', 'Politiques publiques'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Biologie du développement', 'Biologie du développement'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Droit international', 'Droit international'), ('Management sectoriel', 'Management sectoriel')], max_length=271, null=True),
        ),
    ]
