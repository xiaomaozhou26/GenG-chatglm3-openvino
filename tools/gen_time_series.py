import abc
from typing import Type
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from timeseries_generator.base_factor import BaseFactor
from timeseries_generator.errors import FactorAlreadyExistsError, DuplicateNameError

class Generator:
    def __init__(
        self,
        factors: Set[BaseFactor],
        features: Optional[Dict[str, List[str]]] = None,
        date_range: pd.DatetimeIndex = None,
        base_value: float = 1.0,
    ):
        """
        Collects relevant features and creates a resulting DataFrame based on the selected features.

        Args:
            factors: factors that will be applied to the timeseries.
            features: features that will be taken into account in the timeseries generation.
            date_range: daterange of the resulting dataframe.
            base_value: base value of the resulting value of the time series. Mainly useful to give a correct order of
                magnitude to your resulting data.
        """
        if features is None:
            features = {}
        if date_range is None:
            pd.date_range(pd.datetime(1970, 1, 1), periods=50),
        self._factors = factors
        self._features = features
        self._base_value = base_value
        self._date_range = date_range
        self._ts = None

    @property
    def factors(self):
        return self._factors

class GetTSInput(BaseModel):
    instruction: str = Field(description="instruction")

class GetTS(BaseTool):
    name = "GetTS"
    description = "generate a sequence of time series data based on the instruction"
    args_schema: Type[BaseModel] = GetTSInput

    def __init__(self):
        super().__init__()

    def _run(self, date: str, number: str) -> str:
        all_price = {
            "8321":{
                "2024-03-23" : "1154",
                "2024-03-24" : "1381",
            },
            "1234":{
                "2024-03-23" : "1393",
                "2024-03-24" : "2123",
            }
        }
        return all_price[number][date]
        
