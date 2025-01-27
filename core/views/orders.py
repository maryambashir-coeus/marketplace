from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms.addItemForm import AddItemForm
from django.contrib.auth.decorators import login_required
from .models import Purchase, Item

def home(request):
    query = request.GET.get('search', '')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()
    return render(request, 'home.html', {'items': items, 'query': query})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('home')
    else:
        form = AddItemForm()
    return render(request, 'add_item.html', {'form': form})

@login_required
def order_history(request):
    purchases = Purchase.objects.filter(buyer=request.user).order_by('-purchase_date')
    return render(request, 'order_history.html', {'purchases': purchases})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def purchase_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if item.seller == request.user:
        messages.error(request, "You cannot purchase your own item.")
        return redirect('item_detail', item_id=item.id)
    
    if Purchase.objects.filter(item=item).exists():
        messages.error(request, "This item has already been purchased.")
        return redirect('item_detail', item_id=item.id)
    
    Purchase.objects.create(item=item, buyer=request.user)
    messages.success(request, f"You successfully purchased {item.name}!")
    
    return redirect('purchase_success', item_id=item.id)


@login_required
def purchase_success(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'purchase_success.html', {'item': item})
