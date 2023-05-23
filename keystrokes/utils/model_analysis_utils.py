import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

from keystrokes.utils.keyboard_utils import keycode_to_key


def calculate_shap_values(model, X):
    def parse_index(index_str):
        parts = index_str.split("_")
        first_keycode = keycode_to_key(int(parts[1]))
        second_keycode = keycode_to_key(int(parts[2]))
        feature_type = "PRESS" if "PRESS" in index_str else "HOLD"
        return first_keycode, second_keycode, feature_type

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    if isinstance(shap_values, list):
        shap_values = np.array(shap_values)

    mean_abs_shap_values = pd.Series(
        np.abs(shap_values).mean(axis=0), index=X.columns
    ).sort_values(ascending=False)

    df = pd.DataFrame(mean_abs_shap_values).reset_index()
    df.columns = ["index", "shap_value"]

    df[["first_keycode", "second_keycode", "feature_type"]] = df["index"].apply(
        lambda x: pd.Series(parse_index(x))
    )

    df = df[["first_keycode", "second_keycode", "feature_type", "shap_value"]]

    return df


def plot_feature_importance(df):
    """
    Plots the feature importance for a given DataFrame.

    Args:
    df (DataFrame): DataFrame containing feature importance.

    Returns:
    None
    """

    # Combine the first three columns into one column
    df["feature"] = (
        df["first_keycode"] + "_" + df["second_keycode"] + "_" + df["feature_type"]
    )

    # Sort the dataframe by shap_value in descending order
    df = df.sort_values(by="shap_value", ascending=False)

    # Plot the feature importance
    plt.figure(figsize=(10, 16))
    plt.barh(df["feature"], df["shap_value"], color="skyblue")
    plt.xlabel("SHAP Value")
    plt.ylabel("Feature")
    plt.title("Feature Importance")
    plt.gca().invert_yaxis()  # To display the most important feature at the top
    plt.show()
