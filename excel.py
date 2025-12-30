import csv

def create_json_file():

    with open("PBJ Report.csv", "r") as file:
        csv_File = csv.DictReader(file)
        dict_list= []

        for line in csv_File:
            if line.get("Provider") == '':
                continue

            id = line.get("User ID")
            first_name = _set_name(line.get("Provider"))[1].strip()
            last_name = _set_name(line.get("Provider"))[0]
            job_tite_code = _set_job_title_code(line.get("Certification"))
            
            dict_data = {"id": id, "firstName": first_name, "lastName": last_name, "jobTitleCode": job_tite_code}   

            dict_list.append(dict_data)

    id_set = set()       

    for x in dict_list:
        id_set.add(x["id"])

    json_data = []    

    while id_set:
        top = id_set.pop()

        first_occurence = next((dic for dic in dict_list if dic["id"] == top), None)  

        json_data.append(first_occurence)

    print(json_data)           

def _set_name(name):
    full_name = name.split(",")

    return full_name

def _set_job_title_code(job_title):
    job_titles = {"CNA": 10, "LVN": 9, "Medication Aide": 12}

    return job_titles.get(job_title)