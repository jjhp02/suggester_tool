# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# Create your forms here.

class MeasurementPlanForm(forms.Form):
    measurement_plan_json = forms.CharField(widget=forms.Textarea)

class ModelSelectionForm(forms.Form):
    training_file = forms.FileField()