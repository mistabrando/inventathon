def sample():
	drugs = []
	drugs.append({'id':0,'name':'Metformin','times':3,'restrictions':[]})
	drugs.append({'id':1,'name':'Amlodipine','times':1,'restrictions':[]})
	drugs.append({'id':2,'name':'HCTZ','times':1,'restrictions':[]})
	drugs.append({'id':3,'name':'Captopril','times':2,'restrictions':[]})
	drugs.append({'id':4,'name':'Metoprolol','times':1,'restrictions':[]})
	drugs.append({'id':5,'name':'Omeprazole','times':1,'restrictions':['empty']})
	drugs.append({'id':6,'name':'Simvastatin','times':1,'restrictions':[]})
	drugs.append({'id':7,'name':'Antibiotic','times':3,'restrictions':['food']})
	drugs.append({'id':8,'name':'Benzoate Protozine','times':4,'restrictions':['empty']})
	data = {'data' : drugs}
	table = "<table class = 'table-bordered><tr><td>Name</td><td>Times/Day</td><td>Restrictions</td></tr>"
	for drug in data['data']:
		table = table + "<td>" + drug['name'] + "</td>"
		table = table + "<td>" + str(drug['times']) + "</td><td>"
		for restriction in drug['restrictions']:
			table = table + restriction + "<br>"
		table = table + "</td>"
	table = table + "</table>"
	return str(table)
