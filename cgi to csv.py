import csv
import xml.etree.ElementTree as ET
import os
import glob

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = []

    for bug in root.findall('.//bug'):
        bug_id = bug.find('.//bug_id').text if bug.find('.//bug_id') is not None else ''
        short_desc = bug.find('.//short_desc').text if bug.find('.//short_desc') is not None else ''
        resolution = bug.find('.//resolution').text if bug.find('.//resolution') is not None else ''

        comments = bug.findall('.//long_desc')
        comment_texts = [comment.find('.//thetext').text for comment in comments if comment.find('.//thetext') is not None]

        row = [bug_id, short_desc, resolution] + comment_texts

        data.append(row)
    
    return data

def write_to_csv(data, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        max_comments = max(len(row) - 3 for row in data)
        comment_headers = ['Comment' + str(i) for i in range(1, max_comments + 1)]

        csvwriter.writerow(['Bug ID', 'Short Description', 'Resolution'] + comment_headers)

        for row in data:
            csvwriter.writerow(row)


input_directory = 'C:/Users/ntaba/OneDrive/Desktop/SE/new bugs'  

input_files = glob.glob(os.path.join(input_directory, '*.cgi'))


for input_file in input_files:
 
    xml_data = parse_xml(input_file)


    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(input_directory, f'{base_name}.csv')
    write_to_csv(xml_data, output_file)






