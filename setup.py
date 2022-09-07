$heroku buildpacks
=== my-example-app Buildpack URLs
1. heroku-community/example-buildpack
2. https://github.com/heroku/heroku-buildpack-python.git
$heroku buildpacks:clear
$heroku buildpacks:add heroku-community/example-buildpack
$heroku buildpacks:add heroku/python
$heroku buildpacks
=== my-example-app Buildpack URLs
1. heroku-community/example-buildpack
2. heroku/python
