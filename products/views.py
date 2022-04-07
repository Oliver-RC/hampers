from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Occasion, Reviews, savedListItems
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().filter(is_available=True)
    query = None
    occasions = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'occasion':
                sortkey = 'occasion__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'occasion' in request.GET:
            occasions = request.GET['occasion'].split(',')
            products = products.filter(occasion__name__in=occasions)
            occasions = Occasion.objects.filter(name__in=occasions)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search content was entered, please try again")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_occasions': occasions,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    try:
        saved_items = savedListItems.objects.filter(user=request.user.id)
    except savedListItems.DoesNotExist:
        saved_items = None
    if saved_items.filter(item=product).exists():
        button = True
    else:
        button = False
    reviews = Reviews.objects.filter(product_id=product.id, status=True)

    context = {
        'product': product,
        'reviews': reviews,
        'saved_items': saved_items,
        'button': button
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Error - only shop owners allowed')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product to shop database')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product - please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Error - only shop owners allowed')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product - please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the shop """

    if not request.user.is_superuser:
        messages.error(request, 'Error - only shop owners allowed')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted from the shop database')
    return redirect(reverse('products'))


def review_submission(request, product_id):
    """ Logged in user to submit a review on a product """

    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews_submission = Reviews.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews_submission)
            form.save()
            messages.success(request, 'Thank you - your review has been updated')
            return redirect(url)
        except Reviews.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Reviews()
                data.subject = form.cleaned_data['subject']
                data.star_rating = form.cleaned_data['star_rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you - your review has been submitted')
                return redirect(url)


@login_required
def saved_item_list(request):
    """ User to access their saved item list """
    try:
        saved_items = savedListItems.objects.filter(user=request.user.id)[0]
    except IndexError:
        item_list = None
    else:
        item_list = saved_items.item.all()

    if not item_list:
        messages.info(request, 'Your saved items list is empty')

    template = 'products/saved_items.html'
    context = {
        'item_list': item_list,
        'saved_items': saved_items
    }

    return render(request, template, context)


@login_required
def add_saved_items(request, product_id):
    """ user to add a product to their saved item list"""
    item = get_object_or_404(Product, pk=product_id)
    try:
        saved_item = get_object_or_404(savedListItems, user=request.user.id)
    except Http404:
        saved_item = savedListItems.objects.create(user=request.user)
    if item in saved_item.item.all():
        messages.info(request, 'Your Saved Items contains this product already')
    else:
        saved_item.item.add(item)
        messages.info(request, f'Added {item.name} to your Save Items')
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_saved_items(request, product_id):
    """ user to remove a product to their saved item list"""
    item = get_object_or_404(Product, pk=product_id)
    saved_item = get_object_or_404(savedListItems, user=request.user.id)
    if item in saved_item.item.all():
        saved_item.item.remove(item)
        messages.info(request, f'Remove {item.name} from your Save Items')
    else:
        messages.error(request, (f'{item.name} is not in your Save Items'))
    return redirect(request.META.get('HTTP_REFERER'))
