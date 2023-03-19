from datetime import datetime
from tech_news.database import search_news


# Requisito 7


def search_by_title(title):
    data_news = search_news({"title": {"$regex": title, "$options": "$i"}})
    return [(new["title"], new["url"]) for new in data_news]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data_news = search_news({"timestamp": date})
        return [(new["title"], new["url"]) for new in data_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
