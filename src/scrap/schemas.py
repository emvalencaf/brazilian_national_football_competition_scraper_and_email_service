from pydantic import BaseModel, EmailStr, field_validator
from typing import List

class CompetitionID(BaseModel):
    id: str
    season: int

class RequestEmail(BaseModel):
    seasons: List[int]
    email: EmailStr
    
    @classmethod
    @field_validator('seasons')
    def validate_seasons(cls, v: List[int]) -> List[int]:
        """Validate that each season is between 1998 and 2024."""
        invalid_seasons = [season for season in v if season < 1998 or season > 2024]
        if invalid_seasons:
            raise ValueError(f"Seasons must be between 1998 and 2024. Invalid seasons found: {invalid_seasons}")
        return v