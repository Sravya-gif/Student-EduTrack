from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'erp/home.html')

def student_login(request):
    student = None
    total = percentage = None

    if request.method == 'POST':
        roll = request.POST.get('roll')
        try:
            student = Student.objects.get(roll_number=roll)
            total = student.total()
            percentage = student.percentage()
        except:
            pass

    return render(request, 'erp/student_login.html', {
        'student': student,
        'total': total,
        'percentage': percentage
    })

def leaderboard(request):
    students = Student.objects.all()
    students = sorted(students, key=lambda x: x.percentage(), reverse=True)[:3]
    return render(request, 'erp/leaderboard.html', {'students': students})
