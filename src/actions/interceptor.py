def interceptor(request):
    if request.url.startswith(('http://pizzeria.skillbox.cc/?wc-ajax=apply_coupon')):
        request.abort()
