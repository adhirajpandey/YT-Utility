#Importing Libraries
from bs4 import BeautifulSoup
import csv


#Function Definitions
def parseHtml(htmlfile) -> dict:
    try:
        # page = open(htmlfile, 'r', encoding='utf-8')
        soup = BeautifulSoup(htmlfile, 'html.parser')

        videodata = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer')
        outdata = {}

        for video in videodata:
            video_url, video_title = (video['href'], video['title'])
            #building dictionary
            outdata[video_url] = video_title

        print("HTML Page Parsed Successfully")
        return outdata
    
    except Exception as e:
        print("Error Parsing HTML Page : ", e)

def makeCsv(data: dict):
    with open('watchlater.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title','Link'])
        
        for key, value in data.items():
            writer.writerow([value, key])
    
    print("CSV File Created Successfully")

def html2csv(htmlcode) -> str:
    datadict = parseHtml(htmlcode)
    makeCsv(datadict)

    with open('watchlater.csv', 'r', encoding='utf-8') as f:
        csvdata = f.read()

    return csvdata


# print(type(html2csv('samplewl.html')))

