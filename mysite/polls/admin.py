from polls.models import Poll, Choice
from django.contrib import admin

#muestra 3 choice ligado a un poll
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#clase para modificar la parte administrativa de django
class PollAdmin(admin.ModelAdmin):
	#fields=['pub_date', 'question']
	"""fieldsets = [
		(None, {'fields':['question']}),
		('Date Information', {'fields':['pub_date']}),
	]"""
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	list_filter = ['pub_date']
	list_display = ('question', 'pub_date', 'was_published_recently')
	fieldsets = [
		(None, {'fields':['question']}),
		('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines =[ChoiceInline]
	
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
