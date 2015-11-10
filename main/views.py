# -*- encoding: utf-8 -*-

from main.models import Picture
import requests
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.timezone import now
from django.db.models import Q

def main_home(request):
	all_picture = Picture.objects.filter(
            Q(publish_date__lte=now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=now()) | Q(expiry_date__isnull=True),
            Q(is_publish=1))

	return render_to_response("main/home.html", locals(), context_instance=RequestContext(request))