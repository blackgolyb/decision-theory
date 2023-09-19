import requests
import json
import pandas as pd

data_url = "https://prosperity.com/tools/statistics/data"


def get_country_data(rank_or_score, use_full_columns_names=False, get_addons=False):
    if rank_or_score == "rank":
        is_rank_prefix = "rank_"
    elif rank_or_score == "score":
        is_rank_prefix = ""
    else:
        raise ValueError("rank_or_score can be only: rank or score")

    response = requests.get(data_url)
    json_response = response.json()

    with open("data.json", "w") as f:
        f.write(json.dumps(json_response))
    input_df = pd.DataFrame.from_dict(json_response["children"])

    df = pd.DataFrame()

    row_columns = json_response["sub_indexes"]

    columns = list(row_columns.keys())
    input_columns = list(map(lambda x: f"{is_rank_prefix}{x}", columns))

    if use_full_columns_names:
        columns = list(
            map(lambda x: json_response["sub_indexes"][x], json_response["sub_indexes"])
        )

    columns.insert(0, "country")
    input_columns.insert(0, "country")

    df[columns] = input_df[input_columns]

    if not get_addons:
        return df

    addons = pd.DataFrame()
    addons_columns = [
        "country",
        "image",
        "url",
        "year",
    ]
    addons[addons_columns] = input_df[addons_columns]

    return (df, addons)
