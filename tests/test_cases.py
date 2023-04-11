import pytest
from app.functions import *

@pytest.mark.parametrize('case, height, weight', [(1, 0, 150), (2, .1, 1), (3, 2, 0), (4, 1, .1), (5, 63, 125)])
def test_bmiCalculator(case, height, weight):
    # ON lower height
    if case == 1:
        assert bmiCalculator(height, weight) == 0.0
    # OFF lower height
    elif case == 2:
        assert bmiCalculator(height, weight) == 72000.0
    # ON lower weight
    elif case == 3:
        assert bmiCalculator(height, weight) == 0.0
    # OFF lower weight
    elif case == 4:
        assert bmiCalculator(height, weight) == 72.0
    # int
    elif case == 5:
        assert bmiCalculator(height, weight) == 22.7
    
@pytest.mark.parametrize('case, bmi', [(1, 0.0), (2, 0.1), (3, 11.0), (4, 18.4), (5, 18.5), (6, 22.0), (7, 24.9), (8, 25.0), (9, 27.0), (10, 29.9), (11, 30.0), (12, 40.0)])
def test_categorize(case, bmi):
    # ON lower UW
    if case == 1:
        assert categorize(bmi) == "Error"
    # OFF lower UW
    if case == 2:
        assert categorize(bmi) == "Underweight"
    # int UW
    if case == 3:
        assert categorize(bmi) == "Underweight"
    # OFF upper UW and lower NW
    if case == 4:
        assert categorize(bmi) == "Underweight"
    # ON lower NW
    if case == 5:
        assert categorize(bmi) == "Normal weight"
    # int NW
    if case == 6:
        assert categorize(bmi) == "Normal weight"
    # OFF upper NW and lower OW
    if case == 7:
        assert categorize(bmi) == "Normal weight"
    # ON lower OW
    if case == 8:
        assert categorize(bmi) == "Overweight"
    # int OW
    if case == 9:
        assert categorize(bmi) == "Overweight"
    # OFF upper OW and lower Obese
    if case == 10:
        assert categorize(bmi) == "Overweight"
    # ON Obese
    if case == 11:
        assert categorize(bmi) == "Obese"
    # int Obese
    if case == 12:
        assert categorize(bmi) == "Obese"
