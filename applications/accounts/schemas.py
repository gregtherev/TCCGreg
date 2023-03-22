from .models import Team
from ninja import ModelSchema, Schema


class TeamSchema(ModelSchema):
    class Config:
        model = Team
        model_fields = ['name', 'solved_questions', 'relative_time',
                        'penalties', 'formated_time', 'rt_questions',
                        'wr_questions', 'rc_questions']


class AnswerSchema(Schema):
    team_id: int
    answer: str
