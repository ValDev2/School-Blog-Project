import requests

#COllege browser URL
url = "https://data.enseignementsup-recherche.gouv.fr/api/records/1.0/search/?dataset=fr-esr-principaux-etablissements-enseignement-superieur&rows=3350&facet=uai&facet=type_d_etablissement&facet=typologie_d_universites_et_assimiles&facet=secteur_d_etablissement&facet=localisation&facet=siret&facet=siren&facet=identifiant_grid&facet=com_nom&facet=dep_nom&facet=aca_nom&facet=reg_nom&facet=pays_etranger_acheminement&facet=statut_juridique_court&facet=qualification_long&facet=statut_operateur_lolf&facet=identifiant_programme_lolf_chef_de_file&facet=identifiant_interne&facet=anciens_codes_uai&facet=identifiant_dataesr&facet=uai_rgp_loi_esr_2013&facet=universites_fusionnees&facet=etablissement_experimental&facet=vague_contractuelle"


#Calling the API to get 1 : all colleges from France, 2 : all internal_code from them
response = requests.get(url).json()
schools = [univ['fields']['uo_lib'] for univ in response['records']]
#Improtant ! Here a the codes for each schools !
schools_code = [univ['fields']['com_nom'] for univ in response['records']]

#Checking if there are enough codes (no duplicates) for each college
print(len(schools) == len(set(schools_code)))

#Generating the tuple
college_list = []
for i in range(0, len(schools)):
    item = (schools[i], schools[i])
    college_list.append(item)

college_list = tuple(college_list)


#Getting datas about degress / masters

url2 = "https://data.enseignementsup-recherche.gouv.fr/api/records/1.0/search/?dataset=fr_esr_mentions_de_licence_vers_master&rows=810&facet=licence&facet=master"

response2 = requests.get(url2).json()
result_licences = [item['fields']['licence'] for item in response2['records']]
result_masters = [item['fields']['master'] for item in response2['records']]
all_results = result_masters + result_licences
formations = [(item, item[:30]) for item in all_results]
formations = set(formations)
