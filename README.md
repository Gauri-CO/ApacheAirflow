# ApacheAirflow


**Apache AirFlow Mini Project Part1 (Create and Schedule DAG)**
1. Create the Airflow DAG
Create the DAG object with name “marketvol”. Set the default arguments. Your DAG run should
follows:
- Start time and date: 6 PM on the current date.
- Job interval: runs once daily.
- Only runs on weekdays (Mon-Fri).
- If failed: retry twice with a 5-minute interval.

2. Create operators associated with the DAG
2.1. Create a BashOperator to initialize a temporary directory for data download (t0)
2.2. Create a PythonOperator to download the market data (t1, t2)
2.3. Create BashOperator to move the downloaded file to a data location (t3, t4)
2.4. Create a PythonOperator to run a query on both data files in the specified location(t5)

3. Set job dependencies
After defining all the tasks, you need to set their job dependencies so:
- t1 and t2 must run only after t0
- t3 must run after t1
- t4 must run after t2
- t5 must run after both t3 and t4 are complete

Steps to Run:
1. Download the files on Git Hub.
2. Save the .py file in /root/airflow/dags directory
3. Save the .sh file in /root/airflow/scripts directory
4. Execute : airflow db init
5. Execute : airflow scheduler
6. Execute : airflow webserver -p 8080 
Copy : localhost:8080 in your web browser and this will open the Airflow Web UI to monitor the job status

Components:\
DAG File : airflowminiproject.py\
Scripts: \
makedir.sh (t0)\
movedir_TSLA.sh (t3)\
movedir_AAPL.sh (t4)


**DAG Screenshot:** \
![image](https://user-images.githubusercontent.com/75573079/128521311-33a506f8-66ae-4d65-9498-483cf748ed70.png)

![image](https://user-images.githubusercontent.com/75573079/128521336-95e87ced-3809-4f34-83ea-b23db3e66792.png)

![image](https://user-images.githubusercontent.com/75573079/128521353-80bee6c9-42b8-49fa-a145-8fa1a90ada15.png)

![image](https://user-images.githubusercontent.com/75573079/128521382-ad1139dc-1ec9-4b74-a016-cf1e953f2aa4.png)



**Apache AirFlow Mini Project 2 (Log Analyzer)**

Python script to process the Airflow Logs and identify the Error messages.
Log analyzer should show the following information:
- The total count of error messages
- A detailed message regarding each error

Usage:
python LogParser.py
Specify the location of Airflow log directory

![image](https://user-images.githubusercontent.com/75573079/128536421-6fdba443-6b24-4d08-9695-44abe54b17fa.png)


