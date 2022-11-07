from django import forms

class OrderTrackForm(forms.Form):
    order_id=forms.CharField(max_length=32)