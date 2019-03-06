from sanic.response import html
from webconsole.main.app import jinjaEnv


# Index page
async def index(request):
    template = jinjaEnv.get_template('index.html')
    html_content = template.render()
    return html(html_content)
