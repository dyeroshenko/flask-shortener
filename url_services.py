import re
from datetime import datetime

from database import Database

class UrlServices:
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def check_is_valid_url(self, url: str) -> bool:
        filter = re.fullmatch(r'^https?://(www.)?\S*', url)
        return bool(filter)

    def check_if_duplicate(self, url: str) -> bool:
        with Database('url.db') as cursor:
            _SQL = "SELECT full_url FROM urls"
            cursor.execute(_SQL)
            saved_urls = cursor.fetchall()

        for saved_url in saved_urls:
            if url == saved_url[0]:
                return True
        
        return False

    def get_domain(self, url: str) -> str:
        filter = re.fullmatch(r'^https?://(www.)?(\S*?)\/\S*$', url)
        domain = filter.group(2)

        return domain