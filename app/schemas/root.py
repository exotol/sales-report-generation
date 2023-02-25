from pydantic import BaseModel, Field


class Root(BaseModel):
    title: str = Field(
        "Sales report generation service v 0.1.0"
    )
