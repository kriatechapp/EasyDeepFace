
PASSO 1: Instalar Python no Windows

Baixe a versão 64 bits do Python 3.10 ou 3.11:
https://www.python.org/downloads/windows/

Marque a opção “Add Python to PATH” durante a instalação.

Verifique no terminal (cmd ou PowerShell):

python --version
Deve mostrar Python 3.10.x ou Python 3.11.x

Verifique se é 64 bits:

python -c "import struct; print(struct.calcsize('P')*8)"


Resultado deve ser 64

PASSO 2: Criar um ambiente virtual (opcional, mas recomendado)
python -m venv deepface_env
deepface_env\Scripts\activate


Isso evita conflitos entre bibliotecas.

Para desativar o ambiente: deactivate

PASSO 3: Atualizar pip e instalar dependências
python -m pip install --upgrade pip setuptools wheel
pip install opencv-python numpy pandas tqdm
pip install tensorflow==2.13.0
pip install deepface


Se aparecer erro de “Windows Long Path”, siga as instruções:

Ativar Windows Long Path no registro (LongPathsEnabled = 1)

Reinicie o computador

Se aparecer erro de TensorFlow runtime:

Instale o Visual C++ Redistributable: https://aka.ms/vs/17/release/vc_redist.x64.exe

Reinicie o computador
