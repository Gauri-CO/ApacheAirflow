from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime, date
from airflow.utils.dates import days_ago
import yfinance as yf
import pandas as pd

# EXEC_DATE = '{{ macros.ds_format(macros.ds_add(ds, 1), "%Y-%m-%d", "%Y%m%d") }}'
today = date.today()
EXEC_DATE = today.strftime("%Y%m%d")


def query_data():
    path_TSLA = "/tmp/output/" + EXEC_DATE + "/" + "TSLA" + "data.csv"
    df_TSLA = pd.read_csv(path_TSLA,
                     names=['datetime', 'open', 'high', 'low', 'close', 'adj_close', 'vol'])
    dff_TSLA = df_TSLA.aggregate({"open": ['min', 'max'], "vol": ["max"]})
    print(dff_TSLA)

    path_AAPL = "/tmp/output/" + EXEC_DATE + "/" + "AAPL" + "data.csv"
    df_AAPL = pd.read_csv(path_AAPL,
                          names=['datetime', 'open', 'high', 'low', 'close', 'adj_close', 'vol'])
    dff_AAPL = df_TSLA.aggregate({"open": ['min', 'max'], "vol": ["max"]})
    print(dff_AAPL)


def download_market_data(market_symbol):
    start_date = date.today()
    end_date = start_date + timedelta(days=1)
    df = yf.download(market_symbol, start=start_date, end=end_date, interval='1m')
    path = "/tmp/data/" + EXEC_DATE + "/" + market_symbol + "data.csv"
    print("Path is ", path)
    df.to_csv(path, header=False)


default_args = {
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('marketvol_dag', default_args=default_args, description='A simple DAG', schedule_interval='* 6 * * 1-5',
          start_date=days_ago(2))

t0 = BashOperator(
    task_id='CreateDownloadDir',
    bash_command='/root/airflow/scripts/makedir.sh ',
    dag=dag
)

t1 = PythonOperator(
    task_id='DownloadTSLA',
    python_callable=download_market_data,
    op_kwargs={'market_symbol': 'TSLA'},
    dag=dag
)

t2 = PythonOperator(
    task_id='DownloadAAPL',
    python_callable=download_market_data,
    op_kwargs={'market_symbol': 'AAPL'},
    dag=dag
)

t3 = BashOperator(
    task_id='MoveTSLA',
    bash_command='/root/airflow/scripts/movedir_TSLA.sh ',
    dag=dag
)

t4 = BashOperator(
    task_id='MoveAAPL',
    bash_command='/root/airflow/scripts/movedir_AAPL.sh ',
    dag=dag
)

t5 = PythonOperator(
    task_id='QueryData',
    python_callable=query_data,
    dag=dag
)


t0 >> t1
t0 >> t2
t1 >> t3
t2 >> t4
t5 << t3
t5 << t4



