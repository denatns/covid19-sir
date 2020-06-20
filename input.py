import os, glob, shutil, requests
cwd = os.getcwd()
# Put your kaggle.json in the same folder as input.py
os.environ["KAGGLE_CONFIG_DIR"] = cwd+"/"
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
path_ = cwd+"/input/"

shutil.rmtree(path_)

api.dataset_download_files('dgrechka/covid19-global-forecasting-locations-population', 
            path=path_+"/", 
            unzip=True)

api.dataset_download_files('sudalairajkumar/novel-corona-virus-2019-dataset', 
            path=path_+"/", 
            unzip=True)

api.dataset_download_files('lisphilar/covid19-dataset-in-japan', 
            path=path_+"/", 
            unzip=True)

file_list = glob.glob(path_+'/*')
file_list_keep = file_list
file_list_keep = [ele for ele in file_list_keep if not "time_series_covid_19_" in ele]
file_list_keep = [ele for ele in file_list_keep if not "COVID19_line_list_data.csv" in ele]
file_list_keep = [ele for ele in file_list_keep if not "COVID19_open_line_list.csv" in ele]
for file_ in file_list:
    if file_ not in file_list_keep:
        os.remove(file_)

OxCGRT_files = ["https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv", "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest_allchanges.csv", "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest_responses.csv", "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest_withnotes.csv"]

if not os.path.exists(path_+"oxcgrt/"):
    os.makedirs(path_+"oxcgrt/")

for oxcgrt_file in OxCGRT_files:
    r = requests.get(oxcgrt_file, allow_redirects=True)
    open(path_+"oxcgrt/"+oxcgrt_file.rsplit('/', 1)[-1], 'wb').write(r.content)