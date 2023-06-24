import requests
import shodan
requests.packages.urllib3.disable_warnings()


API_KEY="g6AfgRJTNbIAQ8HlpP9ygqoifYAj3zXT"
SEARCH_FOR="http.favicon.hash:3A-855213521"

f=open("url.txt","a")


api = shodan.Shodan(API_KEY)

result = api.search(SEARCH_FOR,limit=1000)


for service in result['matches']:
    IP = service['ip_str']
    url="https://www.shodan.io/search?query=http.favicon.hash%3A-855213521".format(IP)
    f.writelines(url+"\n")


