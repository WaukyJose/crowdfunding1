from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(
        label="Usuario:",
        min_length=6,
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ej.: Donante123"}
        ),
    )
    nombre = forms.CharField(
        label="Nombre:",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ej.: Carlos"}
        ),
    )
    apellido = forms.CharField(
        label="Apellido:",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ej.: Yánez"}
        ),
    )
    email = forms.EmailField(
        label="Email:",
        max_length=75,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ej.: miemailpersonal@gmail.com",
            }
        ),
    )
    password1 = forms.CharField(
        label="Contraseña:",
        min_length=8,
        max_length=16,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Ej.: de*738Hoewiux!$"}
        ),
    )
    password2 = forms.CharField(
        label="Repita la contraseña:",
        min_length=8,
        max_length=16,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Ej.: de*738Hoewiux!$"}
        ),
    )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            self.add_error("password2", "Las contraseñas no coinciden.")

        return cleaned_data


class donarMonto(forms.Form):
    monto = forms.FloatField(
        label="Ingrese el monto a donar",
        widget=forms.NumberInput(
            attrs={
                "step": "any",  # Permite cualquier número de decimales
            }
        ),
    )
