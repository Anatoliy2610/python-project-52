from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    username = forms.CharField(
        label="Имя пользователя",
        help_text="""Обязательное поле.
                               Не более 150 символов.
                               Только буквы, цифры и символы @/./+/-/_.""",
    )
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput()
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже существует")
        return username


class UsersChangeForm(RegisterUserForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            if username != self.instance.username:
                raise forms.ValidationError("Имя пользователя уже существует")
        return username
