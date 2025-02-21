import io
from contextlib import redirect_stdout
from Task2C import run  # Make sure Task2C has the run() function

def test_task2c_output_is_string():
    # Create a StringIO object to capture output
    output_capture = io.StringIO()
    
    # Redirect stdout to the StringIO object while running run()
    with redirect_stdout(output_capture):
        run()
    
    # Retrieve the output as a string
    output = output_capture.getvalue().strip()
    
    # Check that the output is a non-empty string
    assert isinstance(output, str), "Output should be a string."
    assert output != "", "Output should not be empty."
    
# Another approach could be to count the number of stations in the output to make sure there are 10 stations. 