from django import forms

GAMES = [
    ("C", "COINS"),
    ("B", "CUBE"),
    ("N", "RANDOM_NUMBER"),
]


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=GAMES)
    attempts = forms.IntegerField(min_value=1, max_value=64)
