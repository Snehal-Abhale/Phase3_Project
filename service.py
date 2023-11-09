from Phase3_Project.clients.marketaux import MarketAux
from Phase3_Project.clients.msfinance import MsFinance

class ServiceWorkflow:

    def __init__(self) -> None:
        pass

    def run(self):
        marketaux_client = MarketAux()
        marketaux_client.get_news()

        msfinance_client = MsFinance()
        msfinance_client.getListOfNewsArticles()
        msfinance_client.getDetailsOfNewsArticles()
