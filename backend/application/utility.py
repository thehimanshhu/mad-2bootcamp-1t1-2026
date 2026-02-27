from jinja2 import Template
def render_email_template(username , bookings , file_path):
    with open(file_path ,"r") as file:
        t = Template(file.read())
        return t.render(username = username , bookings= bookings)
