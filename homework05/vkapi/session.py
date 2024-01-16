import typing as tp
import time

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Session:
    """
    Сессия.

    :param base_url: Базовый адрес, на который будут выполняться запросы.
    :param timeout: Максимальное время ожидания ответа от сервера.
    :param max_retries: Максимальное число повторных запросов.
    :param backoff_factor: Коэффициент экспоненциального нарастания задержки.
    """

    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
    ) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.session = requests.Session()

    def get(self, method: str, **kwargs: tp.Any) -> requests.Response:
        resp = self.session.get(f"{self.base_url}/{method}", params=kwargs)
        return resp

    def post(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
        response = self.session.post(f"{self.base_url}/{url}", data=kwargs, timeout=self.timeout)
        return response