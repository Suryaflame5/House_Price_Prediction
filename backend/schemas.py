from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class PredictionInput(BaseModel):
    SquareFootage: float = 2500
    Bedrooms: int = 3
    Bathrooms: float = 2.5
    YearBuilt: int = 2000
    NeighborhoodQuality: int = 7
    DistanceToCenter: float = 10.0

class PredictionResponse(BaseModel):
    success: bool
    prediction: Any
    latency_ms: float

class HistoryLog(BaseModel):
    id: int
    timestamp: str
    input_data: Dict[str, Any]
    prediction: Any
    latency_ms: float
