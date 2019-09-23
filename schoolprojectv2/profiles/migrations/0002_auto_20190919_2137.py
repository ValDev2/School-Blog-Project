# Generated by Django 2.2.5 on 2019-09-19 19:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ("Sciences de l'eau", "Sciences de l'eau"), ('Neurosciences', 'Neurosciences'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Sciences cognitives', 'Sciences cognitives'), ('Langues et sociétés', 'Langues et sociétés'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ("Droit de l'économie", "Droit de l'économie"), ('Droit comparé', 'Droit comparé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Management et commerce international', 'Management et commerce interna'), ('Management et administration des entreprises', 'Management et administration d'), ('Finance', 'Finance'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Droit public des affaires', 'Droit public des affaires'), ('Physique, chimie', 'Physique, chimie'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Economie', 'Economie'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Droit privé', 'Droit privé'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Lettres, langues', 'Lettres, langues'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ("Histoire de l'art", "Histoire de l'art"), ('Management stratégique', 'Management stratégique'), ('Politiques publiques', 'Politiques publiques'), ('Risques et environnement', 'Risques et environnement'), ('Droit fiscal', 'Droit fiscal'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Psychanalyse', 'Psychanalyse'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Gestion', 'Gestion'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Sciences et technologies', 'Sciences et technologies'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Lettres et humanités', 'Lettres et humanités'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Tourisme', 'Tourisme'), ('Design', 'Design'), ('Didactique des sciences', 'Didactique des sciences'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Chimie', 'Chimie'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Mondes modernes', 'Mondes modernes'), ('Etudes culturelles', 'Etudes culturelles'), ('Archives', 'Archives'), ('Intelligence économique', 'Intelligence économique'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Danse', 'Danse'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Création littéraire', 'Création littéraire'), ('Musicologie', 'Musicologie'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Energie', 'Energie'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Traduction et interprétation', 'Traduction et interprétation'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Arts du spectacle', 'Arts du spectacle'), ('Acoustique', 'Acoustique'), ('Lettres', 'Lettres'), ('Sciences de la mer', 'Sciences de la mer'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Logique', 'Logique'), ('Bio-géosciences', 'Bio-géosciences'), ('Histoire', 'Histoire'), ('Droit européen', 'Droit européen'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Théologie protestante', 'Théologie protestante'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('STAPS : management du sport', 'STAPS : management du sport'), ('Biotechnologies', 'Biotechnologies'), ('Culture et communication', 'Culture et communication'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Microbiologie', 'Microbiologie'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Biologie végétale', 'Biologie végétale'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Sciences de la vie', 'Sciences de la vie'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Economie du droit', 'Economie du droit'), ('Santé publique', 'Santé publique'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Philosophie', 'Philosophie'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Management sectoriel', 'Management sectoriel'), ('Actuariat', 'Actuariat'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Economie et gestion', 'Economie et gestion'), ('Economie et management publics', 'Economie et management publics'), ('Droit du numérique', 'Droit du numérique'), ('Relations internationales', 'Relations internationales'), ('Physique du vivant', 'Physique du vivant'), ('Ethologie', 'Ethologie'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Information-communication', 'Information-communication'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Arts plastiques', 'Arts plastiques'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Information, communication', 'Information, communication'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Droit social', 'Droit social'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Théologie catholique', 'Théologie catholique'), ('Energétique, thermique', 'Energétique, thermique'), ('Sociologie', 'Sociologie'), ('Physique', 'Physique'), ('Sciences de la matière', 'Sciences de la matière'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Ergonomie', 'Ergonomie'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Théâtre', 'Théâtre'), ('Biologie du développement', 'Biologie du développement'), ('Management public', 'Management public'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Arts', 'Arts'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Administration publique', 'Administration publique'), ('Economie des organisations', 'Economie des organisations'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Economie de la santé', 'Economie de la santé'), ('Biologie-santé', 'Biologie-santé'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Ethnologie', 'Ethnologie'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Information, documentation', 'Information, documentation'), ('Industries culturelles', 'Industries culturelles'), ('Communication des organisations', 'Communication des organisation'), ('Administration économique et sociale', 'Administration économique et s'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Droit des assurances', 'Droit des assurances'), ('Mécanique', 'Mécanique'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Etudes du développement', 'Etudes du développement'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Français langue étrangère', 'Français langue étrangère'), ('Informatique', 'Informatique'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Management', 'Management'), ('Géographie', 'Géographie'), ('Génie civil', 'Génie civil'), ('Economie internationale', 'Economie internationale'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Journalisme', 'Journalisme'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Sciences du médicament', 'Sciences du médicament'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Automatique, robotique', 'Automatique, robotique'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Démographie', 'Démographie'), ('Intervention et développement social', 'Intervention et développement '), ('Droit du patrimoine', 'Droit du patrimoine'), ("Management de l'innovation", "Management de l'innovation"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Economie appliquée', 'Economie appliquée'), ('Economie du développement', 'Economie du développement'), ('Pharmacologie', 'Pharmacologie'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Biologie', 'Biologie'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Droit de la santé', 'Droit de la santé'), ('Sciences du vivant', 'Sciences du vivant'), ('Droit des affaires', 'Droit des affaires'), ('Droit public', 'Droit public'), ('Génétique', 'Génétique'), ('Droit administratif', 'Droit administratif'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Génie mécanique', 'Génie mécanique'), ('Génie industriel', 'Génie industriel'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Communication, publicité', 'Communication, publicité'), ('Marketing, vente', 'Marketing, vente'), ('Création numérique', 'Création numérique'), ('Mondes anciens', 'Mondes anciens'), ('Science politique', 'Science politique'), ('Droit notarial', 'Droit notarial'), ('Mathématiques', 'Mathématiques'), ('Ethique', 'Ethique'), ('Théologie', 'Théologie'), ('Droit civil', 'Droit civil'), ('Biomécanique', 'Biomécanique'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Chimie moléculaire', 'Chimie moléculaire'), ('Finances publiques', 'Finances publiques'), ('Psychologie', 'Psychologie'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Anthropologie', 'Anthropologie'), ('Humanités numériques', 'Humanités numériques'), ('Droit des libertés', 'Droit des libertés'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences sociales', 'Sciences sociales'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Santé', 'Santé'), ('Immunologie', 'Immunologie'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Géomatique', 'Géomatique'), ('Bio-informatique', 'Bio-informatique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Esthétique', 'Esthétique'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Politiques comparées', 'Politiques comparées'), ('Droit', 'Droit'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Géopolitique', 'Géopolitique'), ('Didactique des langues', 'Didactique des langues'), ('Communication publique et politique', 'Communication publique et poli'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Droit international', 'Droit international'), ('Sciences du langage', 'Sciences du langage'), ('Humanités', 'Humanités'), ('Création artistique', 'Création artistique'), ('Mode', 'Mode'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Mondes contemporains', 'Mondes contemporains')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ("Sciences de l'eau", "Sciences de l'eau"), ('Neurosciences', 'Neurosciences'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Sciences cognitives', 'Sciences cognitives'), ('Langues et sociétés', 'Langues et sociétés'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ("Droit de l'économie", "Droit de l'économie"), ('Droit comparé', 'Droit comparé'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Management et commerce international', 'Management et commerce interna'), ('Management et administration des entreprises', 'Management et administration d'), ('Finance', 'Finance'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Droit public des affaires', 'Droit public des affaires'), ('Physique, chimie', 'Physique, chimie'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Economie', 'Economie'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Droit privé', 'Droit privé'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Lettres, langues', 'Lettres, langues'), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ("Histoire de l'art", "Histoire de l'art"), ('Management stratégique', 'Management stratégique'), ('Politiques publiques', 'Politiques publiques'), ('Risques et environnement', 'Risques et environnement'), ('Droit fiscal', 'Droit fiscal'), ('Littérature générale et comparée', 'Littérature générale et compar'), ('Psychanalyse', 'Psychanalyse'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Gestion', 'Gestion'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Sciences et technologies', 'Sciences et technologies'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ('Lettres et humanités', 'Lettres et humanités'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Tourisme', 'Tourisme'), ('Design', 'Design'), ('Didactique des sciences', 'Didactique des sciences'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Chimie', 'Chimie'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Mondes modernes', 'Mondes modernes'), ('Etudes culturelles', 'Etudes culturelles'), ('Archives', 'Archives'), ('Intelligence économique', 'Intelligence économique'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Danse', 'Danse'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Création littéraire', 'Création littéraire'), ('Musicologie', 'Musicologie'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Energie', 'Energie'), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Traduction et interprétation', 'Traduction et interprétation'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Arts du spectacle', 'Arts du spectacle'), ('Acoustique', 'Acoustique'), ('Lettres', 'Lettres'), ('Sciences de la mer', 'Sciences de la mer'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Logique', 'Logique'), ('Bio-géosciences', 'Bio-géosciences'), ('Histoire', 'Histoire'), ('Droit européen', 'Droit européen'), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Théologie protestante', 'Théologie protestante'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('STAPS : management du sport', 'STAPS : management du sport'), ('Biotechnologies', 'Biotechnologies'), ('Culture et communication', 'Culture et communication'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Microbiologie', 'Microbiologie'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Biologie végétale', 'Biologie végétale'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Sciences de la vie', 'Sciences de la vie'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Economie du droit', 'Economie du droit'), ('Santé publique', 'Santé publique'), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Philosophie', 'Philosophie'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Management sectoriel', 'Management sectoriel'), ('Actuariat', 'Actuariat'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Economie et gestion', 'Economie et gestion'), ('Economie et management publics', 'Economie et management publics'), ('Droit du numérique', 'Droit du numérique'), ('Relations internationales', 'Relations internationales'), ('Physique du vivant', 'Physique du vivant'), ('Ethologie', 'Ethologie'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Information-communication', 'Information-communication'), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Arts plastiques', 'Arts plastiques'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Information, communication', 'Information, communication'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Droit social', 'Droit social'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Théologie catholique', 'Théologie catholique'), ('Energétique, thermique', 'Energétique, thermique'), ('Sociologie', 'Sociologie'), ('Physique', 'Physique'), ('Sciences de la matière', 'Sciences de la matière'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Ergonomie', 'Ergonomie'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Théâtre', 'Théâtre'), ('Biologie du développement', 'Biologie du développement'), ('Management public', 'Management public'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Arts', 'Arts'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Sciences pour la santé', 'Sciences pour la santé'), ('Administration publique', 'Administration publique'), ('Economie des organisations', 'Economie des organisations'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ('Economie de la santé', 'Economie de la santé'), ('Biologie-santé', 'Biologie-santé'), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Ethnologie', 'Ethnologie'), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Information, documentation', 'Information, documentation'), ('Industries culturelles', 'Industries culturelles'), ('Communication des organisations', 'Communication des organisation'), ('Administration économique et sociale', 'Administration économique et s'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Droit des assurances', 'Droit des assurances'), ('Mécanique', 'Mécanique'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Etudes du développement', 'Etudes du développement'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Français langue étrangère', 'Français langue étrangère'), ('Informatique', 'Informatique'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Management', 'Management'), ('Géographie', 'Géographie'), ('Génie civil', 'Génie civil'), ('Economie internationale', 'Economie internationale'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ('Journalisme', 'Journalisme'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Sciences du médicament', 'Sciences du médicament'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Automatique, robotique', 'Automatique, robotique'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Démographie', 'Démographie'), ('Intervention et développement social', 'Intervention et développement '), ('Droit du patrimoine', 'Droit du patrimoine'), ("Management de l'innovation", "Management de l'innovation"), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Economie appliquée', 'Economie appliquée'), ('Economie du développement', 'Economie du développement'), ('Pharmacologie', 'Pharmacologie'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Biologie', 'Biologie'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Droit de la santé', 'Droit de la santé'), ('Sciences du vivant', 'Sciences du vivant'), ('Droit des affaires', 'Droit des affaires'), ('Droit public', 'Droit public'), ('Génétique', 'Génétique'), ('Droit administratif', 'Droit administratif'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Génie mécanique', 'Génie mécanique'), ('Génie industriel', 'Génie industriel'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Communication, publicité', 'Communication, publicité'), ('Marketing, vente', 'Marketing, vente'), ('Création numérique', 'Création numérique'), ('Mondes anciens', 'Mondes anciens'), ('Science politique', 'Science politique'), ('Droit notarial', 'Droit notarial'), ('Mathématiques', 'Mathématiques'), ('Ethique', 'Ethique'), ('Théologie', 'Théologie'), ('Droit civil', 'Droit civil'), ('Biomécanique', 'Biomécanique'), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Ingénierie de conception', 'Ingénierie de conception'), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Chimie moléculaire', 'Chimie moléculaire'), ('Finances publiques', 'Finances publiques'), ('Psychologie', 'Psychologie'), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Anthropologie', 'Anthropologie'), ('Humanités numériques', 'Humanités numériques'), ('Droit des libertés', 'Droit des libertés'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences sociales', 'Sciences sociales'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Santé', 'Santé'), ('Immunologie', 'Immunologie'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Géomatique', 'Géomatique'), ('Bio-informatique', 'Bio-informatique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Esthétique', 'Esthétique'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ('Politiques comparées', 'Politiques comparées'), ('Droit', 'Droit'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Géopolitique', 'Géopolitique'), ('Didactique des langues', 'Didactique des langues'), ('Communication publique et politique', 'Communication publique et poli'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Droit international', 'Droit international'), ('Sciences du langage', 'Sciences du langage'), ('Humanités', 'Humanités'), ('Création artistique', 'Création artistique'), ('Mode', 'Mode'), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Mondes contemporains', 'Mondes contemporains')], max_length=271, null=True),
        ),
    ]
