from pydantic import BaseModel
from typing import List, Optional, Union


class DeliveryItem(BaseModel):
    delivery_id: Optional[str] = None
    code: Optional[str] = None
    finished_at: Optional[str] = None  


class DeliverySummary(BaseModel):
    date: Optional[str] = None
    distance_km: Optional[float] = None
    deliveries: Optional[ int] = None
    tips_kd: Optional[float] = None
    collected_kd: Optional[ float] = None
    delivery_items: Optional[List[DeliveryItem]] = None
