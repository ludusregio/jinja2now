# To load the file with jinja2
from jinja2 import Environment, FileSystemLoader

# Pass the directory containing the templates to FileSystemLoader
file_loader = FileSystemLoader('templates')
# Setup an environment
env = Environment(loader=file_loader)
# Load the template
template = env.get_template('hello_world.txt')

# Render the template and print
output = template.render()
print(output)
