import io
from contextlib import redirect_stdout
from Task2B import run  

def test_task2b_output_is_string():
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
    
# Another approach could be to check if the output has been sorted, but since we used Python's built-in sort function, this is not really necessary. 