class AuthCheckerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        applyto = ["/report/"]
        print(f"path: {request.path}")
        response = self.get_response(request)
        if request.path in applyto:
            # Perform authentication logic for secured routes here
            # If authentication fails, return an appropriate response
            # print("middleware will apply here")
            headers = list(request.headers.keys())
            # print(headers)
            # if "Authorization" not in headers:
            #     print("authenticaltion not found")
            # else:
            #     print(f'authentication found {request.headers["Authorization"]}')
        # print(response.headers)

        return response