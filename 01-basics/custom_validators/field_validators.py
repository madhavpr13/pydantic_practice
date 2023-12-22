from pydantic import BaseModel, Field, ValidationError
from pydantic import ValidationInfo
from pydantic import field_validator
from datetime import datetime
from dateutil.parser import parse as parse_date


class Event(BaseModel):
    event_id: int | None = None
    event_name: str | None = None
    event_organizer: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    location: str | None = None
    max_participants: int = Field(default=3)
    participants: list[str] = Field(default_factory=list)

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def validate_dates(cls, value: str) -> datetime:
        parsed_date = parse_date(value)
        return parsed_date

    @field_validator("end_date", mode="after")
    @classmethod
    def validate_end_date(cls, value: datetime, values: ValidationInfo):
        data = values.data
        if data and "start_date" in data:
            if value < data["start_date"]:
                raise ValueError("End date must be after start date")
        return value

    @field_validator("participants", mode="before")
    @classmethod
    def check_participants(cls, value: list[str], values: ValidationInfo):
        data = values.data
        if data and "max_participants" in data:
            if len(value) > data["max_participants"]:
                raise ValueError("Too many participants")
        return value


if __name__ == "__main__":
    try:
        m = Event(
            start_date="Jan 23rd 2021 4 pm",
            end_date="Feb 7th 2021 11 am",
            max_participants=4,
            participants=["John", "Jane", "Bob"],
        )
        print(m.model_dump())
    except ValidationError as ex:
        print(ex)
