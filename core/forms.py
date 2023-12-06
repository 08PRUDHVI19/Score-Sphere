from django import forms

class getResults(forms.Form):
    id=forms.CharField()

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.fields['id'].label=""
        self.fields['id'].widget.attrs.update(
            {'class':'form-control'}
        )
