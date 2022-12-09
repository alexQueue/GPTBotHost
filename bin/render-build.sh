
#!/usr/bin/env bash
# From https://render.com/docs/deploy-rails#update-your-app-for-render
# exit on error
set -o errexit

poetry install
