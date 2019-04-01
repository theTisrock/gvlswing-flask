# urls
# ---- helper classes that hold information about:
#   *Actions
#   *URL pathways


class Action():
    # these are names of methods called by the routes. Use with url_for(Action.[action_name])
    index = 'index'
    admin_panel = 'admin_panel'
    admin_login = 'admin_login'
    admin_register = 'admin_register'
    logout = 'logout'


class URL():
    root = '/'
    index = '/index'
    admin = '/admin'
    admin_control_panel = admin + '/control_panel'
    admin_login = admin + '/login'
    admin_register = admin + '/register'
    logout = '/logout'



# end urls
