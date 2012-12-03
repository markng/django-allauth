import floppyforms as forms


class FacebookConnectForm(forms.Form):
    access_token = forms.CharField(required=True)
