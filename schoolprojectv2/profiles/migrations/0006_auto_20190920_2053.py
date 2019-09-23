# Generated by Django 2.2.5 on 2019-09-20 18:53

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20190920_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Droit social', 'Droit social'), ('Finance', 'Finance'), ('Sciences de la matière', 'Sciences de la matière'), ('Politiques publiques', 'Politiques publiques'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Ethnologie', 'Ethnologie'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Patrimoine et musées', 'Patrimoine et musées'), ('Energétique, thermique', 'Energétique, thermique'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Culture et communication', 'Culture et communication'), ('Etudes du développement', 'Etudes du développement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Droit européen', 'Droit européen'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Sciences du langage', 'Sciences du langage'), ('Physique du vivant', 'Physique du vivant'), ('Economie internationale', 'Economie internationale'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences du médicament', 'Sciences du médicament'), ('Management et commerce international', 'Management et commerce interna'), ('Intelligence économique', 'Intelligence économique'), ('Lettres', 'Lettres'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Etudes culturelles', 'Etudes culturelles'), ('Arts', 'Arts'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Sciences sociales', 'Sciences sociales'), ('Histoire', 'Histoire'), ('Santé', 'Santé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Anthropologie', 'Anthropologie'), ("Droit de l'économie", "Droit de l'économie"), ('Droit international', 'Droit international'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Management sectoriel', 'Management sectoriel'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Droit des libertés', 'Droit des libertés'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Philosophie', 'Philosophie'), ('Communication, publicité', 'Communication, publicité'), ('Droit du patrimoine', 'Droit du patrimoine'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Droit privé', 'Droit privé'), ('Pharmacologie', 'Pharmacologie'), ('Psychologie', 'Psychologie'), ('Lettres, langues', 'Lettres, langues'), ('Biotechnologies', 'Biotechnologies'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Théologie protestante', 'Théologie protestante'), ('Economie du développement', 'Economie du développement'), ('Droit constitutionnel', 'Droit constitutionnel'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Démographie', 'Démographie'), ('Logique', 'Logique'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Neurosciences', 'Neurosciences'), ('Sciences de la vie', 'Sciences de la vie'), ('Théâtre', 'Théâtre'), ('Automatique, robotique', 'Automatique, robotique'), ('Journalisme', 'Journalisme'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Humanités numériques', 'Humanités numériques'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Droit de la santé', 'Droit de la santé'), ('Information, communication', 'Information, communication'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Esthétique', 'Esthétique'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Droit comparé', 'Droit comparé'), ('Gestion', 'Gestion'), ('Administration économique et sociale', 'Administration économique et s'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Economie du droit', 'Economie du droit'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Communication des organisations', 'Communication des organisation'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Tourisme', 'Tourisme'), ('Finances publiques', 'Finances publiques'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Biologie', 'Biologie'), ('Danse', 'Danse'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Information-communication', 'Information-communication'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Design', 'Design'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Mécanique', 'Mécanique'), ('Ergonomie', 'Ergonomie'), ('Economie et management publics', 'Economie et management publics'), ('Biologie végétale', 'Biologie végétale'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Physique, chimie', 'Physique, chimie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Création artistique', 'Création artistique'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Création littéraire', 'Création littéraire'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Droit des assurances', 'Droit des assurances'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Droit civil', 'Droit civil'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Management', 'Management'), ("Histoire de l'art", "Histoire de l'art"), ('Sciences cognitives', 'Sciences cognitives'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ("Sciences de l'eau", "Sciences de l'eau"), ('Industries culturelles', 'Industries culturelles'), ('Lettres et humanités', 'Lettres et humanités'), ('Santé publique', 'Santé publique'), ('Français langue étrangère', 'Français langue étrangère'), ('Economie', 'Economie'), ('Mondes anciens', 'Mondes anciens'), ('Microbiologie', 'Microbiologie'), ('Didactique des sciences', 'Didactique des sciences'), ('Droit administratif', 'Droit administratif'), ('Communication publique et politique', 'Communication publique et poli'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Management et administration des entreprises', 'Management et administration d'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Management public', 'Management public'), ('Bio-géosciences', 'Bio-géosciences'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Biologie du développement', 'Biologie du développement'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Psychanalyse', 'Psychanalyse'), ('Génie mécanique', 'Génie mécanique'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Sciences de la mer', 'Sciences de la mer'), ('Mondes modernes', 'Mondes modernes'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Théologie', 'Théologie'), ('Politiques comparées', 'Politiques comparées'), ('Langues et sociétés', 'Langues et sociétés'), ('Génétique', 'Génétique'), ('Droit', 'Droit'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Droit public des affaires', 'Droit public des affaires'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Science politique', 'Science politique'), ('Sciences du vivant', 'Sciences du vivant'), ('Chimie', 'Chimie'), ('Géopolitique', 'Géopolitique'), ('Economie des organisations', 'Economie des organisations'), ('Droit notarial', 'Droit notarial'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Ethologie', 'Ethologie'), ('Droit public', 'Droit public'), ('Mathématiques', 'Mathématiques'), ('Géographie', 'Géographie'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Didactique des langues', 'Didactique des langues'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Mode', 'Mode'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Immunologie', 'Immunologie'), ('Information, documentation', 'Information, documentation'), ('Economie de la santé', 'Economie de la santé'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Arts du spectacle', 'Arts du spectacle'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Sciences et technologies', 'Sciences et technologies'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Risques et environnement', 'Risques et environnement'), ('Droit des affaires', 'Droit des affaires'), ('Création numérique', 'Création numérique'), ('Humanités', 'Humanités'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Biomécanique', 'Biomécanique'), ('Energie', 'Energie'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Physique', 'Physique'), ('Sociologie', 'Sociologie'), ('Administration publique', 'Administration publique'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Théologie catholique', 'Théologie catholique'), ('Arts plastiques', 'Arts plastiques'), ('Relations internationales', 'Relations internationales'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Musicologie', 'Musicologie'), ('Biologie-santé', 'Biologie-santé'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Gestion de patrimoine', 'Gestion de patrimoine'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Droit fiscal', 'Droit fiscal'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ("Management de l'innovation", "Management de l'innovation"), ('Marketing, vente', 'Marketing, vente'), ('Géomatique', 'Géomatique'), ('Informatique', 'Informatique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ('Mathématiques et applications', 'Mathématiques et applications'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Droit du numérique', 'Droit du numérique'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Economie et gestion', 'Economie et gestion'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Actuariat', 'Actuariat'), ('Bio-informatique', 'Bio-informatique'), ('Economie appliquée', 'Economie appliquée'), ('Management stratégique', 'Management stratégique'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Génie industriel', 'Génie industriel'), ('Acoustique', 'Acoustique'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Mondes contemporains', 'Mondes contemporains'), ('Génie civil', 'Génie civil'), ('Ethique', 'Ethique'), ('Archives', 'Archives')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Droit social', 'Droit social'), ('Finance', 'Finance'), ('Sciences de la matière', 'Sciences de la matière'), ('Politiques publiques', 'Politiques publiques'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Ethnologie', 'Ethnologie'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Patrimoine et musées', 'Patrimoine et musées'), ('Energétique, thermique', 'Energétique, thermique'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Culture et communication', 'Culture et communication'), ('Etudes du développement', 'Etudes du développement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Droit européen', 'Droit européen'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Sciences du langage', 'Sciences du langage'), ('Physique du vivant', 'Physique du vivant'), ('Economie internationale', 'Economie internationale'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences du médicament', 'Sciences du médicament'), ('Management et commerce international', 'Management et commerce interna'), ('Intelligence économique', 'Intelligence économique'), ('Lettres', 'Lettres'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Etudes culturelles', 'Etudes culturelles'), ('Arts', 'Arts'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Sciences sociales', 'Sciences sociales'), ('Histoire', 'Histoire'), ('Santé', 'Santé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Anthropologie', 'Anthropologie'), ("Droit de l'économie", "Droit de l'économie"), ('Droit international', 'Droit international'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Management sectoriel', 'Management sectoriel'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Droit des libertés', 'Droit des libertés'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Philosophie', 'Philosophie'), ('Communication, publicité', 'Communication, publicité'), ('Droit du patrimoine', 'Droit du patrimoine'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Droit privé', 'Droit privé'), ('Pharmacologie', 'Pharmacologie'), ('Psychologie', 'Psychologie'), ('Lettres, langues', 'Lettres, langues'), ('Biotechnologies', 'Biotechnologies'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Théologie protestante', 'Théologie protestante'), ('Economie du développement', 'Economie du développement'), ('Droit constitutionnel', 'Droit constitutionnel'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Démographie', 'Démographie'), ('Logique', 'Logique'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Neurosciences', 'Neurosciences'), ('Sciences de la vie', 'Sciences de la vie'), ('Théâtre', 'Théâtre'), ('Automatique, robotique', 'Automatique, robotique'), ('Journalisme', 'Journalisme'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Humanités numériques', 'Humanités numériques'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Droit de la santé', 'Droit de la santé'), ('Information, communication', 'Information, communication'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Esthétique', 'Esthétique'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Droit comparé', 'Droit comparé'), ('Gestion', 'Gestion'), ('Administration économique et sociale', 'Administration économique et s'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Economie du droit', 'Economie du droit'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Communication des organisations', 'Communication des organisation'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Tourisme', 'Tourisme'), ('Finances publiques', 'Finances publiques'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Biologie', 'Biologie'), ('Danse', 'Danse'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Information-communication', 'Information-communication'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Design', 'Design'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Mécanique', 'Mécanique'), ('Ergonomie', 'Ergonomie'), ('Economie et management publics', 'Economie et management publics'), ('Biologie végétale', 'Biologie végétale'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Physique, chimie', 'Physique, chimie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Création artistique', 'Création artistique'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Création littéraire', 'Création littéraire'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Droit des assurances', 'Droit des assurances'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Droit civil', 'Droit civil'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Management', 'Management'), ("Histoire de l'art", "Histoire de l'art"), ('Sciences cognitives', 'Sciences cognitives'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ("Sciences de l'eau", "Sciences de l'eau"), ('Industries culturelles', 'Industries culturelles'), ('Lettres et humanités', 'Lettres et humanités'), ('Santé publique', 'Santé publique'), ('Français langue étrangère', 'Français langue étrangère'), ('Economie', 'Economie'), ('Mondes anciens', 'Mondes anciens'), ('Microbiologie', 'Microbiologie'), ('Didactique des sciences', 'Didactique des sciences'), ('Droit administratif', 'Droit administratif'), ('Communication publique et politique', 'Communication publique et poli'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Management et administration des entreprises', 'Management et administration d'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Management public', 'Management public'), ('Bio-géosciences', 'Bio-géosciences'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Biologie du développement', 'Biologie du développement'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Psychanalyse', 'Psychanalyse'), ('Génie mécanique', 'Génie mécanique'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Sciences de la mer', 'Sciences de la mer'), ('Mondes modernes', 'Mondes modernes'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Théologie', 'Théologie'), ('Politiques comparées', 'Politiques comparées'), ('Langues et sociétés', 'Langues et sociétés'), ('Génétique', 'Génétique'), ('Droit', 'Droit'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Droit public des affaires', 'Droit public des affaires'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Science politique', 'Science politique'), ('Sciences du vivant', 'Sciences du vivant'), ('Chimie', 'Chimie'), ('Géopolitique', 'Géopolitique'), ('Economie des organisations', 'Economie des organisations'), ('Droit notarial', 'Droit notarial'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Ethologie', 'Ethologie'), ('Droit public', 'Droit public'), ('Mathématiques', 'Mathématiques'), ('Géographie', 'Géographie'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Didactique des langues', 'Didactique des langues'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Mode', 'Mode'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Immunologie', 'Immunologie'), ('Information, documentation', 'Information, documentation'), ('Economie de la santé', 'Economie de la santé'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Arts du spectacle', 'Arts du spectacle'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Sciences et technologies', 'Sciences et technologies'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Risques et environnement', 'Risques et environnement'), ('Droit des affaires', 'Droit des affaires'), ('Création numérique', 'Création numérique'), ('Humanités', 'Humanités'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Biomécanique', 'Biomécanique'), ('Energie', 'Energie'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Physique', 'Physique'), ('Sociologie', 'Sociologie'), ('Administration publique', 'Administration publique'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Théologie catholique', 'Théologie catholique'), ('Arts plastiques', 'Arts plastiques'), ('Relations internationales', 'Relations internationales'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Musicologie', 'Musicologie'), ('Biologie-santé', 'Biologie-santé'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Gestion de patrimoine', 'Gestion de patrimoine'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Droit fiscal', 'Droit fiscal'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ("Management de l'innovation", "Management de l'innovation"), ('Marketing, vente', 'Marketing, vente'), ('Géomatique', 'Géomatique'), ('Informatique', 'Informatique'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Intervention et développement social', 'Intervention et développement '), ('Mathématiques et applications', 'Mathématiques et applications'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Droit du numérique', 'Droit du numérique'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Economie et gestion', 'Economie et gestion'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Actuariat', 'Actuariat'), ('Bio-informatique', 'Bio-informatique'), ('Economie appliquée', 'Economie appliquée'), ('Management stratégique', 'Management stratégique'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Génie industriel', 'Génie industriel'), ('Acoustique', 'Acoustique'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Mondes contemporains', 'Mondes contemporains'), ('Génie civil', 'Génie civil'), ('Ethique', 'Ethique'), ('Archives', 'Archives')], max_length=271, null=True),
        ),
    ]