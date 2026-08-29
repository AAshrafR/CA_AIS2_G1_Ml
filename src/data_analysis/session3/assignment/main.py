from config import DATA_FILE_PATH, COLS_TO_DROP
from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)


def main() -> None:
    '''Run the preprocessing pipeline.'''

    # Read dataset
    try: 
        df = Read_data_file(DATA_FILE_PATH)

        print("\nDataset loaded successfully!")
        print(f"Shape: {df.shape}")

    except (FileNotFoundError, ValueError, RuntimeError) as error:
        print(f"\nError: {error}")
        return

    # Check original data
    print("\n \t\t_____ORIGINAL DATA______")
    print(df.head())

    print("\n \t\t______DATA TYPE REPORT______")
    print(Check_data_type(df))

    # Ask user whether to drop unnecessary features
    choice = input(
        "\nDo you want to remove unnecessary features? (y/n): "
    ).strip().lower()

    if choice == "y":

        print("\nColumns configured for removal:")
        print(COLS_TO_DROP)

        df = Drop_unnecessary_features(
            df,
            COLS_TO_DROP
        )

        print("\n \t\t_______AFTER REMOVING FEATURES_______")
        print(df.head())

        print(f"\nNew shape: {df.shape}")

        print("\n \t\t______UPDATED DATA TYPE REPORT______")
        print(Check_data_type(df))

    else:
        print("\nNo features were removed.")


if __name__ == "__main__":
    main()