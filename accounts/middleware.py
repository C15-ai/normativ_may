from django.utils import timezone
class RequestLogMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)


        user = request.user.username if request.user.is_authenticated else "AnonymousUser"
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        time = timezone.now().strftime("%b %d, %Y %I:%M %p")


        with open("request.log" , "a", encoding="utf-8") as f:
            f.write(f"{user}\t{ip}\t{path}\t{time}\n")


        return response
