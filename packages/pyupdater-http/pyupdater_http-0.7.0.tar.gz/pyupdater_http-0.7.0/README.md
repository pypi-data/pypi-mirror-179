[![Build Status](https://img.shields.io/github/workflow/status/micro-fan/pyupdater-http/main)](https://github.com/micro-fan/pyupdater-http/actions)
[![PyPi version](https://img.shields.io/pypi/v/pyupdater-http.svg)](https://pypi.python.org/pypi/pyupdater-http)


## Parameters

* `server_url` - add basic auth if you need it
* `data_params` - additional params that will be passed with file
* `filename_param` - field name for file name if your server need it


## Usage Example

### with `codeskyblue/gohttpserver`


Traefik is optional, you can export direct ports. This is just reminder of how we're doing it

```bash
$ pip install --user -U dot-tools
$ exec zsh

# if you have local packages in your `PATH`
# like: `/home/user/.local/bin/traefik_run`

$ traefik_run up -d
```

Then launch your web site

```yaml
version: '3.9'

services:
  releases_server:
    image: codeskyblue/gohttpserver:1.1.0
    container_name: releases_server
    # define only if you want to have basic-auth
    command: --auth-type http --auth-http basic_auth_user:basic_auth_password
    volumes:
      - ./uploads:/app/public
    # you can export ports if you're not using traefik
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.releases.rule=Host(`releases.example.com`)"
      - "traefik.http.routers.releases.entrypoints=web"

```

And put into `uploads` directory file `.ghs.yaml`:

```yaml
---
upload: false
delete: false
users:
- email: "cybergrind@example.com"
  delete: true
  upload: true
  token: auth_token_for_upload
```

And add configuration in your `config.pyu`

```json
{
 "app_config": {
    "PLUGIN_CONFIGS": {
      "httpuploader-@cybergrind": {
        "server_url": "http://basic_auth_user:basic_auth_password@releases.example.com/",
        "data_params": {
          "token": "auth_token_for_upload"
        },
        "timeout": 600,
        "filename_param": "filename"
      }
    }
  }
}
```
