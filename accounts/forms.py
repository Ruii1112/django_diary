from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'password1': 'パスワード',
            'password2': 'パスワード（確認用）',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # パスワードフィールドのヘルプテキストを削除
        self.fields['password1'].widget.attrs.update({'placeholder': 'パスワードを入力してください'})
        self.fields['password2'].widget.attrs.update({'placeholder': '確認用パスワードを入力してください'})
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''