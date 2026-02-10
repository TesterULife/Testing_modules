from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=10)
    title: str

    # @field_validator('id')
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('ID is not less than two')
    #     else:
    #         return v

# {'id': 1, 'title': 'Post 1'}
