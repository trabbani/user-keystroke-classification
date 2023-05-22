import fnmatch
import zipfile
import csv
import pandas as pd


def read_csv_from_zip(zip_filepath, file_within_zip):
    """
    Read a CSV file from within a zip file into a pandas DataFrame.

    Parameters:
    zip_filepath (str): The path to the zip file.
    file_within_zip (str): The path to the file within the zip file.

    Returns:
    pd.DataFrame: The resulting pandas DataFrame.
    """
    with zipfile.ZipFile(zip_filepath, "r") as zipped_file:
        with zipped_file.open(f"Keystrokes/files/{file_within_zip}") as myfile:
            df = pd.read_csv(myfile, sep="\t", encoding="latin1", on_bad_lines="skip", quoting=csv.QUOTE_NONE)
    return df.drop(columns=["SENTENCE", "USER_INPUT", "KEYSTROKE_ID", "LETTER"])


def list_keystroke_files_in_zip(zip_filepath):
    """
    List all files in a specific directory within a zip file that match a pattern
    and returns a dataframe with filenames and user ids.

    Parameters:
    zip_filepath (str): The path to the zip file.

    Returns:
    pd.DataFrame: A dataframe with filenames and user ids.
    """
    with zipfile.ZipFile(zip_filepath, "r") as zipped_file:
        file_list = fnmatch.filter(
            zipped_file.namelist(), "Keystrokes/files/*_keystrokes.txt"
        )

    # Extract user ids from filenames and create a dataframe
    data = {
        "filename": [file.split("/")[-1] for file in file_list],
        "user_id": [int(file.split("/")[-1].split("_")[0]) for file in file_list],
    }
    df = pd.DataFrame(data)

    # Sort dataframe by user_id
    df.sort_values(by=["user_id"], inplace=True, ignore_index=True)

    return df


def random_rows_in_range(df, N, start, end, exclude):
    """
    Select N random rows from a specific range within the dataframe, excluding the row at the specified index.

    Parameters:
    df (pd.DataFrame): The dataframe to sample from.
    N (int): The number of random rows to select.
    start (int): The start index of the range.
    end (int): The end index of the range.
    exclude (int): The index of the row to exclude.

    Returns:
    pd.DataFrame: A dataframe containing the selected rows.
    """
    df_range = df.loc[start:end]

    if exclude in df_range.index:
        df_range = df_range.drop(exclude)

    return df_range.sample(N)
