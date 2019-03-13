# halo-issues
Library for retrieving CloudPassage Halo issue information.

This library uses the `/v1/issues` endpoint to build a list of all issues
cerated, observed, or resolved since a certain point in time.

## Installing

`pip install .`

## Usage

Example:

Pretty-print all issues created, observed, or deleted since January 1st, 2019

```python

import os
import pprint

import haloissues

key = os.getenv("HALO_API_KEY")
secret = os.getenv("HALO_API_SECRET_KEY")

halo_issues = haloissues.HaloIssues(key, secret)
pprint.pprint(h_i.describe_all_issues("2019-01-01"))

```
