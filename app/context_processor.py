from users.forms import AjaxAuthenticationForm


def get_context_data(request):
    context = {
        'ajax_login': AjaxAuthenticationForm()
    }
    return context
