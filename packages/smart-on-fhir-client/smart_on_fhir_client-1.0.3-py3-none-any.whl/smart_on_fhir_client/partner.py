import abc
import dataclasses
import enum
from typing import Any

from loguru import logger
from pydantic import BaseModel

from smart_on_fhir_client.strategy import Strategy, StrategyNotFound


@dataclasses.dataclass
class TokenEndpointResponse:
    access_token: str | None = None
    refresh_token: str | None = None
    id_token: str | None = None


class Partner(BaseModel, abc.ABC):
    """Base client"""

    name: str
    supported_strategies: set[Strategy]
    client_id: str | None
    client_secret: str | None
    token_url: str | None
    authorize_url: str | None
    fhir_url: str | None

    async def get_access_token_for_strategy(
        self, strategy: Strategy, **kwargs: Any
    ) -> TokenEndpointResponse:
        if strategy not in self.supported_strategies:
            logger.info(f"{strategy=} is not supported for partner {self.name=}")
            raise StrategyNotFound("Strategy not found")

        # enumerate here all strategies...
        if strategy is Strategy.M2M:
            return await self.get_access_token_for_m2m(**kwargs)
        if strategy is Strategy.AUTHORIZATION_CODE:
            return await self.get_access_token_for_authorization_code(**kwargs)

        raise StrategyNotFound("Strategy not found")

    def attrs(self, *attr_name):
        return dict([(name, getattr(self, name)) for name in attr_name])

    async def get_access_token_for_authorization_code(
        self, **kwargs: Any
    ) -> TokenEndpointResponse:
        """

        Args:
            code:

        Returns:

        """
        ...

    async def get_access_token_for_m2m(self, **kwargs: Any) -> TokenEndpointResponse:
        """

        Args:
            **kwargs:

        Returns: tuple[str, str] pair of access and refresh tokens

        """
        ...

    async def trade_refresh_token_for_access_token(self, refresh_token: str):
        ...


class TargetUrlStrategy(enum.Enum):
    NONE = enum.auto()
    PARTNER = enum.auto()
    ORGANIZATION_NAME = enum.auto()
    CUSTOM = enum.auto()


class Organization:
    def __init__(
        self,
        name: str,
        target_url_strategy: TargetUrlStrategy = TargetUrlStrategy.PARTNER,
        **kwargs,
    ):
        """

        Args:
            name: str name of the organization or practitioner *must be unique*
            target_url_strategy: TargetUrlStrategy strategy used to determine the tenant on which the data is sent
            **kwargs: Any
        """
        self.name = name
        self.target_url_strategy = target_url_strategy
        self.parameters = kwargs

    @property
    def slug(self):
        return self.name.replace(" ", "-").replace("/", "").upper()


# alias on organization
Practitioner = Organization
