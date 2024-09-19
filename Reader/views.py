from django.shortcuts import render, redirect
from .forms import ReaderForm


def reader_form(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_detail')
    else:
        form = ReaderForm()
    return render(request, 'reader_form.html', {'form': form})

