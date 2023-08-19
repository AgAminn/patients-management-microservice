docker run --rm --name yaml_render \
-v $PWD/ci_config/jenkins_crp:/templates \
dinutac/jinja2docker:latest /templates/standalone.j2 /variables/variables.yml --format=yaml > docker-compose.yml


# docker run --rm 
# -v $PWD/inputs/templates:/templates 
# -v $PWD/inputs/variables:/variables \
# -e DATABASE=mysql56 -e IMAGE=latest \
# dinutac/jinja2docker:latest /templates/standalone.j2 /variables/variables.yml --format=yaml > docker-compose.yml