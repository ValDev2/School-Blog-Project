# Generated by Django 2.2.5 on 2019-09-21 08:43

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20190920_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Information, communication', 'Information, communication'), ('Musicologie', 'Musicologie'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Physique du vivant', 'Physique du vivant'), ('Mathématiques', 'Mathématiques'), ('Santé publique', 'Santé publique'), ('Actuariat', 'Actuariat'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Ethologie', 'Ethologie'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Gestion', 'Gestion'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Géographie', 'Géographie'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Droit', 'Droit'), ('Psychologie', 'Psychologie'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Ethique', 'Ethique'), ('Droit comparé', 'Droit comparé'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Ergonomie', 'Ergonomie'), ('Sciences de la vie', 'Sciences de la vie'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Tourisme', 'Tourisme'), ('Théâtre', 'Théâtre'), ('Physique', 'Physique'), ('Administration publique', 'Administration publique'), ('Création littéraire', 'Création littéraire'), ('Lettres', 'Lettres'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Sciences de la matière', 'Sciences de la matière'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Droit européen', 'Droit européen'), ('Communication des organisations', 'Communication des organisation'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Administration économique et sociale', 'Administration économique et s'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Mathématiques et applications', 'Mathématiques et applications'), ('Droit administratif', 'Droit administratif'), ("Sciences de l'eau", "Sciences de l'eau"), ('Administration et échanges internationaux', 'Administration et échanges int'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Théologie', 'Théologie'), ('Création numérique', 'Création numérique'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Droit notarial', 'Droit notarial'), ('Santé', 'Santé'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Arts du spectacle', 'Arts du spectacle'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Automatique, robotique', 'Automatique, robotique'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Droit privé', 'Droit privé'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Etudes du développement', 'Etudes du développement'), ('Information-communication', 'Information-communication'), ('Management sectoriel', 'Management sectoriel'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Management et administration des entreprises', 'Management et administration d'), ("Droit de l'économie", "Droit de l'économie"), ('Pharmacologie', 'Pharmacologie'), ('Droit social', 'Droit social'), ('Management', 'Management'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Energétique, thermique', 'Energétique, thermique'), ('Economie du développement', 'Economie du développement'), ('Génétique', 'Génétique'), ('Logique', 'Logique'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Information, documentation', 'Information, documentation'), ('Anthropologie', 'Anthropologie'), ('Mode', 'Mode'), ('Génie mécanique', 'Génie mécanique'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Théologie protestante', 'Théologie protestante'), ('Droit international', 'Droit international'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Informatique', 'Informatique'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Histoire', 'Histoire'), ('Communication publique et politique', 'Communication publique et poli'), ('Arts', 'Arts'), ('Sciences du médicament', 'Sciences du médicament'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Science politique', 'Science politique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Démographie', 'Démographie'), ('Economie du droit', 'Economie du droit'), ('Humanités', 'Humanités'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Bio-informatique', 'Bio-informatique'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Economie et management publics', 'Economie et management publics'), ("Histoire de l'art", "Histoire de l'art"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Microbiologie', 'Microbiologie'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Psychanalyse', 'Psychanalyse'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Droit public', 'Droit public'), ('Industries culturelles', 'Industries culturelles'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Relations internationales', 'Relations internationales'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Théologie catholique', 'Théologie catholique'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Management stratégique', 'Management stratégique'), ('Philosophie', 'Philosophie'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Economie des organisations', 'Economie des organisations'), ('STAPS : management du sport', 'STAPS : management du sport'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Didactique des langues', 'Didactique des langues'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Design', 'Design'), ('Création artistique', 'Création artistique'), ("Management de l'innovation", "Management de l'innovation"), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Economie appliquée', 'Economie appliquée'), ('Economie de la santé', 'Economie de la santé'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Géomatique', 'Géomatique'), ('Droit fiscal', 'Droit fiscal'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Arts plastiques', 'Arts plastiques'), ('Français langue étrangère', 'Français langue étrangère'), ('Intelligence économique', 'Intelligence économique'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Sciences sociales', 'Sciences sociales'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Chimie', 'Chimie'), ('Droit des affaires', 'Droit des affaires'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Biologie', 'Biologie'), ('Mécanique', 'Mécanique'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Esthétique', 'Esthétique'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Géographie et aménagement', 'Géographie et aménagement'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Chimie moléculaire', 'Chimie moléculaire'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Management et commerce international', 'Management et commerce interna'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Biomécanique', 'Biomécanique'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Géopolitique', 'Géopolitique'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Sciences du langage', 'Sciences du langage'), ('Humanités numériques', 'Humanités numériques'), ('Acoustique', 'Acoustique'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Management public', 'Management public'), ('Culture et communication', 'Culture et communication'), ('Droit civil', 'Droit civil'), ('Droit des libertés', 'Droit des libertés'), ('Energie', 'Energie'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Politiques comparées', 'Politiques comparées'), ('Biologie végétale', 'Biologie végétale'), ('Droit de la santé', 'Droit de la santé'), ('Droit des assurances', 'Droit des assurances'), ('Droit du numérique', 'Droit du numérique'), ('Economie', 'Economie'), ('Archives', 'Archives'), ('Sciences du vivant', 'Sciences du vivant'), ('Immunologie', 'Immunologie'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Ethnologie', 'Ethnologie'), ('Mondes contemporains', 'Mondes contemporains'), ('Risques et environnement', 'Risques et environnement'), ('Lettres et humanités', 'Lettres et humanités'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Mondes anciens', 'Mondes anciens'), ('Neurosciences', 'Neurosciences'), ('Sciences cognitives', 'Sciences cognitives'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Biotechnologies', 'Biotechnologies'), ('Economie internationale', 'Economie internationale'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Economie et gestion', 'Economie et gestion'), ('Sociologie', 'Sociologie'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Finance', 'Finance'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Marketing, vente', 'Marketing, vente'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Finances publiques', 'Finances publiques'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Communication, publicité', 'Communication, publicité'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Droit public des affaires', 'Droit public des affaires'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Physique, chimie', 'Physique, chimie'), ('Bio-géosciences', 'Bio-géosciences'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Lettres, langues', 'Lettres, langues'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Traitement du signal et des images', 'Traitement du signal et des im'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Biologie du développement', 'Biologie du développement'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Danse', 'Danse'), ('Politiques publiques', 'Politiques publiques'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Sciences de la mer', 'Sciences de la mer'), ('Génie industriel', 'Génie industriel'), ('Intervention et développement social', 'Intervention et développement '), ('Journalisme', 'Journalisme'), ('Biologie-santé', 'Biologie-santé'), ('Langues et sociétés', 'Langues et sociétés'), ('Mondes modernes', 'Mondes modernes'), ('Etudes culturelles', 'Etudes culturelles'), ('Génie civil', 'Génie civil'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Sciences et technologies', 'Sciences et technologies'), ('Didactique des sciences', 'Didactique des sciences')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Information, communication', 'Information, communication'), ('Musicologie', 'Musicologie'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Physique du vivant', 'Physique du vivant'), ('Mathématiques', 'Mathématiques'), ('Santé publique', 'Santé publique'), ('Actuariat', 'Actuariat'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Ethologie', 'Ethologie'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Gestion', 'Gestion'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Géographie', 'Géographie'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Droit', 'Droit'), ('Psychologie', 'Psychologie'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Ethique', 'Ethique'), ('Droit comparé', 'Droit comparé'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Ergonomie', 'Ergonomie'), ('Sciences de la vie', 'Sciences de la vie'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Tourisme', 'Tourisme'), ('Théâtre', 'Théâtre'), ('Physique', 'Physique'), ('Administration publique', 'Administration publique'), ('Création littéraire', 'Création littéraire'), ('Lettres', 'Lettres'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Sciences de la matière', 'Sciences de la matière'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Droit européen', 'Droit européen'), ('Communication des organisations', 'Communication des organisation'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Administration économique et sociale', 'Administration économique et s'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Mathématiques et applications', 'Mathématiques et applications'), ('Droit administratif', 'Droit administratif'), ("Sciences de l'eau", "Sciences de l'eau"), ('Administration et échanges internationaux', 'Administration et échanges int'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Théologie', 'Théologie'), ('Création numérique', 'Création numérique'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Droit notarial', 'Droit notarial'), ('Santé', 'Santé'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Arts du spectacle', 'Arts du spectacle'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Automatique, robotique', 'Automatique, robotique'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Droit privé', 'Droit privé'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Etudes du développement', 'Etudes du développement'), ('Information-communication', 'Information-communication'), ('Management sectoriel', 'Management sectoriel'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Management et administration des entreprises', 'Management et administration d'), ("Droit de l'économie", "Droit de l'économie"), ('Pharmacologie', 'Pharmacologie'), ('Droit social', 'Droit social'), ('Management', 'Management'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Energétique, thermique', 'Energétique, thermique'), ('Economie du développement', 'Economie du développement'), ('Génétique', 'Génétique'), ('Logique', 'Logique'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Information, documentation', 'Information, documentation'), ('Anthropologie', 'Anthropologie'), ('Mode', 'Mode'), ('Génie mécanique', 'Génie mécanique'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Théologie protestante', 'Théologie protestante'), ('Droit international', 'Droit international'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Informatique', 'Informatique'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Histoire', 'Histoire'), ('Communication publique et politique', 'Communication publique et poli'), ('Arts', 'Arts'), ('Sciences du médicament', 'Sciences du médicament'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Science politique', 'Science politique'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Démographie', 'Démographie'), ('Economie du droit', 'Economie du droit'), ('Humanités', 'Humanités'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Bio-informatique', 'Bio-informatique'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Economie et management publics', 'Economie et management publics'), ("Histoire de l'art", "Histoire de l'art"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Microbiologie', 'Microbiologie'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Traduction et interprétation', 'Traduction et interprétation'), ('Psychanalyse', 'Psychanalyse'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Droit public', 'Droit public'), ('Industries culturelles', 'Industries culturelles'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Relations internationales', 'Relations internationales'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Théologie catholique', 'Théologie catholique'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Management stratégique', 'Management stratégique'), ('Philosophie', 'Philosophie'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Economie des organisations', 'Economie des organisations'), ('STAPS : management du sport', 'STAPS : management du sport'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Didactique des langues', 'Didactique des langues'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Design', 'Design'), ('Création artistique', 'Création artistique'), ("Management de l'innovation", "Management de l'innovation"), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Economie appliquée', 'Economie appliquée'), ('Economie de la santé', 'Economie de la santé'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Géomatique', 'Géomatique'), ('Droit fiscal', 'Droit fiscal'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Arts plastiques', 'Arts plastiques'), ('Français langue étrangère', 'Français langue étrangère'), ('Intelligence économique', 'Intelligence économique'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Sciences sociales', 'Sciences sociales'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Chimie', 'Chimie'), ('Droit des affaires', 'Droit des affaires'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Biologie', 'Biologie'), ('Mécanique', 'Mécanique'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Esthétique', 'Esthétique'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Géographie et aménagement', 'Géographie et aménagement'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Chimie moléculaire', 'Chimie moléculaire'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Management et commerce international', 'Management et commerce interna'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Biomécanique', 'Biomécanique'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Géopolitique', 'Géopolitique'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Sciences du langage', 'Sciences du langage'), ('Humanités numériques', 'Humanités numériques'), ('Acoustique', 'Acoustique'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Management public', 'Management public'), ('Culture et communication', 'Culture et communication'), ('Droit civil', 'Droit civil'), ('Droit des libertés', 'Droit des libertés'), ('Energie', 'Energie'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Politiques comparées', 'Politiques comparées'), ('Biologie végétale', 'Biologie végétale'), ('Droit de la santé', 'Droit de la santé'), ('Droit des assurances', 'Droit des assurances'), ('Droit du numérique', 'Droit du numérique'), ('Economie', 'Economie'), ('Archives', 'Archives'), ('Sciences du vivant', 'Sciences du vivant'), ('Immunologie', 'Immunologie'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Ethnologie', 'Ethnologie'), ('Mondes contemporains', 'Mondes contemporains'), ('Risques et environnement', 'Risques et environnement'), ('Lettres et humanités', 'Lettres et humanités'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Mondes anciens', 'Mondes anciens'), ('Neurosciences', 'Neurosciences'), ('Sciences cognitives', 'Sciences cognitives'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Biotechnologies', 'Biotechnologies'), ('Economie internationale', 'Economie internationale'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Economie et gestion', 'Economie et gestion'), ('Sociologie', 'Sociologie'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Finance', 'Finance'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Marketing, vente', 'Marketing, vente'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Finances publiques', 'Finances publiques'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Communication, publicité', 'Communication, publicité'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Droit public des affaires', 'Droit public des affaires'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Physique, chimie', 'Physique, chimie'), ('Bio-géosciences', 'Bio-géosciences'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Lettres, langues', 'Lettres, langues'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Analyse et politique économique', 'Analyse et politique économiqu'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Traitement du signal et des images', 'Traitement du signal et des im'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Biologie du développement', 'Biologie du développement'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Danse', 'Danse'), ('Politiques publiques', 'Politiques publiques'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Sciences de la mer', 'Sciences de la mer'), ('Génie industriel', 'Génie industriel'), ('Intervention et développement social', 'Intervention et développement '), ('Journalisme', 'Journalisme'), ('Biologie-santé', 'Biologie-santé'), ('Langues et sociétés', 'Langues et sociétés'), ('Mondes modernes', 'Mondes modernes'), ('Etudes culturelles', 'Etudes culturelles'), ('Génie civil', 'Génie civil'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Sciences et technologies', 'Sciences et technologies'), ('Didactique des sciences', 'Didactique des sciences')], max_length=271, null=True),
        ),
    ]