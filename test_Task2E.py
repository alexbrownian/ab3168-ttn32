import pytest
from Task2E import run  # Ensure Task2G contains your function that produces a PNG
import pathlib

def test_png_output(tmp_path, monkeypatch):
    """
    Test that run() produces at least one PNG file in the working directory.
    """
    # Change the current working directory to the temporary directory.
    monkeypatch.chdir(tmp_path)
    
    # Run the function that is expected to produce a PNG file.
    run()
    
    # Search for any files with a .png extension in the temporary directory.
    png_files = list(tmp_path.glob("Task2E.png"))
    
    # Assert that at least one PNG file was created.
    assert len(png_files) > 0, "No PNG file was produced by run()."