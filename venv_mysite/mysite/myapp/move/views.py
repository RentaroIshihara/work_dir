# myapp/views.py
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            with open('form_data.txt', 'a') as f:
                f.write(f'Username: {username}, Email: {email}\n')
            return render(request, 'my_template.html', {'form': form, 'message': 'フォームのデータを保存しました。'})
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})