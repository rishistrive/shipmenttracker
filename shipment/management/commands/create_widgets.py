from django.core.management.base import BaseCommand
from shipment.models import Widgets

class Command(BaseCommand):
    help = 'Create widgets'


    def handle(self, *args, **kwargs):
        all_widgets = ['Chart', 'Info', 'List', 'Statistics']
        for widgets in all_widgets:
            Widgets.objects.create(name=widgets)