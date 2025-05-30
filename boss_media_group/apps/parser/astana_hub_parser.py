from bs4 import BeautifulSoup
import requests
from logger import logger


def fetch_astana_hub_html():
    url = 'https://astanahub.com/ru/service/techpark/'
    logger.info(f'Парсер запущен: {url}')

    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.debug('Успешно получили HTML-страницу от astanahub')
        return response.content
    except requests.RequestException as e:
        logger.error(f'Ошибка при запросе к {url}: {e}')
        return None


def parse_astana_hub_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('tbody > tr')[:10]

    if not rows:
        logger.warning('Не найдено ни одной строки в таблице на astanahub')

    company_names = []
    for i, row in enumerate(rows):
        tds = row.find_all('td')
        if len(tds) >= 6:
            name = tds[5].get_text(strip=True)
            logger.debug(f'{i + 1}. Найдено название компании: {name}')
            company_names.append(name)
        else:
            logger.warning(f'{i + 1}. Недостаточно колонок в строке: {tds}')

    return company_names


def astana_hub_parser() -> list[str]:
    html = fetch_astana_hub_html()
    if not html:
        return []

    result = parse_astana_hub_html(html)
    logger.info(f'Парсер завершён. Найдено компаний: {len(result)}')
    return result
