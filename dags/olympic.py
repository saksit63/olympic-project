# from airflow.operators.python import PythonOperator
import requests


def get_data():
    athletes = requests.get("https://raw.githubusercontent.com/saksit63/olympic-project/main/dataset/Athletes.csv")
    coaches = requests.get("https://raw.githubusercontent.com/saksit63/olympic-project/main/dataset/Coaches.csv")
    entries_gender = requests.get("https://raw.githubusercontent.com/saksit63/olympic-project/main/dataset/Coaches.csv")
    medals = requests.get("https://raw.githubusercontent.com/saksit63/olympic-project/main/dataset/Coaches.csv")
    teams = requests.get("https://raw.githubusercontent.com/saksit63/olympic-project/main/dataset/Coaches.csv")
    print(athletes)

get_data
    