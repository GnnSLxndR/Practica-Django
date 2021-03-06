#from django.template import Context, loader
#encoding:utf-8
from django.template import RequestContext
from polls.models import Choice, Poll
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
#importar los forms
from polls.forms import ChoiceForm, PollForm, ChoiceForm2

def index(request):
    latest_poll_list = Poll.objects.all().order_by('id')[:5]
    return render_to_response('index.html', {'latest_poll_list': latest_poll_list}, context_instance=RequestContext(request))
	


def detail(request, poll_id):
    #implementar error 404 con Http404
    """
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'poll': p})"""
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('detail.html', {'poll': p},
    							context_instance=RequestContext(request))




def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('results.html', {'poll': p})




def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))



#vista de formulario
def question(request):
	if request.method == 'POST':
		formulario = PollForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/polls/')
	else:
		formulario = PollForm()
	return render_to_response('pollform.html', {'formulario':formulario},
								 context_instance=RequestContext(request))
								 


def new_choice(request):

	"""vista que crea un formulario apartir del modelo.... donde toca seleccionar
	   en que question agregar el choice pero no es la mejor manera para una vista publica
	"""
	if request.method == 'POST':
		formulario = ChoiceForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/polls/')
	else:
		formulario = ChoiceForm()
	return render_to_response('choiceform.html', {'formulario':formulario},
								 context_instance=RequestContext(request))



def new_choice2(request, poll_id):

	"""vista para ingresar choice a un question ya seleccionada en la pagina Index
		como debe ser el ingreso de una choice en una vista publica
	"""
	poll = Poll.objects.get(pk=poll_id)
	if request.method == 'POST':
		choice = Choice(poll=poll)
		formulario = ChoiceForm2(request.POST, instance=choice)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/polls/')
	else:
		formulario = ChoiceForm2()
	return render_to_response('choiceform.html', {'formulario':formulario, 'poll':poll},
								 context_instance=RequestContext(request))



def delete_question(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	p.delete()
	return HttpResponseRedirect(reverse('polls.views.index'))



def delete_choice(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('detail1.html', {
				'poll': p,'error_message': "You didn't select a choice.",
				}, context_instance=RequestContext(request))
	else:
		selected_choice.delete()
		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))



"""las vista detail1 y detalle son la misma vaina :D pero direcciona a una pagina
   html diferente igual que la vista detail linea 17....
"""
def detail1(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('detail1.html', {'poll': p},
    							context_instance=RequestContext(request))


#vista para ver mismo detalle
def detalle(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('detalle.html',{'poll':p},
								context_instance=RequestContext(request))



def actualizar(request, poll_id):
	p = Poll.objects.get(pk=poll_id)
	p.question = request.POST['question']
	p.pub_date = request.POST['fecha']
	p.save()
	return HttpResponseRedirect(reverse('polls.views.index'))
