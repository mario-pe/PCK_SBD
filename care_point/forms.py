from django.db.models import TextField

from .models import *
from django import forms


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract

        fields = ['genre', 'date_from', 'date_to']

        labels = {
            'genre': 'Typ',
            'date_from': 'Data od',
            'date_to': 'Data do',
            # 'caregiver': 'Opiekun',
                }


class Point_of_careForm(forms.ModelForm):

    class Meta:
        model = Point_of_care

        fields = ['city']

        labels = {
            'city': 'miasto',
        }


class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager

        fields = ['name', 'sname', 'point_of_care']

        labels = {
            'name': 'Imie',
            'sname': 'Nazwisko',
            'point_of_care': 'odzial',
        }


class CaregiverForm(forms.ModelForm):

    class Meta:
        model = Caregiver

        fields = ['name', 'sname', 'point_of_care']

        labels = {
            'name': 'Imie',
            'sname': 'Nazwisko',
            'point_of_care': 'Odzial',
        }



class AddressForm(forms.ModelForm):

    class Meta:
        model = Address

        fields = ['city', 'street', 'number', 'zip_code']

        labels = {
            'city': 'Miasto',
            'street': 'Ulica',
            'number': 'Numer domu',
            'zip_code': 'Kod pocztowy',
        }


class WardForm(forms.ModelForm):

    class Meta:
        model = Ward

        fields = ['name', 'sname', 'pesel']

        labels = {
            'name': 'Imie',
            'sname': 'Nazwisko',
            'pesel': 'PESEL',
            'address': 'Adres',
        }


class DecisionForm(forms.ModelForm):

    illness = forms.ModelMultipleChoiceField(queryset=Illness.objects.all(), widget=forms.CheckboxSelectMultiple())
    activity = forms.ModelMultipleChoiceField(queryset=Activity.objects.all() ,widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Decision

        fields = ['percent_payment', 'hours', 'charge', 'ward', 'illness', 'activity']

        labels = {
            'percent_payment': 'Doplata z MOPS w procentach',
            'hours': 'Przyslugujace godziny',
            'charge': 'Stawka godzinowa',
            'ward': 'Podopieczny',
            'illness': 'Dolegliwosci',
            'activity': 'Czynnosci',
        }


class IllnessForm(forms.ModelForm):

    class Meta:
        model = Illness

        fields = ['name', 'description']

        labels = {
            'name': 'Nazwa shorzenia',
            'description': 'Opis',
        }


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity

        fields = ['name', 'description']

        labels = {
            'name': 'Nazwa shorzenia',
            'description': 'Opis',
        }


class WorksheetForm(forms.ModelForm):

    class Meta:
        model = Worksheet

        fields = ['caregiver', 'ward', 'genre', 'decision', 'date', 'hour_from', 'hour_to',
                  'description']

        labels = {
            'caregiver': 'Opiekunka',
            'ward': 'Podopieczny',
            'genre': 'typ zlecenia',
            'decision': 'Decyzji',
            'date': 'Data',
            'hour_from': 'Godzina od',
            'hour_to': 'Godzina do',
        }
