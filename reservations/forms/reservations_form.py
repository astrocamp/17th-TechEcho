from datetime import timedelta

from django.forms import ModelForm
from django.forms.widgets import DateTimeInput, TextInput

from reservations.models import TeacherSchedule


class TeacherScheduleForm(ModelForm):
    class Meta:
        model = TeacherSchedule
        fields = ["start_time"]
        widgets = {
            "start_time": DateTimeInput(
                attrs={"class": "flatpickr my-4", "type": "text"}
            ),
        }
        labels = {
            "start_time": "開始時間",
        }

    def save(self, commit=True):
        schedule = super().save(commit=False)
        if schedule.start_time:
            # 設定結束時間為開始時間後的1小時
            schedule.end_time = schedule.start_time + timedelta(hours=1)
        if commit:
            schedule.save()
        return schedule
