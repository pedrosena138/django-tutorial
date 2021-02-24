from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = get_list_or_404(
        Question.objects.order_by('-pub_date')[:5])
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        error = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }

        return render(request, 'polls/detail.html', error)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prev ents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# The code for our vote() view does have a small problem.
# It first gets the selected_choice object from the database, then computes the new value of votes, and then saves it back to the database.
# If two users of your website try to vote at exactly the same time, this might go wrong: The same value, let’s say 42, will be retrieved for votes.
# Then, for both users the new value of 43 is computed and saved, but 44 would be the expected value.

# This is called a race condition. If you are interested, you can read Avoiding race conditions using F() to learn how you can solve this issue.
