from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import time

# Настройка Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://ria.ru/")

# Ожидание полной загрузки страницы
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# Ожидание кнопки "Политика" и клик по ней
politics_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Политика'))
)
politics_button.click()

# Ожидание загрузки страницы с новостями о политике
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))  
)

# Кнопка "Еще 20 материалов"
load_more_button_xpath = "//div[contains(@class, 'list-more') and contains(text(), 'Еще 20 материалов')]"

# Нажимаем на кнопку 5 раз с прокруткой
for _ in range(5):
    # Прокрутка вниз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # Ожидание загрузки новых элементов

    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, load_more_button_xpath))
        )
        load_more_button.click()
        time.sleep(2)  # Ожидание загрузки новых материалов
    except Exception as e:
        print(f"Ошибка при нажатии на кнопку: {e}")
        break

# Получение HTML-кода страницы после загрузки всех материалов
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

articles = []

# Извлечение данных о статьях
for item in soup.find_all('a', class_='list-item__title color-font-hover-only'):
    title = item.text.strip()
    link = item['href']
    articles.append({
        'title': title,
        'link': link
    })

# Закрытие драйвера
driver.quit()

# Сохранение в DataFrame и экспорт в CSV
df = pd.DataFrame(articles)
df.to_csv('politics_news_ria.csv', index=False)

print(f"Найдено статей: {len(articles)}")  # Вывод количества найденных статей
