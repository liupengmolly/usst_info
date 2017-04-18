from django.test import TestCase

# Create your tests here.
def test(request):
	return HttpResponse(request.GET.get(query))