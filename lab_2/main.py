import pandas as pd

from services.get_data import get_country_data


data_type = "score"


def print_best_countries(df, rank_or_score, columns):
    df = df.copy()
    df["mean"] = df[columns].mean(axis=1)
    df.sort_values(by="mean", ascending=rank_or_score == "rank", inplace=True)

    print(df[["country", *columns]].head(10))


def task_1(df):
    df = df.copy()
    df["Economic"] = df[
        [
            "Investment Environment",
            "Enterprise Conditions",
            "Infrastructure & Market Access",
            "Economic Quality",
        ]
    ].mean(axis=1)

    columns = [
        "Safety & Security",
        "Social Capital",
        "Economic",
        "Health",
        "Education",
    ]

    print_best_countries(
        df,
        data_type,
        columns,
    )


def task_2(df):
    df = df.copy()

    columns = [
        "Safety & Security",
        "Social Capital",
        "Investment Environment",
        "Economic Quality",
        "Health",
    ]

    print_best_countries(
        df,
        data_type,
        columns,
    )


def task_3(df):
    df = df.copy()

    columns = [
        "Safety & Security",
        "Personal Freedom",
        "Health",
        "Living Conditions",
        "Natural Environment",
    ]

    print_best_countries(
        df,
        data_type,
        columns,
    )


def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)

    df = get_country_data(data_type, use_full_columns_names=True)
    [
        "Safety & Security",
        "Personal Freedom",
        "Governance",
        "Social Capital",
        "Investment Environment",
        "Enterprise Conditions",
        "Infrastructure & Market Access",
        "Economic Quality",
        "Living Conditions",
        "Health",
        "Education",
        "Natural Environment",
    ]

    print()
    task_1(df)
    print()
    task_2(df)
    print()
    task_3(df)


if __name__ == "__main__":
    main()
