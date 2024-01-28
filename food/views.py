from django.shortcuts import redirect, render
from .models import Items
from .forms import ItemsForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# from django.template import loader

# Create your views here.


# def hello(request):
#     return HttpResponse("Hellow word")


def items(request):
    food = Items.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item': food,
    }
    return render(request, 'food/index.html', context)


class ItemsViews(ListView):
    model = Items
    template_name = 'food/index.html'
    context_object_name = 'item'


def detail(request, item_id):
    items = Items.objects.get(pk=item_id)
    context = {
        'item_name': items.items_name,
        'item_price': items.items_price,
        'item_desc': items.items_desc,
        'item_img': items.items_image,
        'item_id': items.id,
    }
    return render(request, 'food/detail.html', context)


class ItemsDetailsViews(DetailView):
    model = Items
    template_name = 'food/detail.html'


def create_items(request):
    form = ItemsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:items')
    return render(request, 'food/from-create.html', {'form': form})


class CreateItems(CreateView):
    model = Items
    template_name = 'food/from-create.html'
    fields = ['items_name', 'items_desc', 'items_price',
              'items_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def update_items(request, item_id):
    items = Items.objects.get(pk=item_id)
    form = ItemsForm(request.POST or None, instance=items)

    if form.is_valid():
        form.save()
        return redirect('food:items')
    return render(request, 'food/from-create.html', {'form': form})


def delete_items(request, item_id):
    items = Items.objects.get(pk=item_id)
    print(f"**********{request.method}")
    if request.method == 'POST':
        print("**********")

        items.delete()
        return redirect('food:items')
    return render(request, 'food/delete.html', {'item_id': item_id})


class DeleteItems(DetailView):
    model = Items
    template_name = 'food/delete.html'
