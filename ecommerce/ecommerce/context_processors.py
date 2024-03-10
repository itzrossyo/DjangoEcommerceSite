def login_check_func(request):
    if request.user.is_authenticated:
        is_login = True
    else:
        is_login = False
    
    return {'is_login':is_login}