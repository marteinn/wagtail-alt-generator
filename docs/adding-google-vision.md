# Adding Google Vision

### Google Vision

Google's Cloud Vision API [docs](https://cloud.google.com/vision/).

- (+) Stable
- (-) Support only tags

#### Installing

- `pip install wagtailaltgenerator[google_vision]`

#### Settings

The Google Vision provider is based on `google-api-python-client` and are typically done using [Application Default Credentials](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow) for authentication.

You can authenticate locally with the [Google Cloud SDK](https://cloud.google.com/sdk/), on production with either the built in credentials (if you already run on Google Cloud) or with a [Service Account key file](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount).

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.google_vision.GoogleVision'`

