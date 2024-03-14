import requests
from bs4 import BeautifulSoup

# A class to hold the essential features for dark web monitoring
class DarkWebMonitor:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url
    
    # Connects to a Tor network to anonymize the requests.
    def connect_to_tor(self):
        self.session.proxies = {
            'http': 'socks5h://localhost:9050',
            'https': 'socks5h://localhost:9050'
        }
    
    def search(self, term):
        '''
        This method searches the dark web for the provided term.
        It returns the found contents if any.
        '''
        try:
            # Construct the search URL
            search_url = f'{self.base_url}/search?query={term}'
            
            # Make a request to the dark web using the onion URL
            response = self.session.get(search_url)
            response.raise_for_status()
            
            # Use BeautifulSoup to parse the HTML page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract and return the contents
            contents = soup.find_all('div', {'class': 'content'})
            return [content.text for content in contents]
        except requests.RequestException as e:
            print(f'Error while searching: {e}')
            return []
    
    def monitor(self, terms):
        '''
        This method monitors the dark web for a list of terms.
        It returns a dictionary with the terms as keys and the results as values.
        '''
        results = {}
        for term in terms:
            results[term] = self.search(term)
        return results

# Usage of the DarkWebMonitor class
if __name__ == '__main__':
    monitor = DarkWebMonitor('http://hss3uro2hsxfogfq.onion') # This is a fake URL used for demonstration purposes.
    monitor.connect_to_tor()
    terms_to_monitor = ['credit card', 'identity theft', 'exploit']
    findings = monitor.monitor(terms_to_monitor)
    
    for term, content in findings.items():
        print(f'Search term: {term}{'='*len(term)}')

        for snippet in content:
            print(snippet, '')
        print('')