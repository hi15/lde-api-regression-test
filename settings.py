'''Settings used by LDE regression test'''

'''URL API to test'''
BASE_URL = 'https://simcaq.c3sl.ufpr.br/api/v1/'

'''List of all base routes available to test'''
BASE_ROUTE_LIST = [
		['class'],
		['enrollment'],
		['enrollment', '&dims=location'],
		['enrollment', '&dims=rural_location'],
		['enrollment', '&dims=school_year'],
		['enrollment', '&dims=educational_level'],
		['enrollment', '&dims=adm_dependency'],
		['enrollment', '&dims=gender'],
		['state'],
		['region'],
		['city'],
		['school','id:11000023'],
		['classroom'],
		['teacher'],
		['idhm', '&dims=state'],
		['idhmr','&dims=state'],
		['idhml','&dims=state'],
		['idhme', '&dims=state'],
		['pibpercapita'],
		['population'],
		['rate_school','&dims=age_range'],
		['gloss_enrollment_ratio','&dims=education_level_basic'],
		['liquid_enrollment_ratio','&dims=education_level_basic'],
		['education_years'],
		['infrastructure'],
		#['school_infrastructure'],
		#['siope'],
		['out_of_school'],
		#['class_count','&dims=education_level_mod'],
		['daily_charge_amount','integral_time:\"1\"'],
		['transport'],
		['cub'],
		['auxiliar'],
		#'portal_mec_inep',
		['enrollment_projection'],
		['employees'],
		['financial'],
		['university_enrollment'],
		#['university'],
		['university_teacher'],
		['course_count']
]

'''SIMCAQ ROUTE LIST'''
SIMCAQ_ROUTE_LIST = [
	['enrollment','&dims=adm_dependency_detailed,location'],
	['enrollment','&dims=region']
]

'''LDE ROUTE LIST'''
LDE_ROUTE_LIST = []
