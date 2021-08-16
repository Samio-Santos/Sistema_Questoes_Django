from django.shortcuts import render, redirect

# Personalização pagina 404
def page_not_404(request, exception):
    return render(request, 'paginas_personalizadas/404.html')

