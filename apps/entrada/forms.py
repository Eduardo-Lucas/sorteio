from django import forms


class ContactForm(forms.Form):
    nome_completo = forms.CharField(label='Nome Completo', max_length=50, help_text='Informe seu nome completo')
    email = forms.EmailField(max_length=50, help_text='Informe seu endereço eletrônico')
    mensagem = forms.CharField(widget=forms.Textarea, required=True, help_text='Escreva sua mensagem')
