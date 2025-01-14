from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Game, Console, Platform
from .forms import ProductForm, GameForm, ConsoleForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    title = ""
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                products = products.annotate(lower_name=Lower('name'))
                sortkey = 'lower_name'
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            title = "|"+",".join(str(category) for category in categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                 request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
             description__icontains=query)
            products = products.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search': query,
        'categories': categories,
        'sorting': sorting,
        'title': title,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        'game': product.game,
        'console': product.console,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product.'
                               'Please ensure the form is valid.')
        else:
            form = ProductForm()
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update product.'
                               'Please ensure the form is valid.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are editing {product.name}')
    else:
        form = ProductForm()

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def add_game(request):
    """ Add a game details """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = GameForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully added game details!')
                return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to add a game.'
                               'Please ensure the form is valid.')
        else:
            form = GameForm()
    else:
        form = ""

    template = 'products/add_game.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_game(request, game_id):
    """ Edit a product in the store """
    game = get_object_or_404(Game, pk=game_id)
    product = game.product
    if request.user.is_superuser:
        if request.method == 'POST':
            form = GameForm(request.POST, instance=game)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated game!')
                if (product):
                    return redirect(reverse('product_detail',
                                    args=[product.id]))
                else:
                    return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to update game.'
                               'Please ensure the form is valid.')
        else:
            form = GameForm(instance=game)
            messages.info(request, f'You are editing {game.title}')
    else:
        form = ""

    template = 'products/edit_game.html'
    context = {
        'form': form,
        'game': game,
    }

    return render(request, template, context)


def delete_game(request, game_id):
    """ Delete a product from the store """
    game = get_object_or_404(Game, pk=game_id)
    product = game.product
    if request.user.is_superuser:
        game.delete()
        messages.success(request, 'Game deleted!')
    return redirect(reverse('product_detail', args=[product.id]))


def add_console(request):
    """ Add a console details """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ConsoleForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully'
                                 ' added console details!')
                return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to add a console.'
                               ' Please ensure the form is valid.')
        else:
            form = ConsoleForm()
    else:
        form = ""
    template = 'products/add_console.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_console(request, console_id):
    """ Edit a product i
    n the store """
    console = get_object_or_404(Console, pk=console_id)
    product = console.product
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ConsoleForm(request.POST, instance=console)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated console!')
                if (product):
                    return redirect(reverse('product_detail',
                                    args=[product.id]))
                else:
                    return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to update console.'
                               'Please ensure the form is valid.')
        else:
            form = ConsoleForm(instance=console)
            messages.info(request, f'You are editing {console.title}')
    else:
        form = ""
    template = 'products/edit_console.html'
    context = {
        'form': form,
        'console': console,
    }

    return render(request, template, context)


def delete_console(request, console_id):
    """ Delete a product from the store """
    console = get_object_or_404(Console, pk=console_id)
    product = console.product
    if request.user.is_superuser:
        console.delete()
        messages.success(request, 'Console deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
