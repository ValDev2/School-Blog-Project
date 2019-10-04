# Generated by Django 2.2.5 on 2019-10-04 20:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20191004_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Géopolitique', 'Géopolitique'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Management des PME-PMI', 'Management des PME-PMI'), ('Economie des organisations', 'Economie des organisations'), ('Langues et sociétés', 'Langues et sociétés'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Mondes anciens', 'Mondes anciens'), ('Logique', 'Logique'), ('Physique, chimie', 'Physique, chimie'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Psychologie', 'Psychologie'), ('Droit public des affaires', 'Droit public des affaires'), ('Sciences de la vie', 'Sciences de la vie'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Communication, publicité', 'Communication, publicité'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Génie mécanique', 'Génie mécanique'), ('Management stratégique', 'Management stratégique'), ('Droit administratif', 'Droit administratif'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Santé', 'Santé'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Communication des organisations', 'Communication des organisation'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Droit des assurances', 'Droit des assurances'), ('Droit public', 'Droit public'), ('Biologie', 'Biologie'), ('Droit social', 'Droit social'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Intervention et développement social', 'Intervention et développement '), ('Démographie', 'Démographie'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Droit du numérique', 'Droit du numérique'), ('Droit européen', 'Droit européen'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Economie appliquée', 'Economie appliquée'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Communication publique et politique', 'Communication publique et poli'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Didactique des langues', 'Didactique des langues'), ("Sciences de l'eau", "Sciences de l'eau"), ('Droit civil', 'Droit civil'), ('Management sectoriel', 'Management sectoriel'), ('Ergonomie', 'Ergonomie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Théâtre', 'Théâtre'), ('Politiques comparées', 'Politiques comparées'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Economie et management publics', 'Economie et management publics'), ('Droit des libertés', 'Droit des libertés'), ('Biologie du développement', 'Biologie du développement'), ('Administration publique', 'Administration publique'), ('Management et administration des entreprises', 'Management et administration d'), ('Marketing, vente', 'Marketing, vente'), ('Archives', 'Archives'), ('Sciences du langage', 'Sciences du langage'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Mécanique', 'Mécanique'), ('Création littéraire', 'Création littéraire'), ('Finances publiques', 'Finances publiques'), ('Géomatique', 'Géomatique'), ('Humanités numériques', 'Humanités numériques'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Biologie végétale', 'Biologie végétale'), ('Economie du droit', 'Economie du droit'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Sciences de la mer', 'Sciences de la mer'), ('Biomécanique', 'Biomécanique'), ('Tourisme', 'Tourisme'), ('Information, documentation', 'Information, documentation'), ('Design', 'Design'), ('Industries culturelles', 'Industries culturelles'), ('Génie industriel', 'Génie industriel'), ('Acoustique', 'Acoustique'), ('Automatique, robotique', 'Automatique, robotique'), ('Journalisme', 'Journalisme'), ('Mondes contemporains', 'Mondes contemporains'), ('Santé publique', 'Santé publique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie', 'Chimie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Droit comparé', 'Droit comparé'), ('Lettres', 'Lettres'), ('Economie et gestion', 'Economie et gestion'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Politiques publiques', 'Politiques publiques'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Droit fiscal', 'Droit fiscal'), ('Arts', 'Arts'), ('Ethique', 'Ethique'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Information-communication', 'Information-communication'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Lettres, langues', 'Lettres, langues'), ('Mondes médiévaux', 'Mondes médiévaux'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Sciences et technologies', 'Sciences et technologies'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Actuariat', 'Actuariat'), ('Neurosciences', 'Neurosciences'), ('Mode', 'Mode'), ('Intelligence économique', 'Intelligence économique'), ('Bio-informatique', 'Bio-informatique'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Arts du spectacle', 'Arts du spectacle'), ('Droit des affaires', 'Droit des affaires'), ('Droit', 'Droit'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Mondes modernes', 'Mondes modernes'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Biotechnologies', 'Biotechnologies'), ('Energie', 'Energie'), ('Science politique', 'Science politique'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Culture et communication', 'Culture et communication'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Economie', 'Economie'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Philosophie', 'Philosophie'), ('Psychanalyse', 'Psychanalyse'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Economie de la santé', 'Economie de la santé'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Droit de la santé', 'Droit de la santé'), ('Ethologie', 'Ethologie'), ('Economie internationale', 'Economie internationale'), ('Arts plastiques', 'Arts plastiques'), ('Sociologie', 'Sociologie'), ('Ethnologie', 'Ethnologie'), ('Sciences cognitives', 'Sciences cognitives'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Théologie catholique', 'Théologie catholique'), ('Création artistique', 'Création artistique'), ('Risques et environnement', 'Risques et environnement'), ("Histoire de l'art", "Histoire de l'art"), ('Anthropologie', 'Anthropologie'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Etudes culturelles', 'Etudes culturelles'), ('Sciences du médicament', 'Sciences du médicament'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Management et commerce international', 'Management et commerce interna'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Droit privé', 'Droit privé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Danse', 'Danse'), ('Génétique', 'Génétique'), ('Génie civil', 'Génie civil'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Immunologie', 'Immunologie'), ('Microbiologie', 'Microbiologie'), ('Bio-géosciences', 'Bio-géosciences'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Esthétique', 'Esthétique'), ('Lettres et humanités', 'Lettres et humanités'), ('Finance', 'Finance'), ('Sciences de la matière', 'Sciences de la matière'), ('Création numérique', 'Création numérique'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Physique du vivant', 'Physique du vivant'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ("Droit de l'économie", "Droit de l'économie"), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit international', 'Droit international'), ('Management', 'Management'), ('Didactique des sciences', 'Didactique des sciences'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Sciences sociales', 'Sciences sociales'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Relations internationales', 'Relations internationales'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Physique', 'Physique'), ('Musicologie', 'Musicologie'), ('Français langue étrangère', 'Français langue étrangère'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Géographie', 'Géographie'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Théologie protestante', 'Théologie protestante'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Management public', 'Management public'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Economie du développement', 'Economie du développement'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Administration économique et sociale', 'Administration économique et s'), ('Etudes du développement', 'Etudes du développement'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Histoire', 'Histoire'), ('Humanités', 'Humanités'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Droit notarial', 'Droit notarial'), ('Gestion', 'Gestion'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Informatique', 'Informatique'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Théologie', 'Théologie'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Energétique, thermique', 'Energétique, thermique'), ("Management de l'innovation", "Management de l'innovation"), ('Biologie-santé', 'Biologie-santé'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Mathématiques', 'Mathématiques'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Sciences du vivant', 'Sciences du vivant'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Information, communication', 'Information, communication'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Pharmacologie', 'Pharmacologie'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur")], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Géopolitique', 'Géopolitique'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Management des PME-PMI', 'Management des PME-PMI'), ('Economie des organisations', 'Economie des organisations'), ('Langues et sociétés', 'Langues et sociétés'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Mondes anciens', 'Mondes anciens'), ('Logique', 'Logique'), ('Physique, chimie', 'Physique, chimie'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Psychologie', 'Psychologie'), ('Droit public des affaires', 'Droit public des affaires'), ('Sciences de la vie', 'Sciences de la vie'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Communication, publicité', 'Communication, publicité'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Génie mécanique', 'Génie mécanique'), ('Management stratégique', 'Management stratégique'), ('Droit administratif', 'Droit administratif'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Santé', 'Santé'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Communication des organisations', 'Communication des organisation'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Droit des assurances', 'Droit des assurances'), ('Droit public', 'Droit public'), ('Biologie', 'Biologie'), ('Droit social', 'Droit social'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Intervention et développement social', 'Intervention et développement '), ('Démographie', 'Démographie'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Droit du numérique', 'Droit du numérique'), ('Droit européen', 'Droit européen'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Economie appliquée', 'Economie appliquée'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Communication publique et politique', 'Communication publique et poli'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Didactique des langues', 'Didactique des langues'), ("Sciences de l'eau", "Sciences de l'eau"), ('Droit civil', 'Droit civil'), ('Management sectoriel', 'Management sectoriel'), ('Ergonomie', 'Ergonomie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Théâtre', 'Théâtre'), ('Politiques comparées', 'Politiques comparées'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Economie et management publics', 'Economie et management publics'), ('Droit des libertés', 'Droit des libertés'), ('Biologie du développement', 'Biologie du développement'), ('Administration publique', 'Administration publique'), ('Management et administration des entreprises', 'Management et administration d'), ('Marketing, vente', 'Marketing, vente'), ('Archives', 'Archives'), ('Sciences du langage', 'Sciences du langage'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Mécanique', 'Mécanique'), ('Création littéraire', 'Création littéraire'), ('Finances publiques', 'Finances publiques'), ('Géomatique', 'Géomatique'), ('Humanités numériques', 'Humanités numériques'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Biologie végétale', 'Biologie végétale'), ('Economie du droit', 'Economie du droit'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Sciences de la mer', 'Sciences de la mer'), ('Biomécanique', 'Biomécanique'), ('Tourisme', 'Tourisme'), ('Information, documentation', 'Information, documentation'), ('Design', 'Design'), ('Industries culturelles', 'Industries culturelles'), ('Génie industriel', 'Génie industriel'), ('Acoustique', 'Acoustique'), ('Automatique, robotique', 'Automatique, robotique'), ('Journalisme', 'Journalisme'), ('Mondes contemporains', 'Mondes contemporains'), ('Santé publique', 'Santé publique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie', 'Chimie'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Droit comparé', 'Droit comparé'), ('Lettres', 'Lettres'), ('Economie et gestion', 'Economie et gestion'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Politiques publiques', 'Politiques publiques'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Droit fiscal', 'Droit fiscal'), ('Arts', 'Arts'), ('Ethique', 'Ethique'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Information-communication', 'Information-communication'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Lettres, langues', 'Lettres, langues'), ('Mondes médiévaux', 'Mondes médiévaux'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Sciences et technologies', 'Sciences et technologies'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Actuariat', 'Actuariat'), ('Neurosciences', 'Neurosciences'), ('Mode', 'Mode'), ('Intelligence économique', 'Intelligence économique'), ('Bio-informatique', 'Bio-informatique'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Arts du spectacle', 'Arts du spectacle'), ('Droit des affaires', 'Droit des affaires'), ('Droit', 'Droit'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Mondes modernes', 'Mondes modernes'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Biotechnologies', 'Biotechnologies'), ('Energie', 'Energie'), ('Science politique', 'Science politique'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Culture et communication', 'Culture et communication'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Economie', 'Economie'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Philosophie', 'Philosophie'), ('Psychanalyse', 'Psychanalyse'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Economie de la santé', 'Economie de la santé'), ('Chimie moléculaire', 'Chimie moléculaire'), ('Droit de la santé', 'Droit de la santé'), ('Ethologie', 'Ethologie'), ('Economie internationale', 'Economie internationale'), ('Arts plastiques', 'Arts plastiques'), ('Sociologie', 'Sociologie'), ('Ethnologie', 'Ethnologie'), ('Sciences cognitives', 'Sciences cognitives'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Théologie catholique', 'Théologie catholique'), ('Création artistique', 'Création artistique'), ('Risques et environnement', 'Risques et environnement'), ("Histoire de l'art", "Histoire de l'art"), ('Anthropologie', 'Anthropologie'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Etudes culturelles', 'Etudes culturelles'), ('Sciences du médicament', 'Sciences du médicament'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Management et commerce international', 'Management et commerce interna'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Droit privé', 'Droit privé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Danse', 'Danse'), ('Génétique', 'Génétique'), ('Génie civil', 'Génie civil'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Immunologie', 'Immunologie'), ('Microbiologie', 'Microbiologie'), ('Bio-géosciences', 'Bio-géosciences'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Esthétique', 'Esthétique'), ('Lettres et humanités', 'Lettres et humanités'), ('Finance', 'Finance'), ('Sciences de la matière', 'Sciences de la matière'), ('Création numérique', 'Création numérique'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Physique du vivant', 'Physique du vivant'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ("Droit de l'économie", "Droit de l'économie"), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit international', 'Droit international'), ('Management', 'Management'), ('Didactique des sciences', 'Didactique des sciences'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Sciences sociales', 'Sciences sociales'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Relations internationales', 'Relations internationales'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Physique', 'Physique'), ('Musicologie', 'Musicologie'), ('Français langue étrangère', 'Français langue étrangère'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Géographie', 'Géographie'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Théologie protestante', 'Théologie protestante'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Management public', 'Management public'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Economie du développement', 'Economie du développement'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Administration économique et sociale', 'Administration économique et s'), ('Etudes du développement', 'Etudes du développement'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Histoire', 'Histoire'), ('Humanités', 'Humanités'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Droit notarial', 'Droit notarial'), ('Gestion', 'Gestion'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Informatique', 'Informatique'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Théologie', 'Théologie'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Energétique, thermique', 'Energétique, thermique'), ("Management de l'innovation", "Management de l'innovation"), ('Biologie-santé', 'Biologie-santé'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Mathématiques', 'Mathématiques'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Sciences du vivant', 'Sciences du vivant'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Information, communication', 'Information, communication'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Pharmacologie', 'Pharmacologie'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur")], max_length=271, null=True),
        ),
    ]
