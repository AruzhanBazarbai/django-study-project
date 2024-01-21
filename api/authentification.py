from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication): # to change auth system in tastypie
    def is_authenticated(self, request, **kwargs):
        if request.method=="GET":
            return True
        
        return super().is_authenticated(request, **kwargs)