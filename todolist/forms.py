from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, 
    widget=forms.TextInput(
        attrs={'class': '', 'Placeholder': 'Ingresar la tarea ej. compras', 'aria-label': 'Todo', 'aria-describeby': 'add-btn'}
    ))