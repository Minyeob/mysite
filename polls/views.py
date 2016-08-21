from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        i=request.POST['choice']
        j = i.replace('"','')
        selected_choice = p.choice_set.get(pk=j)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't selected a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})