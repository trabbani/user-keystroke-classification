# import importlib.util
# import inspect
# import os
# from pathlib import Path

# import pytest

# from keystrokes.utils import path_utils


# def test_get_project_root(tmp_path):
#     # The name of the Python file containing the get_project_root function
#     full_path = Path(inspect.getfile(path_utils))

#     # Generate the parts of the directory structure dynamically
#     # Get the parent directory parts of the module's path
#     parent_dirs = full_path.parent.parts[full_path.parent.parts.index('keystrokes'):]

#     # Create a directory structure that mimics your project's structure
#     d = tmp_path
#     for dir in parent_dirs:
#         d = d / dir
#     d.mkdir(parents=True)

#     # Copy the real path_utils.py into the temporary directory structure
#     os.system(f"cp {full_path} {d}")

#     # The expected root directory is tmp_path / "keystrokes"
#     expected_root = tmp_path 

#     # The path to the copied path_utils.py
#     script_path = d / full_path.name

#     # Load the copied module
#     spec = importlib.util.spec_from_file_location("path_utils", script_path)
#     copied_path_utils = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(copied_path_utils)

#     # Call the get_project_root function and check that it returns the expected path
#     assert copied_path_utils.get_project_root() == expected_root


# def test_get_data_path(mocker):
#     """Tests get_data_path method."""
#     mocker.patch(
#         "keystrokes.utils.path_utils.get_project_root", return_value=Path("/root")
#     )
#     assert path_utils.get_data_path("folder") == Path("/root/data/folder")


# def test_get_config(mocker):
#     """Tests get_config method."""
#     mocker.patch(
#         "keystrokes.utils.path_utils.get_project_root", return_value=Path("/root")
#     )
#     mock_open = mocker.mock_open(read_data="key: value")
#     mocker.patch("builtins.open", mock_open)
#     assert path_utils.get_config() == {"key": "value"}


# def test_get_data_raw_folder(mocker):
#     """Tests get_data_raw_folder method."""

#     # Mock function to replace get_data_path
#     def mock_get_data_path(folder_name):
#         return f'data/{folder_name}'

#     mocker.patch("keystrokes.utils.path_utils.get_data_path", side_effect=mock_get_data_path)

#     # Test case when the configuration specifies a raw_folder
#     mocker.patch(
#         "keystrokes.utils.path_utils.get_config",
#         return_value={"raw_folder": "raw_folder"},
#     )
#     assert path_utils.get_data_raw_folder() == "raw_folder"

#     # Test case when the configuration does not specify a raw_folder
#     mocker.patch("keystrokes.utils.path_utils.get_config", return_value={})
#     assert path_utils.get_data_raw_folder() == "data/raw"
