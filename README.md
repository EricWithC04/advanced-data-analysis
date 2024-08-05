# Ejercicio de Repaso Librerías Python

Una vez clonado el repositorio, crear un entorno virtual y acceder al mismo:
```bash
virtualenv venv
```
```bash
source venv/Scripts/activate
```
Instalar las dependencias:
```bash
pip install -r requirements.txt
```

Crear una base de datos con los campos requeridos e importar los datos del archivo `data.csv`  

En el archivo `main.py`, cambiar las credenciales de la linea `6` en caso de ser necesario
```python
host = "localhost", 
database = 'companydata',
user="root", 
passwd=""
```

Para probar cada uno de los ejercicios, en la ultima linea escribir un `print()` dentro del cuál invocar la función correspondiente

```python
print(total_employees_per_department()) # Ejemplo
```