import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from dotenv import load_dotenv
import os
import time
import math

load_dotenv()
LOGIN = os.getenv('STEPIC_LOGIN')
PASSWORD = os.getenv('STEPIC_PASSWORD')

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="session")
def hidden_message():
    message = []

    yield message  # возвращаем список во время тестов

    # финализатор: выводим фразу после всех тестов
    if message:
        print("\nСобранное сообщение от инопланетян:")
        print("".join(message))


@pytest.mark.parametrize('link', links)
def test_correct_feedback(browser, link, hidden_message):
    wait = WebDriverWait(browser, 20)
    browser.get(link)

    # Авторизация
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='login']")))
    login_button.click()

    login = wait.until(EC.visibility_of_element_located((By.ID, 'id_login_email')))
    login.send_keys(LOGIN)
    password = browser.find_element(By.ID, 'id_login_password')
    password.send_keys(PASSWORD)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit.click()

    # Ждём поле ответа и вводим логарифм времени
    answer = str(math.log(int(time.time())))
    textarea = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    textarea.clear()
    textarea.send_keys(answer)

    # Кликаем кнопку "Отправить"
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Отправить')]")))
    browser.execute_script("arguments[0].click();", send_button)

    # Ждём фидбека
    try:
        feedback = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        text = feedback.text.strip()
    except StaleElementReferenceException:
        feedback = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        text = feedback.text.strip()

    if text != "Correct!":
        hidden_message.append(text)

    assert text == "Correct!", f"Ожидали 'Correct!', но получили '{text}'"
