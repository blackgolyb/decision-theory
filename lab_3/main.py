import pandas as pd
import matplotlib.pyplot as plt

from services.get_data import get_country_data


data_type = "score"


def count_best_solutions(df):
    results = []
    for i in df.index:
        current_item = df.iloc[i]

        if not results:
            results.append(i)
            continue

        for j in range(len(results)):
            check_id = results[j]
            check_item = df.iloc[check_id]

            if all(current_item >= check_item):
                results[j] = i
            elif any(current_item >= check_item):
                results.append(i)

        results = list(set(results))

    for k in range(len(results)):
        current_item = df.iloc[results[k]]
        for j in range(len(results)):
            check_id = results[j]
            check_item = df.iloc[check_id]

            if all(current_item >= check_item):
                results[j] = results[k]

    results = list(set(results))

    return results


def plot_with_names(ax, df, col1, col2, col3=None):
    if col3 is None:
        ax.scatter(df[col1], df[col2])
    else:
        ax.scatter(df[col1], df[col2], df[col3])

    if col3 is None:
        for i in df.index:
            pos = (df[col1][i], df[col2][i])
            ax.annotate(df["country"][i], pos, zorder=1, ha="center")
    else:
        for i in df.index:
            pos = (df[col1][i], df[col2][i], df[col3][i])
            ax.text(*pos, df["country"][i], zorder=1, ha="center")

    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    if col3 is not None:
        ax.set_zlabel(col3)


def print_best_solutions(df, columns):
    df = df.copy()

    df = df[["country", *columns]]
    count_df = df[columns]

    results = count_best_solutions(count_df)
    print(df.iloc[results])
    result_df = df.iloc[results]

    if len(columns) == 2:
        fig = plt.figure()
        ax = fig.add_subplot()
        plot_with_names(ax, result_df, columns[0], columns[1])
        plt.show()
    if len(columns) == 3:
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax3d = fig.add_subplot(2, 2, 4, projection="3d")

        plot_with_names(ax1, result_df, columns[0], columns[1])
        plot_with_names(ax2, result_df, columns[0], columns[2])
        plot_with_names(ax3, result_df, columns[1], columns[2])
        plot_with_names(ax3d, result_df, columns[0], columns[1], columns[2])

        plt.show()


def task_test():
    df = pd.DataFrame(
        {
            "country": [1, 2, 3, 4, 5, 6],
            "y1": [1, 2, 4, 4, 1, 2],
            "y2": [4, 4, 2, 1, 1, 4],
        }
    )

    columns = [
        "y1",
        "y2",
    ]

    print_best_solutions(df, columns)


def task1(df):
    df = df.copy()

    columns = [
        "Safety & Security",
        "Health",
    ]

    print_best_solutions(df, columns)


def task2(df):
    df = df.copy()

    columns = [
        "Safety & Security",
        "Investment Environment",
        "Health",
    ]

    print_best_solutions(df, columns)


def task3(df):
    df = df.copy()

    columns = [
        "Safety & Security",
        "Social Capital",
        "Investment Environment",
        "Economic Quality",
        "Health",
    ]

    print_best_solutions(df, columns)


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

    task1(df)

    task2(df)

    task3(df)


if __name__ == "__main__":
    main()
