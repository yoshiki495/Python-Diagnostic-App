from django import forms
from .models import Result

# http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.phpを参考に


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["result1", "result2", "result3", "result4", "result5"]
