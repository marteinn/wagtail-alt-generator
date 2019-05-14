# Adding AWS Rekognition as a provider

### Overview

Amazon's image analysis API. [Docs](https://aws.amazon.com/rekognition/)

- (+) Stable
- (-) Supports only tags

#### Installing

Add `...[rekognition]` when you install wagtailaltgenerator (this will install the extra packages required).

- `pip install wagtailaltgenerator[rekognition]`

#### Settings

The Rekognition provider is based on [boto](http://boto3.readthedocs.io/) and uses its [configuration](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

These are three of the most common settings:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account
- `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account
- `AWS_DEFAULT_REGION`: The default region to use, e.g. us-west-2, eu-west-1, etc

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.rekognition.Rekognition'`
