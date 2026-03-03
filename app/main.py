import pandas as pd
from modules.mon_module import print_data


def main():
    """Load CSV data and print it to the console."""
    df = pd.read_csv("app/moncsv.csv")
    print_data(df)



if __name__ == "__main__":
    main()
