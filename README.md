# Aplicación Web Simple en Python

## Características

- Interfaz web moderna y responsiva
- Mensaje de bienvenida personalizado
- API REST simple
- Diseño atractivo con gradientes y animaciones
- Totalmente funcional con Python puro

## Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

```bash
python app.py
```

### 3. Abrir en el navegador

Accede a: **http://localhost:5000**

## Estructura del proyecto

```
AppWeb/
├── app.py                 # Archivo principal de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── templates/
│   └── index.html        # Página principal HTML
└── README.md             # Este archivo
```

## Tecnologías utilizadas

- **Python 3.x**
- **Flask** - Framework web ligero
- **HTML5** - Estructura
- **CSS3** - Estilos
- **JavaScript** - Interactividad

## Ejemplos de uso

### Acceso a la página principal
```
GET http://localhost:5000/
```

### Acceso a la API
```
GET http://localhost:5000/api/mensaje
```

```python
@app.route('/')
def bienvenida():
    return render_template('index.html', mensaje="Tu mensaje aquí")
```

