import requests


def dowload_from_url(url):
    
    r = requests.get(url)
  
    with open("python.csv","wb") as pdf:
        pdf.write(r.content)

def main():
    
    url = r'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
	
    print("starting")
    dowload_from_url(url)
    print("download complted")
        



if __name__=="__main__":
	main()