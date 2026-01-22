from subprocess import call
import os

# Instalamos python3 y hacemos git clone
call(['sudo', 'apt-get', 'update'])

call(['sudo', 'apt-get', 'install', '-y',
      'python3.9', 'python3.9-distutils'])
#


call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])

call(['sudo', 'apt-get', 'install', '-y', 'git'])


call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
call(['python3.9','-m','pip', 'install', '--user','-r', 'practica_creativa2/bookinfo/src/productpage/requirements.txt'])

# Configuración del entorno y modificación del código Python
app_dir = 'practica_creativa2/bookinfo/src/productpage'
os.chdir(app_dir)

team_id = os.environ.get("TEAM_ID", "19")

# Modificación de la plantilla HTML para personalizar el título
os.chdir('templates')

with open('productpage.html', 'r') as fin:
    content = fin.read()

content = content.replace(
    '{% block title %}Simple Bookstore App{% endblock %}',
    '{% block title %}Grupo {{ team_id }} {% endblock %}'
)

with open('productpage.html', 'w') as fout:
    fout.write(content)

# Ejecución de la aplicación en el puerto 9090
os.chdir('..')
call(['python3.9', 'productpage_monolith.py', '9090'])
