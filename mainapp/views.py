from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment 
from .forms import CommentForm
from .forms import ContactForm

def index(request):
    category_slug = request.GET.get('category')  # Отримуємо параметр з URL
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()  # Отримуємо всі категорії
    return render(request, 'mainapp/index.html', {'posts': posts, 'categories': categories})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()  # Отримуємо всі коментарі до цієї статті
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Прив'язуємо коментар до статті
            comment.save()
            return redirect('post_detail', slug=post.slug)  # Перенаправляємо назад на сторінку статті
    else:
        form = CommentForm()

    return render(request, 'mainapp/post_detail.html', {'post': post, 'comments': comments, 'form': form})

from django.shortcuts import render

def about(request):
    return render(request, 'mainapp/about.html')  # Створимо шаблон для сторінки "Про мене"

def contact(request):
    return render(request, 'mainapp/contact.html')  # Створимо шаблон для сторінки "Контакти"



from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Тут можна обробити дані форми, наприклад, надіслати email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Для прикладу, ми просто виведемо повідомлення
            print(f"Запит від {name} ({email}): {message}")
            
            # Потім можна перенаправити користувача або відобразити повідомлення про успіх
            return render(request, 'mainapp/contact_success.html', {'name': name})
    else:
        form = ContactForm()
    
    return render(request, 'mainapp/contact.html', {'form': form})

def recent_posts(request):
    # Отримуємо останні 5 постів, сортуємо за датою створення
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'recent_posts.html', {'posts': posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отправка email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['твій_мейл@gmail.com']  # Сюди буде надходити лист

            send_mail(subject, message, sender, recipients)
            return HttpResponse('Ваше повідомлення надіслано!')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})