from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from pathlib import Path
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "diary/index.html", {"datetime_now": datetime_now})
    
class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, "diary/page_form.html", {"form": form})
    
class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.order_by("-page_date")
        return render(request, "diary/page_list.html", {"page_list": page_list})
    
class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})
    
class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, "diary/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        old_picture = page.picture

        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            new_picture = request.FILES.get("picture")
            if new_picture and old_picture and old_picture != new_picture:
                Path(old_picture.path).unlink(missing_ok=True)
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_update.html", {"form": form})
    
class PageDeleteVies(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_confirm_delete.html", {"page": page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect("diary:page_list")

index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteVies.as_view()