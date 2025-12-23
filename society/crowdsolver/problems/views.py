from django.shortcuts import render
from .models import signup , Category, raiseproblem, givesuggestion, voting
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate


def home(request):
    temp = 'home.html'
    return render(request,temp)

def sign_up(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email_flatno = request.POST.get('email_flatno')
        password = request.POST.get('password')
        sign_up=signup.objects.create(name=name, email_flatno=email_flatno, password=password)
        sign_up.save()
        return redirect('log_in')
     return render(request,'signup.html')

def log_in(request):
    if request.method == 'POST':
        email_flatno = request.POST.get('email_flatno')
        password = request.POST.get('password')
        try:
            user = signup.objects.get(email_flatno=email_flatno, password=password)
            request.session['member_id'] = user.id
            return redirect('dashboard')
        except signup.DoesNotExist:
            return render(request,'wrong.html')
    return render(request,'login.html')

def dashboard(request):
    memberinfo = signup.objects.get(id=request.session.get('member_id'))

    temp = 'dashboard.html'
    return render(request,temp,{'memberinfo':memberinfo})

def member(request):

    temp = 'member.html'
    return render(request,temp)

def raise_problem(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        created_by = request.session.get('member_id')
        if not title or not description or not category:
            # Handle error, perhaps redirect or show message
            return render(request, 'raiseproblem.html', {'categorys': Category.objects.all(), 'error': 'All fields are required.'})
        try:
            category_id = int(category)
            Category.objects.get(id=category_id)  # Validate category exists
        except (ValueError, Category.DoesNotExist):
            return render(request, 'raiseproblem.html', {'categorys': Category.objects.all(), 'error': 'Invalid category.'})
        raise_problem=raiseproblem.objects.create(title=title, description=description, category_id=category_id, created_by_id=created_by)
        raise_problem.save()
        return redirect('dashboard')
    categorys = Category.objects.all()
    temp = 'raiseproblem.html'
    return render(request,temp,{'categorys':categorys})


def suggestions(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('log_in')
    raiseproblems = raiseproblem.objects.exclude(created_by_id=member_id)
    return render(request, 'suggestions.html', {'raiseproblems': raiseproblems})

def givesuggestions(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        created_by = request.session.get('member_id')
        givesuggestion_obj = givesuggestion.objects.create(content=content, created_by_id=created_by)
        givesuggestion_obj.save()
        return redirect('suggestions')
    return render(request, 'givesuggestions.html')


def vote(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('log_in')
    if request.method == 'POST':
        name = signup.objects.get(id=member_id).name
        member = signup.objects.get(id = member_id)
        suggestions_id = request.POST.get('suggestions_id')
        solution = givesuggestion.objects.get(id=suggestions_id)
        votetype = request.POST.get('vote')

        already_voted = voting.objects.filter(memberdata=member, suggestiondata=solution).exists()
        if not already_voted:
            is_approval = (votetype == 'approve')
            voting.objects.create(memberdata=member, suggestiondata=solution, is_approval=(votetype =='approve'))

            if votetype == 'approve':
                solution.approval += 1
            else:
                solution.reject += 1
            solution.save()
        
        return redirect('voting')
    solution = givesuggestion.objects.all()
    for sol in solution:
        total = sol.approval + sol.reject
        if total > 0:
            sol.percentage = (sol.approval / total) * 100
        else:
            sol.percentage = 0
        voted_solutions = voting.objects.filter(memberdata__id=member_id, suggestiondata=sol).values_list('suggestiondata__id', flat=True)
        sol.has_voted = sol.id in voted_solutions
        
    return render(request, 'voting.html', {'solution': solution})

 


def profile(request):
    member_id = request.session.get('member_id')
    memberinfo = signup.objects.get(id=member_id)
    problem = raiseproblem.objects.filter(created_by_id = member_id)

    return render(request,'profile.html',{'memberinfo':memberinfo, 'problem':problem})



def finalsolution(request):
    allvotes = givesuggestion.objects.all().order_by('-approval')

    temp = 'finalsolution.html'
    return render(request,temp,{'allvotes':allvotes})


def wrong(request):
    return redirect('wrong')

def logout(request):
    request.session.flush()
    return redirect('log_in')

def solutions(request):
    sol = givesuggestion.objects.all()
    return render(request, 'solutions.html', {'sol': sol})