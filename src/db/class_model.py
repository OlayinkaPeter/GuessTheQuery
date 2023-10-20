from pydantic import BaseModel


class SearchQueryInput(BaseModel):
    search_query: str
