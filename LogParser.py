import re
from datetime import date
from pathlib import Path

print("-------Log parser started at: ",date.today())

error_cnt = 0
error_list = []
pattern = "^\[.+\]\s+\{.+\}\s+ERROR\s+.+"
airflow_log_path = "C://Users/gauri/AppData/Local/Packages/CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc/LocalState/rootfs/root/airflow/logs"

for p in Path(airflow_log_path).rglob( '*.log' ):
    filename = p
    f=open(filename,'r')
    contents = f.readlines()

    for content in contents:
        x = re.search(pattern,content)
        if x:
            error_cnt += 1
            error_list.append(content)


    f.close()


print("Total No of Errors: ",error_cnt)
print("Here are all the errors----")

for error in error_list:
    print(error)


print("----------Log parser ended at ",date.today())