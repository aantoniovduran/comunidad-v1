from django.shortcuts import render, redirect
from pagos.models import Profile, Cuota, Pagos
from .forms import PagosForm
from django.contrib.auth.decorators import login_required


def pagina_inicio(request):
    return render(request, 'pagina/inicio.html')

@login_required
def listacuotas(request):
    listacuotas = Cuota.objects.all().filter(socio=request.user)
    contexto = {'cuotas': listacuotas}
    return render(request, 'pagina/cuotas.html', contexto)


#@login_required
#def pagos_new(request):
 #   form = PagosForm()
  #  return render(request, 'paginas/pagos.html', {'form': form})

@login_required
def perfil(request):
    return render(request, "pagina/perfil.html")

@login_required
def pagos_new(request):
    if request.method == 'POST':
        form = PagosForm(request.user, request.POST)
        if form.is_valid():
            pagos = form.save(commit=False)
            pagos.user = request.user
            pagos.save()
            return redirect('pagos')
    else:
        form = PagosForm(request.user)
    return render(request, 'pagina/pagos.html', {'form': form})