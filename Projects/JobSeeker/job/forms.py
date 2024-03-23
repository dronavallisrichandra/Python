from django import forms
from django.db.models import fields
from .models import TechUser, JobUser, JobPost, Profile, JobApply, HrUser


class HrUserCreate(forms.ModelForm):

	class Meta:
		model = HrUser
		fields="__all__"


class TechUserCreate(forms.ModelForm):

	CHOICES=[('M','Male'),
         ('F','Female')]

	gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	password=forms.CharField(label='Password', widget=forms.PasswordInput)
	dob=forms.CharField(label='Date of Birth', widget=forms.widgets.DateInput(attrs={'type':"date"}))
   

	class Meta:
		model=TechUser
		fields="__all__"


class JobUserCreate(forms.ModelForm):

	CHOICES=[('M','Male'),
         ('F','Female')]

	gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	password=forms.CharField(label='Password', widget=forms.PasswordInput)
	dob=forms.CharField(label='Date of Birth', widget=forms.widgets.DateInput(attrs={'type':"date"}))
   

	class Meta:
		model=JobUser
		fields="__all__"


class JobPostCreate(forms.ModelForm):

	PostDate=forms.CharField(label='Post Date', widget=forms.widgets.DateInput(attrs={'type':"date"}))

	class Meta:
		model=JobPost
		fields="__all__"

class ProfileCreate(forms.ModelForm):

	education1 = [
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
    ]
	job_role1 = [
        ('Junior Analyst','Junior Analyst'),
        ('Analyst','Analyst'),
        ('Engineer','Engineer'),
        ('Senior Engineer','Senior Engineer'),
        ('Manager','Manager'),
    ]

	education = forms.ChoiceField(choices=education1, widget=forms.Select(attrs={'class': 'form-control'}))
	job_role = forms.ChoiceField(choices=job_role1, widget=forms.Select(attrs={'class': 'form-control'}))
	
	class Meta:
		model=Profile
		fields="__all__"

class JobApplyCreate(forms.ModelForm):


	class Meta:
		model = JobApply
		fields="__all__"
