from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=30, label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=30, label='Parolayı Doğrula', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm: #bu parola alanı doldurulmuş mu confirm alanı doldurulmuşmu? 2 si aynı olmadıgı zaman!
            raise forms.ValidationError("Parolalar eşleşmiyor!")
        
        values = {
            'username' : username,
            'password' : password
        }
        return values







