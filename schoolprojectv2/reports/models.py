from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class Report(models.Model):
    SPAM_REPORT = 'SPAM'
    NEGATIV_REPORT = 'NEGA'
    RACIST_REPORT = 'RACI'
    HARASS_REPORT = 'HARAS'
    UNNECESSARY_REPORT = 'UNNE'

    REPORT_TYPE = [
        (SPAM_REPORT, 'Spam'),
        (NEGATIV_REPORT, 'Negative Behavior'),
        (RACIST_REPORT, 'Racist Behavior'),
        (HARASS_REPORT, 'Harassement Report'),
        (UNNECESSARY_REPORT, 'unnecessary / motiveless behavior')
    ]

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    report_type = models.CharField(choices = REPORT_TYPE, default = UNNECESSARY_REPORT, max_length = 100)
    datestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.from_user} reported {self.report_type} on {self.content_type} instance"

    def save(self, *args, **kwargs):
        #checking if the same report has already been made
        instance = Report.objects.filter(
            from_user = self.from_user,
            content_type = self.content_type,
            object_id = self.object_id,
            report_type = self.report_type
        )
        if instance.exists():
            raise ValueError("This report has already been made !")
        return super(Report, self).save(*args, **kwargs)
