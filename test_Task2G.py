import pytest
from Task2G import assess_flood_risk

def test_assess_flood_risk_output(capsys):
    """
    Test that assess_flood_risk() produces a non-empty string output.
    """
    # Run the function (which prints the results)
    assess_flood_risk()
    
    # Capture the output from stdout
    captured = capsys.readouterr()
    output = captured.out.strip()
    
    # Assert that the output is a string
    assert isinstance(output, str), "The output should be a string."
    
    # Assert that the output is not empty
    assert output != "", "The function should produce some output."
    
    # Optionally, you could check that the output contains expected keywords:
    assert "risk" in output.lower(), "Expected output to mention 'risk'."