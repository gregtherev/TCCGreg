import magic
from datetime import datetime, timedelta

from django.db import models
from ..accounts.models import Team, Judge

EVENT_TYPES = (
    (0, "Envio automático"),
    (1, "Validação do juíz")
)

SUBMISSION_STATUS = (
    (0, "Incorreto"),
    (1, "Correto")
)


def validate_pdf(value):
    mime = magic.Magic(mime=True)
    content_type = mime.from_buffer(value.read())
    if content_type != 'application/pdf':
        raise BaseException("File is not a PDF")


class Event(models.Model):
    name = models.CharField("Nome do evento", max_length=255)
    date = models.DateField("Data do evento")
    start_time = models.DateTimeField("Hora de início", blank=True, null=True)
    duration = models.PositiveIntegerField("Duraçao do evento em horas",
                                           null=True,
                                           default=1)
    type = models.IntegerField(
        "Tipo de submissão", choices=EVENT_TYPES, default=0)
    punishment_value = models.IntegerField(
        verbose_name='Valor em minutos de cada punição acumulada',
        default=20)
    final_results = models.JSONField("Resultado final", null=True, blank=True)
    partial_results = models.JSONField("Resultado parcial", null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    questions_pdf = models.FileField(upload_to='question_pdfs/', validators=[validate_pdf], null=True)
    institution = models.ForeignKey('Institution',
                                    on_delete=models.SET_NULL,
                                    null=True)
    judges = models.ManyToManyField(Judge)

    def __str__(self):
        return self.name

    def is_running_today(self):
        return self.date == datetime.now().date()

    def finish_time(self):
        finish_time = datetime.now()
        finish_time = finish_time.replace(hour=self.start_time.hour,
                                          minute=self.start_time.minute)
        finish_time = finish_time + timedelta(hours=self.duration)
        return finish_time

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ('date', '-start_time')


class Question(models.Model):
    qt_number = models.PositiveIntegerField("Número da questão", null=False)
    question = models.TextField('Texto da questão (opcional)', null=True)
    # TODO criar campo de submissão do arquivo da questão
    # image = models.ImageField('Upload de imagem', upload_to=None, height_field=None, width_field=None, max_length=None) ## NOQA
    correct_ansnwer = models.CharField("Alternativa correta ('X' caso seja validação de juíz)",  # NOQA
                                       max_length=1)
    event = models.ForeignKey('Event',
                              on_delete=models.CASCADE,
                              verbose_name='Evento')

    def __str__(self):
        return f'Questão {self.id}'

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'


class Institution(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da instituição")
    city = models.CharField(max_length=50, verbose_name="Cidade")
    # TODO criar parametro de logo para subir a imagem da instituição

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'


class Submission(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)
    time = models.TimeField(auto_now_add=True)
    status = models.PositiveIntegerField(
        "Status da subimissão", choices=SUBMISSION_STATUS)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
