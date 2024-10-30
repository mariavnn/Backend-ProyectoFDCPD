from scraper_utils import get_news_articles # Importa la función de scraping


def main():
   new_data = get_news_articles()
   
   for news in new_data:
    print(news)
    
if __name__ == "__main__":
    main()
