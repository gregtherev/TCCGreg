from pydantic import BaseModel


class TeamInfo(BaseModel):
    name: str
    solved_questions: int
    relative_time: int
    penalties: int
    rt_questions: str
    wr_questions: str
    rc_questions: str
    formated_time: int
