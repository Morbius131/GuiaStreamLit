# Guía interactiva de componentes de Streamlit

Aplicación educativa que explica y demuestra componentes comunes de Streamlit.

## Ejecutar localmente

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Desplegar en Streamlit Community Cloud

1. Sube `app.py`, `requirements.txt` y `README.md` a un repositorio de GitHub.
2. Abre https://share.streamlit.io/
3. Crea una app seleccionando el repositorio, la rama y `app.py`.

## Secciones incluidas

- Inicio
- Texto y formato
- Entradas y formularios
- Diseño y navegación
- Mensajes y estado
- Tablas y gráficos
- Archivos y multimedia
- Estado, caché y ejecución
- Mini proyecto CRUD en memoria
- Chuleta de referencia

Nota: el CRUD de demostración almacena datos en `st.session_state`, no en una base de datos persistente.
