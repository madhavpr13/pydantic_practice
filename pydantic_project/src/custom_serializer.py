from pydantic import BaseModel, field_serializer
from datetime import datetime

class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt", when_used="json-unless-none")
    def serialize_date(self):
        # print(f"type= {type(value)}")
        return self.dt.strftime("%Y/%m/%d %I:%M %p")


m = Model(dt=datetime(2020, 1,1, 12, 0))
print(repr(m))
print(m.model_dump_json())

