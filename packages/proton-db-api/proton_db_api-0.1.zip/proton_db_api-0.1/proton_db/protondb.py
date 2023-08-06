from dacite import from_dict

from .classes import Game
from .requestable import Requestable

SEARCH_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.protondb.com',
    'Referer': 'https://www.protondb.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-algolia-api-key': '9ba0e69fb2974316cdaec8f5f257088f',
    'x-algolia-application-id': '94HE6YATEI',
}

SEARCH_DATA = '{"query":"%game_name","attributesToHighlight":"","attributesToSnippet":"","facets":"tags","facetFilters":"appType:Game","hitsPerPage":50,"attributesToRetrieve":"lastUpdated,name,objectID,followers,oslist,releaseYear,tags,technologies,userScore","page":0}'
SEARCH_BY_ID_DATA = '{"query":"","attributesToHighlight":[],"attributesToSnippet":[],"facets":["tags"],"facetFilters":[["appType:Game"]],"hitsPerPage":100,"attributesToRetrieve":["lastUpdated","name","objectID","followers","oslist","releaseYear","tags","technologies","userScore"],"filters":"(objectID:%game_id)"}'


SEARCH_LINK = "https://94he6yatei-dsn.algolia.net"
SEARCH_METHOD = "1/indexes/steamdb/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.13.0)%3B%20Browser"

class ProtonDB(Requestable):
    def __init__(self):
        super().__init__("https://www.protondb.com")
        self.search_engine = Requestable(SEARCH_LINK, SEARCH_HEADERS)

    async def get_game(self, game_id: int):
        r = await self.get_json(f"proxy/steam/api/appdetails/", parameters={"appids": game_id})
        data = r[str(game_id)]["data"]
        return from_dict(Game, data)

    async def get_proton_db_game_dict(self, game_id):
        r = await self.search_engine.get_json(SEARCH_METHOD, "POST", data=SEARCH_BY_ID_DATA.replace("%game_id", str(game_id)))
        return r["hits"][0]

    async def get_ids_from_name(self, name: str) -> list[int]:
        r = await self.search_engine.get_json(SEARCH_METHOD, method="POST", data=SEARCH_DATA.replace("%game_name",name))
        return [int(hit["objectID"]) for hit in r["hits"]]

    async def get_game_from_name(self, name: str):
        return await self.get_game((await self.get_ids_from_name(name))[0])

    async def get_game_tier(self, game_id: int) -> str:
        r = await self.get_json(f"api/v1/reports/summaries/{game_id}.json")
        return r.get("tier", "pending")
