def algo():    
    drugs = []
    drugs.append({'id':0,'name':'Metformin','times':3,'restrictions':[]})
    drugs.append({'id':1,'name':'Amlodipine','times':1,'restrictions':[]})
    drugs.append({'id':2,'name':'HCTZ','times':1,'restrictions':[]})
    drugs.append({'id':3,'name':'Captopril','times':2,'restrictions':[]})
    drugs.append({'id':4,'name':'Metoprolol','times':1,'restrictions':[]})
    drugs.append({'id':5,'name':'Omeprazole','times':1,'restrictions':['empty']})
    drugs.append({'id':6,'name':'Simvastatin','times':1,'restrictions':[]})
    drugs.append({'id':7,'name':'Aspirin','times':1,'restrictions':['food']})
    #drugs.append({'id':7,'name':'Antibiotic','times':3,'restrictions':['food']})
    #drugs.append({'id':8,'name':'Benzoate Protozine','times':4,'restrictions':['empty']})

    #drugs = [drug0, drug1, drug2, drug3, drug4, drug5]
    # move the most frequent drug to the front of the list
    max_times = 0
    most_freq_drug = 0
    for drug in drugs:
        if drug["times"] > max_times:
            max_times = drug["times"]
            most_freq_drug = drug["id"]
    drugs.insert(0, drugs.pop(most_freq_drug))

    schedule = {
            "pre-breakfast" : [],
        "post-breakfast" : [],
        "pre-lunch" : [],
        "post-lunch" : [],
        "pre-dinner" : [],
        "post-dinner" : [],
        "sleep" : []
    }
    keys_unordered = [
        "pre-breakfast",
        "pre-dinner",
        "pre-lunch",
        "sleep",
        "post-breakfast",
        "post-dinner",
        "post-lunch"
    ]
    keys = [
        "pre-breakfast",
        "post-breakfast",
        "pre-lunch",
        "post-lunch",
        "pre-dinner",
        "post-dinner",
        "sleep"
    ]
    for drug in drugs:
        if "empty" in drug["restrictions"]:
            schedule["pre-breakfast"].append(drug)
            if drug["times"] >= 2:
                schedule["pre-dinner"].append(drug)
                if drug["times"] >= 3:
                    schedule["pre-lunch"].append(drug)
                    if drug["times"] >= 4:
                        schedule["sleep"].append(drug)
                        if drug["times"] > 4:
                            print "drug must be taken over 4 times a day with empty stomach" 
        elif "food" in drug["restrictions"]:
            schedule["post-breakfast"].append(drug)
            if drug["times"] >= 2:
                schedule["post-dinner"].append(drug)
                if drug["times"] >= 3:
                    schedule["post-lunch"].append(drug)
                    if drug["times"] > 3:
                        print "drug must be taken over 3 times a day with food"
        else: # no empty or food restriction
            times = drug["times"]    
            index = 0

            # find number of time slots that have already been filled
            filled_times = 0
            for time in keys:
                if len(schedule[time]) > 0:
                    filled_times = filled_times + 1 

            while times > 0:
                time = keys_unordered[index]
                if (len(schedule[time]) > 0)|(times >= filled_times):
                    schedule[time].append(drug)
                    times = times - 1
                    filled_times = filled_times - 1
                index = index + 1
                if index == len(keys):
                    #print "drug must be taken over 8 times a day"
                    break
                
    return schedule
