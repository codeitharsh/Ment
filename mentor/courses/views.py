from django.views.generic import TemplateView

class Courses(TemplateView):
    template_name = 'courses/courses.html'
