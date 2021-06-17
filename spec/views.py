from spec.forms import CreateApplyForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import applicant
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def main(request):
    applicants = applicant.objects
    return render(request, 'main.html', {'applicants': applicants})


def info(request, applicant_id):
    resume_info = get_object_or_404(applicant, pk=applicant_id)
    return render(request, 'info.html', {'resume_info': resume_info})


def create(request):
    if request.method == 'POST':
        form = CreateApplyForm(request.POST, request.FILES)
        if form.is_valid():
            applicants = form.save(commit=False)
            applicants.date = timezone.datetime.now()
            applicants.save()
        return redirect('/info/'+str(applicants.id))
    else:
        form = CreateApplyForm()
    return render(request, 'create.html', {'form': form})


def create_applicant(request):
    person = applicant()
    person.name = request.GET['name']
    person.age = request.GET['age']
    person.introduce = request.GET['introduce']
    person.gender = request.GET['gender']
    person.date = timezone.datetime.now()
    person.photo = request.FILES['photo']
    person.save()
    return redirect('/info/'+str(person.id))


def edit(request, applicant_id):
    applicants = applicant.objects.get(id=applicant_id)
    if request.method == "POST":
        form = CreateApplyForm(
            request.POST, request.FILES, instance=applicants)
        if form.is_valid():
            applicants = form.save()
            return redirect('/info/'+str(applicants.id))
    else:
        form = CreateApplyForm(instance=applicants)
        return render(request, 'create.html', {'form': form})


def delete(request, applicant_id):
    applicants = applicant.objects.get(id=applicant_id)
    applicants.delete()
    return redirect("main")


def user_info(request):
    applicants = applicant.objects
    return render(request, 'userinfo.html', {'applicants': applicants})
