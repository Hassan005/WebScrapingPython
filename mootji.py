import pymongo
client = pymongo.MongoClient("mongodb://mootje:mootje2000@82.217.36.166/properties") # defaults to port 27017
db=client.properties
col=db.ids
import json



from selenium import webdriver
chromedriver_location = "H:/setups/selenium/chromedriver"

docs=col.find()
list_=[]
for i in docs:
    list_.append(i)
print(list_[-1])
s=list_[-1]
start=s["starting_ids"]
print(start)
end=s["ending_ids"]
url=s["search_url"]
range1=s["query"]
# start = int(input('Please input starting id...'))

# end = int(input('Please input ending id...'))
arr = []
idInput = ''
# range1 = 50
no = 0
inserted = 0
if (end > start):
    rang = len(range(end-start))+1
    for i in (range(rang)):
        no = i
        if (inserted >= range1):
#             print('naye',arr)
            idInput = idInput[:-1]
           
            print(idInput)
#             str1 = ','.join(str(e) for e in arr)
#             print(str1)
            arr.append(idInput)
#             print(arr)
            idInput = ''
            inserted = 0
#             print(arr, no+start, end)
            if (no+start < end+1):
                idInput = idInput + str(no+start) + ','
#                 print(idInput)
                inserted += 1
                if(no+start == end):
                    idInput = idInput[:-1]

                    arr.append(idInput)
                    idInput = ''
                    inserted = 0
#                     print(arr, no+start, end)
        else:
#             print('eys',arr)
            idInput = idInput + str(no+start) + ','
#             print(idInput)
            inserted += 1
            if(no+start == end):
                idInput = idInput[:-1]
                arr.append(idInput)
                idInput = ''
                inserted = 0
#                 print(arr, no+start, end)

temp = s["name"]
colSave=db[temp]
print(colSave)
for i in arr:
    
    driver = webdriver.Chrome(chromedriver_location)
    driver.get(url)
    input_field='//*[@id="objectIds"]'
    driver.find_element_by_xpath(input_field).send_keys(i)
    select_box='//*[@id="f"]/option[2]'
    driver.find_element_by_xpath(select_box).click()
    get_json='/html/body/div/form/table/tbody/tr[36]/td/input[1]'
    driver.find_element_by_xpath(get_json).click()
    txt=driver.find_element_by_xpath("/html/body/pre").text
    data=json.loads(txt)
    print(type(data))
    colSave.insert_one(data)
    print('hi json')