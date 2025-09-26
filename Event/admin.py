from django.contrib import admin

# Register your models here.

from .models import Event,Participants


# admin.site.register(Event)


class ParticipantInline(admin.StackedInline):
    
    model=Participants
    
    extra=20


def accept_state(ModelAdmin , request , queryset):
    
    queryset.update(state=True)


def refuse_state(ModelAdmin , request , queryset):
    
    queryset.update(state=False)
    
    
    

def changeCategory(ModelAdmin , request , queryset):
    
    queryset.update(category="Sport")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description','category','state','organisateur','nbr_participants','evt_date',)

    
    search_fields=('title',)
    
    list_per_page=1
    
    list_filter=('category','state',)
    
    actions=[accept_state , refuse_state , changeCategory]
    
    
    inlines=[ParticipantInline]




admin.site.register(Participants)