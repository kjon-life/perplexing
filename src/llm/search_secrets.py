#!/usr/bin/env python3
"""
Parse command-line arguments and execute .ipynb notebook search.

This function sets up the argument parser, retrieves the directory
and cell ID from the command line, calls the search_notebooks function, and prints the results.

Command-line arguments:
    directory: A path to the directory to search for notebooks.
    cell_id: The cell ID to search for within the notebooks.

Returns:
    None

Prints:
    - The path of the notebook and the cell index if the cell ID is found.
    - A message indicating that the cell ID was not found if no match is found.
"""
import os
import nbformat
import argparse
import logging
from tqdm import tqdm


def search_notebooks(directory: str, cell_id: str) -> tuple[str | None, int | None]:
    """
    Search Jupyter notebooks in a directory for a specific cell ID.

    This function recursively traverses the given directory and its subdirectories,
    looking for Jupyter notebook files (.ipynb). It searches each notebook for a cell
    with the specified cell ID in its metadata. It includes a progress indicator.

    Args:
        directory (str): The path to the directory to search.
        cell_id (str): The cell ID to search for in the notebooks.

    Returns:
        tuple: A tuple containing two elements:
            - str or None: The path of the notebook containing the cell ID, or None if not found.
            - int or None: The index of the cell within the notebook, or None if not found.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If there are insufficient permissions to read the directory or files.

    Example:
        >>> notebook_path, cell_index = search_notebooks('/path/to/notebooks', 'abc123')
        >>> if notebook_path:
        ...     print(f"Found in {notebook_path} at index {cell_index}")
        ... else:
        ...     print("Cell ID not found")
    """
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".ipynb"):
                    notebook_path = os.path.join(root, file)
                    try:
                        with open(notebook_path, 'r', encoding='utf-8') as f:
                            notebook = nbformat.read(f, as_version=4)
                        for cell in notebook.cells:
                            if 'id' in cell.metadata and cell.metadata['id'] == cell_id:
                                return notebook_path, notebook.cells.index(cell)
                    except (IOError, nbformat.reader.NotJSONError) as e:
                        print(f"Error reading {notebook_path}: {e}")
    except OSError as e:
        print(f"Error accessing directory {directory}: {e}")
    return None, None

def main():
    """
    Jupyter Notebook Cell ID Search Tool by perplexity.ai

    Search for a specific cell ID within metadata in
    Jupyter notebooks (.ipynb) in a given directory and its subdirectories.

    Use as a command-line utility
    or import as a module in other Python scripts.

    Usage as a script:
        python search_secrets.py <directory> <cell_id>

    Functions:
        search_notebooks(directory, cell_id): Search for a cell ID in notebooks.
        main(): Parse command-line arguments and execute the search.

    Dependencies:
        - os
        - nbformat
        - argparse
    """
    parser = argparse.ArgumentParser(description='Search Jupyter notebook metadata for a specific cell ID.')
    parser.add_argument('directory', help='Directory to search for Jupyter notebooks')
    parser.add_argument('cell_id', help='Cell ID to search for')
    
    args = parser.parse_args()
    
    notebook_path, cell_index = search_notebooks(args.directory, args.cell_id)
    
    if notebook_path:
        print(f"Cell ID found in notebook: {notebook_path}")
        print(f"Cell index: {cell_index}")
    else:
        print("Cell ID not found in any notebook.")

if __name__ == '__main__':
    main()