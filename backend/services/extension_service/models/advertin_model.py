from pydantic import BaseModel

class AdvertIn(BaseModel):
    company_name: str
    job_title: str
    location: str
    post_url: str
    description: str