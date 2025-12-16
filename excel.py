import pandas

data_frame = pandas.read_csv("PBJ Report.csv")

user_ids_list = data_frame['User ID']

names = data_frame["Provider"]

def set_job_title_code(job_title):
    job_titles = {"CNA": 10, "LVN": 9, "Medication Aide": 12}

    return job_titles[job_title]