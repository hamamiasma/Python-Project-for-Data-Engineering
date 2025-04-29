import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

#functions to extract the data from different file formats

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 

'''
To extract from an XML file, you need first to parse the data from the file using the ElementTree function. 
You can then extract relevant information from this data and append it to a pandas dataframe as follows.

def extract_from_xml(file_to_process):
    rows = []  # إنشاء قائمة فاضية لتجميع الصفوف
    tree = ET.parse(file_to_process)  # قراءة ملف XML
    root = tree.getroot()  # الحصول على الجذر الرئيسي
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        new_row = {"name": name, "height": height, "weight": weight}
        rows.append(new_row)  # إضافة كل صف إلى القائمة
    dataframe = pd.DataFrame(rows)  # إنشاء DataFrame دفعة واحدة من كل الصفوف
    return dataframe

'''
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 

'''
Now you need a function to identify which function to call on basis of the filetype of the data file. 
To call the relevant function, write a function extract, which uses the glob library to identify the filetype. 
This can be done as follows:
'''

def extract(): 
    #create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['name','height','weight']) 
     
    # process all csv files, except the target file
    for csvfile in glob.glob("*.csv"): 
        if csvfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

'''
We need to load the transformed data to a CSV file that you can use to load to a database as per requirement.
'''
def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 


def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 

        f.write(timestamp + ',' + message + '\n') 

        
        
# Testing ETL operations and log progress
# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 
