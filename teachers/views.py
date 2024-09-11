from datetime import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from lib.utils.pagination import paginate

from .forms import TeacherForm
from .models import Teacher


def mentor(request):
    return render(request, "teachers/mentor.html")


def index(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher_info = form.save(commit=False)
            teacher_info.user = request.user
            teacher_info.save()
            messages.success(request, "歡迎加入")
            return redirect("teachers:index")

        return render(request, "teachers/new.html", {"form": form})

    teachers = Teacher.objects.all()
    teachers = paginate(request, teachers)
    return render(request, "teachers/index.html", {"teachers": teachers})


@login_required
def new(request):
    form = TeacherForm()
    return render(request, "teachers/new.html", {"form": form})


def show(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    chat_group = teacher.chat_group
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "更新成功")
            return redirect("teachers:show", id=id)
        return render(request, "teachers/edit.html", {"teacher": teacher, "form": form})

    questions = teacher.get_questions().order_by("-created_at")[:3]
    answers = teacher.get_answers().order_by("-created_at")[:3]
    context = {
        "teacher": teacher,
        "questions": questions,
        "answers": answers,
        "chat_group": chat_group,
        "teacher_schedule_start": teacher.schedule_start,
        "teacher_schedule_end": teacher.schedule_end,
    }

    return render(request, "teachers/show.html", context)


@login_required
def edit(request, id):
    teacher = get_object_or_404(Teacher, id=id, user=request.user)
    form = TeacherForm(instance=teacher)
    return render(request, "teachers/edit.html", {"teacher": teacher, "form": form})


@login_required
def delete(request, id):
    teacher = get_object_or_404(Teacher, id=id, user=request.user)
    teacher.delete()
    messages.success(request, "刪除成功")
    return redirect("teachers:index")
