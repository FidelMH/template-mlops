import pandas as pd
from modules.mon_module import print_data


def main():
    df = pd.read_csv("app/moncsv.csv")
    print_data(df)



if __name__ == "__main__":
    main()
