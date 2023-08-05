import requests
import pandas as pd
import numpy as np


def get_ip():
    r = requests.get("https://api.ipify.org?format=json")
    data = r.json()
    return data["ip"]


def get_normal_df(no_normals=2, normal_size=100):
    d = {}

    for i in range(no_normals):
        d["dist{}".format(i+1)] = np.random.normal(size=100)

    df = pd.DataFrame.from_dict(d)


    print(df)


if __name__ == "__main__":
    print(get_ip())
    print(get_normal_df())
