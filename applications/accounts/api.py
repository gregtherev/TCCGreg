"""This module contains the API for the accounts application."""
from ninja import Router

from .models import Team
from ..events.models import Question
from .schemas import TeamSchema, AnswerSchema  # NoQA

router = Router()


@router.get("/hello")
def hello(request):
    return "Hello, World!"


@router.get("/leaderboard-teams/{event_id}")
def leaderboard_teams(request, event_id: int):
    teams = Team.objects.filter(event__id=event_id)
    event = Team.event
    teams_list = []

    for team in teams:
        team.formated_time = ((team.penalties*60) * event.punishment_value
                              if team.penalties else team.relative_time)
        team_info = TeamSchema(**team.__dict__)
        teams_list.append(team_info)

    return teams_list


@router.post("/submit-answer/{event_id}/{question_number}")
def submit_answer(answer_info: AnswerSchema, event_id: int,
                  question_number: int):
    team = Team.objects.get(pk=answer_info.team_id)
    question = Question.objects.get(event__id=event_id,
                                    question_number=question_number)

    if answer_info.answer.lower() == question.correct_ansnwer.lower():
        if question_number in team.wr_questions:
            wr_set = team.wr_questions.split(",")
            wr_set = set(wr_set)
            wr_set.remove(str(question_number))

            rc_set = team.rc_questions.split(",")
            rc_set.add(question_number)

            team.rc_questions = str(rc_set)
            team.solved_questions += 1
            team.relative_time += answer_info.time
            team.save()

            return {"status": "SUCCESS", "question_status": "recovered"}

        rt_set = team.rt_questions.split(",")
        rt_set.add(question_number)

        team.rt_questions = str(rt_set)
        team.solved_questions += 1
        team.relative_time += answer_info.time
        team.save()

        return {"status": "SUCCESS", "question_status": "right"}

    if answer_info.answer.lower() != question.correct_ansnwer.lower():
        wr_set = team.wr_questions.split(",")
        wr_set = set(wr_set)
        wr_set.add(question_number)

        team.wr_questions = str(wr_set)
        team.penalties += 1
        team.save()

        return {"status": "SUCCESS", "question_status": "wrong"}

# TODO POPULAR O N-N SUBMISSAO A CADA SUBMISSAO ENVIADA PELO TIME
