import asyncio
import aiohttp
from pyllector.models import HttpMethod, ContentType

class ApiCollector(aiohttp.ClientSession):
    def __init__(self, main_api_link: str, main_params: dict = None, main_cookie: dict = None, **kwargs):
        super().__init__(cookies=main_cookie, **kwargs)
        self.main_api_link = self._right_main_link(main_api_link)
        self.main_api_params = main_params
    
    def _pull_params_together(self, params: dict = None) -> dict:
        return {**self.main_api_params,  **params} if params is not None else self.main_api_params
    
    def _right_main_link(self, main_link):
        return main_link if main_link[-1] == '/' else f'{main_link}/'
    
    async def push(self, method: str = '', content_type: ContentType = ContentType.TEXT,
                   http_method: HttpMethod = HttpMethod.GET,
                   params: dict = None, limit: int = 5,
                   time: float = 60, check_key: str = None, **kwargs) -> dict | str | None:
        
        if limit == 0:
            print('Failed get this url. Tries is over')
            return None
        
        params = self._pull_params_together(params)
        async with self.request(http_method.value, f'{self.main_api_link}{method}', params=params, **kwargs) as response:
            print(response.url, response.status)
            if response.status != 400:
                if self._is_valid_response(response):
                    if content_type == ContentType.TEXT:
                        return await response.text()
                    if content_type == ContentType.JSON:
                        response = await response.json()
                        if check_key != None:
                            try:
                                if response[check_key]:
                                    return response
                            except KeyError:
                                print('Key is failed!! I`ll try again.')
                                return await self.push(method, content_type, limit=limit-1, **kwargs)
                        return response
                else:
                    if response.status != 429:
                        print(f'Failed get it url. Status code {response.status}. URL {response.url}')
                    else:
                        print(f'429 Http code. Repeat request again across {time} seconds.')
                        await asyncio.sleep(time)
                    return await self.push(method, content_type, limit=limit-1, **kwargs)
            else:
                print('Bad Request', response.url)
                return None
            
    def _is_valid_response(self, request) -> bool:
        return True if request.status == 200 else False
        

    
