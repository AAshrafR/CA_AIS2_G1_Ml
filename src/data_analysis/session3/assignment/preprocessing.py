import pandas as pd


def Read_data_file(file_path: str) -> pd.DataFrame:
    '''
    Read a CSV dataset and return it as a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the provided path is invalid or the file is empty.
        RuntimeError: If the file cannot be read.

    Example:
        df = Read_data_file("data/titanic.csv")
    '''

    if not file_path or not isinstance(file_path, str):
        raise ValueError("Invalid file path. Please provide a valid path.")

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("The file was read successfully, but it is empty.")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"The file was not found: {file_path}"
        )

    except pd.errors.EmptyDataError:
        raise ValueError(
            f"The file is empty: {file_path}"
        )

    except pd.errors.ParserError:
        raise RuntimeError(
            f"Unable to parse the CSV file: {file_path}"
        )

    except OSError:
        raise RuntimeError(
            f"The file could not be read: {file_path}"
        )


def Drop_unnecessary_features(
    df: pd.DataFrame,
    cols_to_drop: list[str]
) -> pd.DataFrame:
    '''
    Remove unnecessary columns from a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        cols_to_drop (list[str]): List of column names to remove.

    Returns:
        pd.DataFrame: DataFrame after removing the specified columns.

    Example:
        df = Drop_unnecessary_features(df,["PassengerId", "Name"])
    '''

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")

    if not isinstance(cols_to_drop, list):
        raise TypeError("cols_to_drop must be a list.")

    missing_columns = [
        column for column in cols_to_drop
        if column not in df.columns
    ]

    if missing_columns:
        print(
            f"Warning: These columns were not found: "
            f"{missing_columns}"
        )

    existing_columns = [
        column for column in cols_to_drop
        if column in df.columns
    ]

    return df.drop(columns=existing_columns)


def Check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Create a data-quality report for the DataFrame.

    The report contains:
        - Column name
        - Data type
        - Number of unique values

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transposed data-quality report.

    Example:
        report = Check_data_type(df)
        print(report)
    '''

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")

    report = pd.DataFrame({
        "Column_Name": df.columns,
        "Data_Type": df.dtypes.astype(str).values,
        "Unique Values": df.nunique().values
    })

    return report.set_index("Column_Name").T