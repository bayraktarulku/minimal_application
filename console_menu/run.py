import os

import click
import pandas as pd
from menu import ConsoleMenu


def cls():
    os.system("clear")


def list():
    cls()
    df = pd.read_csv("file.csv")
    print("############## List ##############")
    print(df)
    return df


def add():
    cls()
    print("############## Add record to List ##############")
    df = pd.read_csv("file.csv")
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    df.loc[df.shape[0]] = [name, surname, age]
    df.to_csv("file.csv", index=False)
    print("Saved")


def update():
    print("update")


def delete():
    df = list()
    idx = input("line number you want to delete: ")
    cls()
    print(df.iloc[[idx]])
    if click.confirm("Do you want to continue?", default=True):
        print("Do something")
        # df.drop(1)


menu = ConsoleMenu(
    "simple menu options",
    {
        "Table List": list,
        "record add": add,
        "record update": update,
        "record delete": delete,
    },
)

menu.execute()
