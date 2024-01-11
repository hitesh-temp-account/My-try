import sys
import re

def code_coverage_report():
  if table_list == ""
    print(get_table_list(file_paths))

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

file_paths = sys.argv[1].split("\n")
table_list = sys.argv[2]

code_coverage_report()
