# Generated by Django 2.2.5 on 2019-09-21 09:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20190921_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(blank=True, choices=[('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Droit des affaires', 'Droit des affaires'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Physique', 'Physique'), ('Sociologie', 'Sociologie'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Industries culturelles', 'Industries culturelles'), ('Philosophie', 'Philosophie'), ("Droit de l'économie", "Droit de l'économie"), ('Culture et communication', 'Culture et communication'), ('Etudes du développement', 'Etudes du développement'), ('Biologie', 'Biologie'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Droit notarial', 'Droit notarial'), ('Administration économique et sociale', 'Administration économique et s'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Intelligence économique', 'Intelligence économique'), ('Arts', 'Arts'), ('Sciences de la vie', 'Sciences de la vie'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Management et commerce international', 'Management et commerce interna'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Histoire de l'art", "Histoire de l'art"), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit public', 'Droit public'), ('Relations internationales', 'Relations internationales'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Logique', 'Logique'), ('Traduction et interprétation', 'Traduction et interprétation'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Management stratégique', 'Management stratégique'), ('Ethique', 'Ethique'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Sciences du vivant', 'Sciences du vivant'), ('Mode', 'Mode'), ('Théologie', 'Théologie'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Lettres', 'Lettres'), ('Informatique', 'Informatique'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Gestion', 'Gestion'), ('Journalisme', 'Journalisme'), ('Economie de la santé', 'Economie de la santé'), ('Neurosciences', 'Neurosciences'), ('Droit civil', 'Droit civil'), ('Théâtre', 'Théâtre'), ('Droit de la santé', 'Droit de la santé'), ('Santé', 'Santé'), ('Communication publique et politique', 'Communication publique et poli'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Génie industriel', 'Génie industriel'), ('Théologie catholique', 'Théologie catholique'), ('Acoustique', 'Acoustique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Biologie-santé', 'Biologie-santé'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Tourisme', 'Tourisme'), ("Management de l'innovation", "Management de l'innovation"), ('Administration publique', 'Administration publique'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Politiques comparées', 'Politiques comparées'), ('Biologie du développement', 'Biologie du développement'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Microbiologie', 'Microbiologie'), ('Génie mécanique', 'Génie mécanique'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Droit européen', 'Droit européen'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Intervention et développement social', 'Intervention et développement '), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Chimie moléculaire', 'Chimie moléculaire'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Ethologie', 'Ethologie'), ('Economie et gestion', 'Economie et gestion'), ('Droit public des affaires', 'Droit public des affaires'), ('Ergonomie', 'Ergonomie'), ('Lettres et humanités', 'Lettres et humanités'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Science politique', 'Science politique'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Littérature générale et comparée', 'Littérature générale et compar'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Finances publiques', 'Finances publiques'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Chimie', 'Chimie'), ('Sciences sociales', 'Sciences sociales'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Anthropologie', 'Anthropologie'), ('Management et administration des entreprises', 'Management et administration d'), ('Géomatique', 'Géomatique'), ('Sciences et technologies', 'Sciences et technologies'), ('Immunologie', 'Immunologie'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Création littéraire', 'Création littéraire'), ('Sciences cognitives', 'Sciences cognitives'), ('Géographie', 'Géographie'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Actuariat', 'Actuariat'), ('Economie appliquée', 'Economie appliquée'), ('Economie du développement', 'Economie du développement'), ('Génétique', 'Génétique'), ('Esthétique', 'Esthétique'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Droit', 'Droit'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Démographie', 'Démographie'), ('Ethnologie', 'Ethnologie'), ('Management sectoriel', 'Management sectoriel'), ('Management public', 'Management public'), ('Droit du numérique', 'Droit du numérique'), ('Information-communication', 'Information-communication'), ('Sciences de la mer', 'Sciences de la mer'), ('Archives', 'Archives'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Arts du spectacle', 'Arts du spectacle'), ('Droit privé', 'Droit privé'), ('Pharmacologie', 'Pharmacologie'), ('Psychologie', 'Psychologie'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Droit des assurances', 'Droit des assurances'), ('Energie', 'Energie'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Management', 'Management'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Marketing, vente', 'Marketing, vente'), ('Création numérique', 'Création numérique'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Mondes modernes', 'Mondes modernes'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Design', 'Design'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Sciences du médicament', 'Sciences du médicament'), ('Physique du vivant', 'Physique du vivant'), ('Santé publique', 'Santé publique'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Mondes anciens', 'Mondes anciens'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Arts plastiques', 'Arts plastiques'), ('Droit fiscal', 'Droit fiscal'), ('Droit comparé', 'Droit comparé'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Energétique, thermique', 'Energétique, thermique'), ('Mécanique', 'Mécanique'), ('Didactique des sciences', 'Didactique des sciences'), ('Economie et management publics', 'Economie et management publics'), ('Economie des organisations', 'Economie des organisations'), ('Etudes culturelles', 'Etudes culturelles'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Droit international', 'Droit international'), ('Français langue étrangère', 'Français langue étrangère'), ('Bio-informatique', 'Bio-informatique'), ('Psychanalyse', 'Psychanalyse'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Mondes contemporains', 'Mondes contemporains'), ('Histoire', 'Histoire'), ('Mathématiques', 'Mathématiques'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Biologie végétale', 'Biologie végétale'), ('Didactique des langues', 'Didactique des langues'), ('Politiques publiques', 'Politiques publiques'), ('Information, documentation', 'Information, documentation'), ('Biomécanique', 'Biomécanique'), ('Droit des libertés', 'Droit des libertés'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Economie du droit', 'Economie du droit'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Sciences du langage', 'Sciences du langage'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Musicologie', 'Musicologie'), ('Humanités', 'Humanités'), ('Génie civil', 'Génie civil'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Biotechnologies', 'Biotechnologies'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Communication, publicité', 'Communication, publicité'), ('Automatique, robotique', 'Automatique, robotique'), ('Information, communication', 'Information, communication'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Droit social', 'Droit social'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Lettres, langues', 'Lettres, langues'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Risques et environnement', 'Risques et environnement'), ('Théologie protestante', 'Théologie protestante'), ('Finance', 'Finance'), ('Création artistique', 'Création artistique'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Economie', 'Economie'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Communication des organisations', 'Communication des organisation'), ('Sciences de la matière', 'Sciences de la matière'), ('Géopolitique', 'Géopolitique'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Physique, chimie', 'Physique, chimie'), ('Ingénierie de conception', 'Ingénierie de conception'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Economie internationale', 'Economie internationale'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Humanités numériques', 'Humanités numériques'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences de l'eau", "Sciences de l'eau"), ('Bio-géosciences', 'Bio-géosciences'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Langues et sociétés', 'Langues et sociétés'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit administratif', 'Droit administratif'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Danse', 'Danse')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='completed_degree',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Comptabilité - contrôle - audit', 'Comptabilité - contrôle - audi'), ('Droit des affaires', 'Droit des affaires'), ('Muséologie, muséo-expographie', 'Muséologie, muséo-expographie'), ('Physique', 'Physique'), ('Sociologie', 'Sociologie'), ('Information et médiation scientifique et technique', 'Information et médiation scien'), ('Biodiversité, écologie et évolution', 'Biodiversité, écologie et évol'), ('Industries culturelles', 'Industries culturelles'), ('Philosophie', 'Philosophie'), ("Droit de l'économie", "Droit de l'économie"), ('Culture et communication', 'Culture et communication'), ('Etudes du développement', 'Etudes du développement'), ('Biologie', 'Biologie'), ('Ingénierie des systèmes complexes', 'Ingénierie des systèmes comple'), ('Droit notarial', 'Droit notarial'), ('Administration économique et sociale', 'Administration économique et s'), ('Nutrition et sciences des aliments', 'Nutrition et sciences des alim'), ('Intelligence économique', 'Intelligence économique'), ('Arts', 'Arts'), ('Sciences de la vie', 'Sciences de la vie'), ("Sciences de l'océan, de l'atmosphère et du climat", "Sciences de l'océan, de l'atmo"), ('Génie des procédés et des bio-procédés', 'Génie des procédés et des bio-'), ('Gestion des ressources humaines', 'Gestion des ressources humaine'), ('Géographie, aménagement, environnement et développement', 'Géographie, aménagement, envir'), ('Patrimoine et musées', 'Patrimoine et musées'), ('Management et commerce international', 'Management et commerce interna'), ("Sciences et technologie de l'agriculture, de l'alimentation et de l'environnement", "Sciences et technologie de l'a"), ("Histoire de l'art", "Histoire de l'art"), ("Droit de l'entreprise", "Droit de l'entreprise"), ('Analyse et politique économique', 'Analyse et politique économiqu'), ('Qualité, hygiène, sécurité', 'Qualité, hygiène, sécurité'), ('Droit public', 'Droit public'), ('Relations internationales', 'Relations internationales'), ('Toxicologie et éco-toxicologie', 'Toxicologie et éco-toxicologie'), ('Logique', 'Logique'), ('Traduction et interprétation', 'Traduction et interprétation'), ("Droit de l'immobilier", "Droit de l'immobilier"), ('Méthodes informatiques appliquées à la gestion des entreprises - MIAGE', 'Méthodes informatiques appliqu'), ('Droit constitutionnel', 'Droit constitutionnel'), ('Management stratégique', 'Management stratégique'), ('Ethique', 'Ethique'), ("Histoire de l'art et archéologie", "Histoire de l'art et archéolog"), ('Ingénierie nucléaire', 'Ingénierie nucléaire'), ('Econométrie, statistiques', 'Econométrie, statistiques'), ('Géoressources, géorisques, géotechnique', 'Géoressources, géorisques, géo'), ('Chimie et sciences du vivant', 'Chimie et sciences du vivant'), ('Sciences du vivant', 'Sciences du vivant'), ('Mode', 'Mode'), ('Théologie', 'Théologie'), ('Contrôle de gestion et audit organisationnel', 'Contrôle de gestion et audit o'), ('Biologie, agrosciences', 'Biologie, agrosciences'), ('Optique, image, vision, multimédia', 'Optique, image, vision, multim'), ('Aéronautique et espace', 'Aéronautique et espace'), ('Lettres', 'Lettres'), ('Informatique', 'Informatique'), ('Géographie et aménagement', 'Géographie et aménagement'), ('Gestion', 'Gestion'), ('Journalisme', 'Journalisme'), ('Economie de la santé', 'Economie de la santé'), ('Neurosciences', 'Neurosciences'), ('Droit civil', 'Droit civil'), ('Théâtre', 'Théâtre'), ('Droit de la santé', 'Droit de la santé'), ('Santé', 'Santé'), ('Communication publique et politique', 'Communication publique et poli'), ('Histoire du droit et des institutions', 'Histoire du droit et des insti'), ('Chimie physique et analytique', 'Chimie physique et analytique'), ('Droit pénal et sciences criminelles', 'Droit pénal et sciences crimin'), ('Sciences et techniques des activités physiques et sportives', 'Sciences et techniques des act'), ('Génie industriel', 'Génie industriel'), ('Théologie catholique', 'Théologie catholique'), ('Acoustique', 'Acoustique'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), pratiques et ingénierie de la formation", "Métiers de l'enseignement, de "), ('Biologie-santé', 'Biologie-santé'), ('Economie sociale et solidaire', 'Economie sociale et solidaire'), ('Tourisme', 'Tourisme'), ("Management de l'innovation", "Management de l'innovation"), ('Administration publique', 'Administration publique'), ('Arts de la scène et du spectacle vivant', 'Arts de la scène et du spectac'), ('Gestion des territoires et développement local', 'Gestion des territoires et dév'), ('Politiques comparées', 'Politiques comparées'), ('Biologie du développement', 'Biologie du développement'), ("Métiers du livre et de l'édition", "Métiers du livre et de l'éditi"), ('Instrumentation, mesure, métrologie', 'Instrumentation, mesure, métro'), ('Microbiologie', 'Microbiologie'), ('Génie mécanique', 'Génie mécanique'), ('STAPS : entraînement et optimisation de la performance sportive', 'STAPS : entraînement et optimi'), ('Transport, mobilités, réseaux', 'Transport, mobilités, réseaux'), ('Droit européen', 'Droit européen'), ('Epistémologie, histoire des sciences et des techniques', 'Epistémologie, histoire des sc'), ('Intervention et développement social', 'Intervention et développement '), ("Administration et liquidation d'entreprises en difficulté", 'Administration et liquidation '), ('Chimie moléculaire', 'Chimie moléculaire'), ('Réseaux et télécommunication', 'Réseaux et télécommunication'), ('STAPS : management du sport', 'STAPS : management du sport'), ('Ethologie', 'Ethologie'), ('Economie et gestion', 'Economie et gestion'), ('Droit public des affaires', 'Droit public des affaires'), ('Ergonomie', 'Ergonomie'), ('Lettres et humanités', 'Lettres et humanités'), ('Etudes européennes et internationales', 'Etudes européennes et internat'), ("Droit de l'environnement et de l'urbanisme", "Droit de l'environnement et de"), ('Humanités et industries créatives', 'Humanités et industries créati'), ('Sciences économiques et sociales', 'Sciences économiques et social'), ('Science politique', 'Science politique'), ('Monnaie, banque, finance, assurance', 'Monnaie, banque, finance, assu'), ('Littérature générale et comparée', 'Littérature générale et compar'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 2e degré", "Métiers de l'enseignement, de "), ('Sciences de la Terre et des planètes, environnement', 'Sciences de la Terre et des pl'), ('Agrosciences, environnement, territoires, paysage, forêt', 'Agrosciences, environnement, t'), ('Finances publiques', 'Finances publiques'), ('Droit des collectivités territoriales', 'Droit des collectivités territ'), ('Physique appliquée et ingénierie physique', 'Physique appliquée et ingénier'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales', 'Mathématiques et informatique '), ('Droit bancaire et financier', 'Droit bancaire et financier'), ('Chimie', 'Chimie'), ('Sciences sociales', 'Sciences sociales'), ('Mathématiques et applications', 'Mathématiques et applications'), ('Anthropologie', 'Anthropologie'), ('Management et administration des entreprises', 'Management et administration d'), ('Géomatique', 'Géomatique'), ('Sciences et technologies', 'Sciences et technologies'), ('Immunologie', 'Immunologie'), ('Histoire de la philosophie', 'Histoire de la philosophie'), ('Création littéraire', 'Création littéraire'), ('Sciences cognitives', 'Sciences cognitives'), ('Géographie', 'Géographie'), ('Civilisations, cultures et sociétés', 'Civilisations, cultures et soc'), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), encadrement éducatif", "Métiers de l'enseignement, de "), ('Actuariat', 'Actuariat'), ('Economie appliquée', 'Economie appliquée'), ('Economie du développement', 'Economie du développement'), ('Génétique', 'Génétique'), ('Esthétique', 'Esthétique'), ("Ingénierie de l'image, ingénierie du son", "Ingénierie de l'image, ingénie"), ('Droit', 'Droit'), ('Psychologie : psychopathologie clinique psychanalytique', 'Psychologie : psychopathologie'), ('Démographie', 'Démographie'), ('Ethnologie', 'Ethnologie'), ('Management sectoriel', 'Management sectoriel'), ('Management public', 'Management public'), ('Droit du numérique', 'Droit du numérique'), ('Information-communication', 'Information-communication'), ('Sciences de la mer', 'Sciences de la mer'), ('Archives', 'Archives'), ('Sciences et génie des matériaux', 'Sciences et génie des matériau'), ('Arts du spectacle', 'Arts du spectacle'), ('Droit privé', 'Droit privé'), ('Pharmacologie', 'Pharmacologie'), ('Psychologie', 'Psychologie'), ("Archéologie, sciences pour l'archéologie", "Archéologie, sciences pour l'a"), ('Droit des assurances', 'Droit des assurances'), ('Energie', 'Energie'), ('Langues étrangères appliquées', 'Langues étrangères appliquées'), ('Sciences sanitaires et sociales', 'Sciences sanitaires et sociale'), ('Traitement automatique des langues', 'Traitement automatique des lan'), ('Management', 'Management'), ('Gestion de patrimoine', 'Gestion de patrimoine'), ('Arts, lettres et civilisations', 'Arts, lettres et civilisations'), ('Ingénierie de la santé', 'Ingénierie de la santé'), ('Marketing, vente', 'Marketing, vente'), ('Création numérique', 'Création numérique'), ('Innovation, entreprise et société', 'Innovation, entreprise et soci'), ('Sciences et techniques des activités physiques et sportives ― STAPS', 'Sciences et techniques des act'), ("Sciences de l'homme, anthropologie, ethnologie", "Sciences de l'homme, anthropol"), ('Mondes modernes', 'Mondes modernes'), ('Biologie structurale, génomique', 'Biologie structurale, génomiqu'), ('Design', 'Design'), ('Droit du patrimoine', 'Droit du patrimoine'), ('Sciences des religions et sociétés', 'Sciences des religions et soci'), ('Direction de projets ou établissements culturels', 'Direction de projets ou établi'), ('Sciences du médicament', 'Sciences du médicament'), ('Physique du vivant', 'Physique du vivant'), ('Santé publique', 'Santé publique'), ('Langues, littératures et civilisations étrangères et régionales', 'Langues, littératures et civil'), ("Economie de l'environnement, de l'énergie et des transports", "Economie de l'environnement, d"), ('Mondes anciens', 'Mondes anciens'), ('Psychologie sociale, du travail et des organisations', 'Psychologie sociale, du travai'), ('Arts plastiques', 'Arts plastiques'), ('Droit fiscal', 'Droit fiscal'), ('Droit comparé', 'Droit comparé'), ('Administration et échanges internationaux', 'Administration et échanges int'), ('Energétique, thermique', 'Energétique, thermique'), ('Mécanique', 'Mécanique'), ('Didactique des sciences', 'Didactique des sciences'), ('Economie et management publics', 'Economie et management publics'), ('Economie des organisations', 'Economie des organisations'), ('Etudes culturelles', 'Etudes culturelles'), ('Cinéma et audiovisuel', 'Cinéma et audiovisuel'), ('Droit international', 'Droit international'), ('Français langue étrangère', 'Français langue étrangère'), ('Bio-informatique', 'Bio-informatique'), ('Psychanalyse', 'Psychanalyse'), ('STAPS : activité physique adaptée et santé', 'STAPS : activité physique adap'), ('Mondes contemporains', 'Mondes contemporains'), ('Histoire', 'Histoire'), ('Mathématiques', 'Mathématiques'), ("Sciences pour l'ingénieur", "Sciences pour l'ingénieur"), ("Métiers de l'enseignement, de l'éducation et de la formation (MEEF), 1er degré", "Métiers de l'enseignement, de "), ('Biologie végétale', 'Biologie végétale'), ('Didactique des langues', 'Didactique des langues'), ('Politiques publiques', 'Politiques publiques'), ('Information, documentation', 'Information, documentation'), ('Biomécanique', 'Biomécanique'), ('Droit des libertés', 'Droit des libertés'), ("Gestion de l'environnement", "Gestion de l'environnement"), ('Economie du droit', 'Economie du droit'), ('Etudes sur le genre', 'Etudes sur le genre'), ('Sciences du langage', 'Sciences du langage'), ('Urbanisme et aménagement', 'Urbanisme et aménagement'), ('Mondes médiévaux', 'Mondes médiévaux'), ('Management des PME-PMI', 'Management des PME-PMI'), ('Musicologie', 'Musicologie'), ('Humanités', 'Humanités'), ('Génie civil', 'Génie civil'), ("Economie de l'entreprise et des marchés", "Economie de l'entreprise et de"), ('Astrophysique, astronomie, planétologie', 'Astrophysique, astronomie, pla'), ('Entrepreneuriat et management de projets', 'Entrepreneuriat et management '), ('Biotechnologies', 'Biotechnologies'), ('Histoire, civilisations, patrimoine', 'Histoire, civilisations, patri'), ('Mathématiques et informatique appliquées aux sciences humaines et sociales - MIASHS', 'Mathématiques et informatique '), ('Gestion de production, logistique, achats', 'Gestion de production, logisti'), ('Communication, publicité', 'Communication, publicité'), ('Automatique, robotique', 'Automatique, robotique'), ('Information, communication', 'Information, communication'), ('Ville et environnements urbains', 'Ville et environnements urbain'), ('Droit social', 'Droit social'), ('Sciences de la Terre', 'Sciences de la Terre'), ('Lettres, langues', 'Lettres, langues'), ('Architecture, urbanisme, paysage', 'Architecture, urbanisme, paysa'), ('Risques et environnement', 'Risques et environnement'), ('Théologie protestante', 'Théologie protestante'), ('Finance', 'Finance'), ('Création artistique', 'Création artistique'), ('Biologie moléculaire et cellulaire', 'Biologie moléculaire et cellul'), ("Sciences de l'information et des bibliothèques", "Sciences de l'information et d"), ("Sciences de l'éducation", "Sciences de l'éducation"), ('Biologie intégrative et physiologie', 'Biologie intégrative et physio'), ('Nanosciences et nanotechnologies', 'Nanosciences et nanotechnologi'), ('Economie', 'Economie'), ('Audiovisuel, médias interactifs numériques, jeux', 'Audiovisuel, médias interactif'), ('Communication des organisations', 'Communication des organisation'), ('Sciences de la matière', 'Sciences de la matière'), ('Géopolitique', 'Géopolitique'), ('Electronique, énergie électrique, automatique', 'Electronique, énergie électriq'), ('Calcul haute performance, simulation', 'Calcul haute performance, simu'), ('Physique, chimie', 'Physique, chimie'), ('Ingénierie de conception', 'Ingénierie de conception'), ("STAPS : ingénierie et ergonomie de l'activité physique", 'STAPS : ingénierie et ergonomi'), ('Conservation-restauration des biens culturels', 'Conservation-restauration des '), ('Chimie et sciences des matériaux', 'Chimie et sciences des matéria'), ('Economie internationale', 'Economie internationale'), ('Physique fondamentale et applications', 'Physique fondamentale et appli'), ('Psychologie clinique, psychopathologie et psychologie de la santé', 'Psychologie clinique, psychopa'), ('Mathématiques appliquées, statistique', 'Mathématiques appliquées, stat'), ('Economie industrielle et des réseaux', 'Economie industrielle et des r'), ('Economie du travail et des ressources humaines', 'Economie du travail et des res'), ('Humanités numériques', 'Humanités numériques'), ('Sciences pour la santé', 'Sciences pour la santé'), ("Sciences de l'eau", "Sciences de l'eau"), ('Bio-géosciences', 'Bio-géosciences'), ('Justice, procès et procédures', 'Justice, procès et procédures'), ('Biochimie, biologie moléculaire', 'Biochimie, biologie moléculair'), ('Langues et sociétés', 'Langues et sociétés'), ("Psychologie de l'éducation et de la formation", "Psychologie de l'éducation et "), ('Droit de la propriété intellectuelle', 'Droit de la propriété intellec'), ('Droit administratif', 'Droit administratif'), ("Management des systèmes d'information", "Management des systèmes d'info"), ('Sciences de la vie et de la Terre', 'Sciences de la vie et de la Te'), ('Traitement du signal et des images', 'Traitement du signal et des im'), ('Danse', 'Danse')], max_length=271, null=True),
        ),
    ]