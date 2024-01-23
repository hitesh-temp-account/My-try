import sys
import re

def code_coverage_report():
  if table_string == 'null':
    print(get_table_list(file_paths))
  else:
    base_table_list = get_table_list(file_paths).split(',')
    head_table_list = table_string.split(',')

    html = "<h2>Code coverage</h2>"
    html += "<table><tr><th>Module</th><th>Coverage</th>"
    if head_table_list:
      html += <th>Coverage</th>
      table_list = head_table_list
    else:
      table_list = base_table_list
    html += "</tr>"
    
    for index in range(0, len(table_list), 3):
      start_tag = ""
      end_tag = ""
      link_tag = f"<a href='{table_list[index+2]}'>"
      if index == len(table_list)-3:
        start_tag = "<b>"
        end_tag = "</b>"
        link_tag = ""
      html += f"<tr><td>{start_tag}{link_tag}{table_list[index]}{end_tag}</td>" \
              f"<td>{start_tag}<img src={format_percentage(table_list[index+1])}>{end_tag}</td>"
      if head_table_list:
        diff = float(head_table_list[index+1])
        if head_table_list[index] in base_table_list:
          moduleIndex = base_table_list.index(head_table_list[index])
          diff -= float(base_table_list[moduleIndex+1])
          html += f"<td>{round(diff,2)}%</td>"
      html += "</tr>"
    html += "</table><br><i>MIN Cverage: 35%</i>"
    print(html)

def get_table_list(file_paths):
  coveredSum=0
  totalSum=0
  table_string=[]
  for file in file_paths:
    file_text = open(file, 'rt').read()
    values = re.findall(r'Total</td><td class="bar">(.*?)</td>', file_text, re.DOTALL)[0].split(" ")
    module_name = re.findall(r'<h1>(.*?)</h1>', file_text, re.DOTALL)[0]
    missed = int(values[0].replace(",", ""))
    total = int(values[2].replace(",", ""))
    covered = total - missed
    module_coverage_percentage = round((covered/total)*100, 2)
    module_link = "xyz"
    table_string.append(f"{module_name},{module_coverage_percentage},{module_link},")
    coveredSum += covered
    totalSum += total
  table_string.sort()
  overall_coverage = round((coveredSum/totalSum)*100, 2)
  table_string.append(f"Overall coverage,{overall_coverage},")
  table_string="".join(table_string)
  return table_string
  
def format_percentage(coverage):
  color = "red" if float(coverage) < 35 else "green"
  coverage = f"https://img.shields.io/badge/{coverage}%25-{color}.svg"
  return coverage

file_paths = sys.argv[1].split("\n")
table_string = sys.argv[2]

code_coverage_report()
