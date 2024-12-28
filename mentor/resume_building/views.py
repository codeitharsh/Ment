from django.views.generic import TemplateView

class Resume(TemplateView):
    template_name = 'resume_building/resume.html'
