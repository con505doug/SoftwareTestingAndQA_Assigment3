import pytest
from functions import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from app import create_app
from flask.testing import FlaskClient

url = "http://127.0.0.1:5000"

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

@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as test_client:
        yield test_client


def test_page(test_client: FlaskClient):
    response = test_client.get('/')
    assert response.status_code == 200


def test_form_fillout(test_client: FlaskClient):
    response = test_client.post('/', data={
        'feet': '6',
        'inches': '5',
        'weight':'160'})
    assert response.status_code == 200

def test_form_fillout2(test_client: FlaskClient):
    response = test_client.post('/', data={
        'feet': '0',
        'inches': '0',
        'weight':'160'})
    assert response.status_code == 200

def test_form(driver):
    driver.get('http://127.0.0.1:5000')
    feet = driver.find_element(By.ID, 'feet')
    feet.send_keys('5')
    inches = driver.find_element(By.ID, 'inches')
    inches.send_keys('3')
    weight = driver.find_element(By.ID, 'weight')
    weight.send_keys('125')
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    bmi = driver.find_element(By.ID, 'bmi')
    assert bmi.text == 'BMI: 22.7'

def test_form2(driver):
    driver.get('http://127.0.0.1:5000')
    feet = driver.find_element(By.ID, 'feet')
    feet.send_keys('-1')
    inches = driver.find_element(By.ID, 'inches')
    inches.send_keys('3')
    weight = driver.find_element(By.ID, 'weight')
    weight.send_keys('125')
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    error = driver.find_element(By.XPATH, "//span[(text()='[Number must be at least 0.]')]")
    assert error.text == '[Number must be at least 0.]'

def test_form3(driver):
    driver.get('http://127.0.0.1:5000')
    feet = driver.find_element(By.ID, 'feet')
    feet.send_keys('0')
    inches = driver.find_element(By.ID, 'inches')
    inches.send_keys('0')
    weight = driver.find_element(By.ID, 'weight')
    weight.send_keys('125')
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    error = driver.find_element(By.XPATH, "//span[(text()='Total height must be greater than 0 inches')]")
    assert error.text == 'Total height must be greater than 0 inches'


