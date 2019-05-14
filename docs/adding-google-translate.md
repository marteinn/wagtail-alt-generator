# Translating description/tags

## Why is this necessary?

The generated descriptions are returned as english, so we need to use separate translation providers to translate them to your websites local language.

### Overview

Google's Cloud Translation Api [docs](https://cloud.google.com/translate/docs/).

#### Installing

- `pip install wagtailaltgenerator[google_translate]`

#### Settings

The Google Cloud Translation Api uses `google-cloud-translate` and are typically authenticated using [Application Default Credentials](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow) for authentication.

You can authenticate locally with the [Google Cloud SDK](https://cloud.google.com/sdk/), on production with either the built in credentials (if you already run on Google Cloud) or with a [Service Account key file](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount).

You also need to activate translation

- `ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG`: `True`


