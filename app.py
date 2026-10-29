import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import date

st.set_page_config(
    page_title="Guía interactiva de Streamlit",
    page_icon="📘",
    layout="wide",
)

st.title("📘 Guía interactiva de componentes de Streamlit")
st.caption("Proyecto educativo: explora componentes, mira ejemplos y prueba cómo responden.")
st.info("Cada sección incluye una breve explicación y ejemplos funcionales. Usa el menú lateral para navegar.")

seccion = st.sidebar.radio(
    "📚 Secciones",
    [
        "Inicio",
        "Texto y formato",
        "Entradas y formularios",
        "Diseño y navegación",
        "Mensajes y estado",
        "Tablas y gráficos",
        "Archivos y multimedia",
        "Estado, caché y ejecución",
        "Mini proyecto CRUD",
        "Chuleta de referencia",
    ],
)

if seccion == "Inicio":
    st.header("¿Qué es Streamlit?")
    st.write(
        "Streamlit es un framework de Python para crear aplicaciones web de datos. "
        "Escribes Python y Streamlit genera la interfaz; no necesitas construir por separado "
        "un frontend con HTML, CSS o JavaScript para una aplicación básica."
    )
    a, b, c = st.columns(3)
    a.metric("Curva inicial", "Baja")
    b.metric("Lenguaje principal", "Python")
    c.metric("Uso frecuente", "Datos e IA")
    st.subheader("Cómo funciona")
    st.code(
        "Entrada del usuario → lógica Python → resultado en la interfaz",
        language="text",
    )
    st.markdown(
        """
        **Flujo típico de desarrollo**
        1. Crear `app.py`.
        2. Importar Streamlit: `import streamlit as st`.
        3. Dibujar la interfaz usando `st.title()`, `st.button()`, etc.
        4. Ejecutar con `streamlit run app.py`.
        5. Publicar el proyecto desde un repositorio GitHub en Streamlit Community Cloud.
        """
    )
    st.subheader("Requisitos del proyecto")
    st.code("pip install -r requirements.txt\nstreamlit run app.py", language="bash")
    st.warning("La aplicación vuelve a ejecutar el script cuando hay interacciones. Usa `st.session_state` para conservar estado entre ejecuciones.")

elif seccion == "Texto y formato":
    st.header("1. Texto y formato")
    st.write("Los componentes de texto sirven para explicar, titular y mostrar contenido.")
    st.subheader("Títulos y texto")
    st.title("st.title() — título principal")
    st.header("st.header() — encabezado")
    st.subheader("st.subheader() — subtítulo")
    st.write("st.write() muestra texto, objetos y estructuras de datos.")
    st.caption("st.caption() muestra una nota secundaria.")
    st.markdown("Markdown admite **negrita**, *cursiva*, listas y enlaces.")
    st.code('st.title("Mi aplicación")\nst.header("Sección")\nst.write("Hola")\nst.caption("Nota secundaria")', language="python")
    st.divider()
    st.subheader("Código, JSON y ecuaciones")
    st.code("def saludar(nombre):\n    return f'Hola, {nombre}'", language="python")
    st.json({"usuario": "Ana", "activo": True, "roles": ["editor", "lector"]})
    st.latex(r"E = mc^2")
    st.code("st.code('print(1 + 1)', language='python')\nst.json({'activo': True})\nst.latex(r'E = mc^2')", language="python")

elif seccion == "Entradas y formularios":
    st.header("2. Entradas de datos")
    st.write("Los widgets capturan valores introducidos o seleccionados por el usuario.")
    with st.container(border=True):
        nombre = st.text_input("st.text_input — Nombre", placeholder="Escribe tu nombre")
        descripcion = st.text_area("st.text_area — Descripción", placeholder="Escribe varias líneas")
        edad = st.number_input("st.number_input — Edad", min_value=0, max_value=120, value=20)
        acepta = st.checkbox("st.checkbox — Acepto las condiciones")
        nivel = st.slider("st.slider — Nivel", min_value=0, max_value=100, value=50)
        ciudad = st.selectbox("st.selectbox — Ciudad", ["Bogotá", "Medellín", "Cali", "Villavicencio"])
        lenguajes = st.multiselect("st.multiselect — Lenguajes", ["Python", "Java", "JavaScript", "C++"])
        prioridad = st.radio("st.radio — Prioridad", ["Baja", "Media", "Alta"], horizontal=True)
        fecha = st.date_input("st.date_input — Fecha", value=date.today())
        hora = st.time_input("st.time_input — Hora")
        color = st.color_picker("st.color_picker — Color", "#00AEEF")
        cantidad = st.select_slider("st.select_slider — Tamaño", options=["XS", "S", "M", "L", "XL"], value="M")
        st.write("Valor actual:", {
            "nombre": nombre, "descripcion": descripcion, "edad": edad,
            "acepta": acepta, "nivel": nivel, "ciudad": ciudad,
            "lenguajes": lenguajes, "prioridad": prioridad,
            "fecha": str(fecha), "hora": str(hora), "color": color,
            "tamaño": cantidad,
        })
    st.subheader("Botones")
    if st.button("st.button — Probar acción"):
        st.success("¡El botón se ha pulsado!")
    st.code(
        'nombre = st.text_input("Nombre")\n'
        'edad = st.number_input("Edad", min_value=0)\n'
        'activo = st.checkbox("Activo")\n'
        'ciudad = st.selectbox("Ciudad", ["Bogotá", "Cali"])\n'
        'if st.button("Guardar"):\n'
        '    st.success(f"Guardado: {nombre}")',
        language="python",
    )
    st.subheader("Formulario: enviar varios campos juntos")
    with st.form("formulario_demo"):
        correo = st.text_input("Correo electrónico")
        comentario = st.text_area("Comentario")
        enviado = st.form_submit_button("Enviar formulario")
    if enviado:
        if correo.strip():
            st.success(f"Formulario recibido para {correo}.")
            st.write("Comentario:", comentario or "(sin comentario)")
        else:
            st.error("Introduce un correo para continuar.")
    st.caption("Dentro de `st.form()` los cambios se envían al pulsar el botón de envío del formulario.")

elif seccion == "Diseño y navegación":
    st.header("3. Diseño y navegación")
    st.write("Estos componentes organizan la interfaz en regiones, columnas, pestañas y paneles.")
    st.subheader("Columnas")
    col1, col2, col3 = st.columns(3)
    col1.metric("Columna 1", "A")
    col2.metric("Columna 2", "B")
    col3.metric("Columna 3", "C")
    st.code('col1, col2, col3 = st.columns(3)\ncol1.write("A")\ncol2.write("B")\ncol3.write("C")', language="python")
    st.subheader("Contenedor")
    with st.container(border=True):
        st.write("Este contenido está agrupado dentro de `st.container()`.")
        st.caption("Útil para organizar bloques relacionados.")
    st.subheader("Pestañas")
    tab1, tab2, tab3 = st.tabs(["Resumen", "Código", "Notas"])
    with tab1:
        st.write("Contenido de la pestaña Resumen.")
    with tab2:
        st.code('tab1, tab2 = st.tabs(["Resumen", "Código"])', language="python")
    with tab3:
        st.info("Cada pestaña tiene su propio bloque de contenido.")
    st.subheader("Expander")
    with st.expander("Pulsa para desplegar detalles"):
        st.write("`st.expander()` permite ocultar contenido secundario hasta que el usuario lo necesite.")
    st.subheader("Barra lateral")
    st.write("El menú de navegación de esta aplicación está construido en `st.sidebar`.")
    st.code('opcion = st.sidebar.selectbox("Sección", ["Inicio", "Reportes"])', language="python")

elif seccion == "Mensajes y estado":
    st.header("4. Mensajes y feedback")
    st.success("st.success — operación completada")
    st.info("st.info — información general")
    st.warning("st.warning — advertencia")
    st.error("st.error — error")
    st.code('st.success("Guardado")\nst.info("Información")\nst.warning("Revisa los datos")\nst.error("Ocurrió un error")', language="python")
    st.subheader("Progreso y carga")
    if st.button("Simular proceso"):
        barra = st.progress(0, text="Iniciando...")
        for porcentaje in range(0, 101, 20):
            time.sleep(0.08)
            barra.progress(porcentaje, text=f"Procesando: {porcentaje}%")
        st.success("Proceso de demostración finalizado.")
    st.caption("`st.spinner()` también puede mostrar un indicador mientras se ejecuta una tarea.")
    st.subheader("Métricas")
    m1, m2, m3 = st.columns(3)
    m1.metric("Usuarios", "1.240", "+8%")
    m2.metric("Errores", "3", "-2")
    m3.metric("Tiempo medio", "120 ms", "-15 ms")

elif seccion == "Tablas y gráficos":
    st.header("5. Tablas y visualización de datos")
    st.write("Streamlit puede mostrar DataFrames y gráficos sencillos o integrar bibliotecas especializadas.")
    df = pd.DataFrame({
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "Ventas": [120, 150, 135, 190, 220],
        "Gastos": [80, 95, 90, 110, 130],
    })
    st.subheader("Tabla interactiva — st.dataframe()")
    st.dataframe(df, use_container_width=True)
    st.subheader("Tabla estática — st.table()")
    st.table(df.head(3))
    st.subheader("Gráfico de líneas — st.line_chart()")
    st.line_chart(df.set_index("Mes")[["Ventas", "Gastos"]])
    st.subheader("Gráfico de barras — st.bar_chart()")
    st.bar_chart(df.set_index("Mes")[["Ventas", "Gastos"]])
    st.subheader("Gráfico de dispersión — st.scatter_chart()")
    puntos = pd.DataFrame({"Horas": [1, 2, 3, 4, 5, 6], "Puntuación": [52, 58, 65, 70, 82, 88]})
    st.scatter_chart(puntos, x="Horas", y="Puntuación")
    st.code(
        'st.dataframe(df, use_container_width=True)\n'
        'st.table(df.head(3))\n'
        'st.line_chart(df.set_index("Mes")[["Ventas", "Gastos"]])\n'
        'st.bar_chart(df.set_index("Mes")[["Ventas", "Gastos"]])',
        language="python",
    )
    st.caption("Para gráficos avanzados puedes usar `st.pyplot()` con Matplotlib o `st.plotly_chart()` con Plotly.")

elif seccion == "Archivos y multimedia":
    st.header("6. Archivos y multimedia")
    st.subheader("Subir un archivo")
    archivo = st.file_uploader("Selecciona un archivo de texto o CSV", type=["txt", "csv"])
    if archivo is not None:
        st.success(f"Archivo cargado: {archivo.name}")
        if archivo.name.lower().endswith(".csv"):
            try:
                datos = pd.read_csv(archivo)
                st.dataframe(datos, use_container_width=True)
            except Exception as exc:
                st.error(f"No se pudo leer el CSV: {exc}")
        else:
            contenido = archivo.getvalue().decode("utf-8", errors="replace")
            st.text_area("Contenido del archivo", contenido, height=180)
    st.code(
        'archivo = st.file_uploader("Sube un CSV", type=["csv"])\n'
        'if archivo is not None:\n'
        '    df = pd.read_csv(archivo)\n'
        '    st.dataframe(df)',
        language="python",
    )
    st.subheader("Imagen")
    st.write("`st.image()` muestra una imagen local o una URL accesible.")
    st.code('st.image("imagen.png", caption="Ejemplo", width=300)', language="python")
    st.subheader("Audio y video")
    st.code('st.audio("audio.mp3")\nst.video("video.mp4")', language="python")
    st.warning("No se incluye un archivo multimedia de ejemplo. Usa rutas de archivos que existan en tu proyecto o fuentes accesibles.")

elif seccion == "Estado, caché y ejecución":
    st.header("7. Estado, caché y ejecución")
    st.subheader("st.session_state")
    st.write("Conserva valores entre reruns dentro de la sesión de un usuario.")
    if "contador_guia" not in st.session_state:
        st.session_state.contador_guia = 0
    x, y = st.columns(2)
    if x.button("Incrementar contador"):
        st.session_state.contador_guia += 1
    if y.button("Reiniciar contador"):
        st.session_state.contador_guia = 0
    st.metric("Contador de esta sesión", st.session_state.contador_guia)
    st.code(
        'if "contador" not in st.session_state:\n'
        '    st.session_state.contador = 0\n'
        'if st.button("Incrementar"):\n'
        '    st.session_state.contador += 1\n'
        'st.write(st.session_state.contador)',
        language="python",
    )
    st.subheader("Caché de datos")
    st.write("`st.cache_data` puede reutilizar resultados de funciones que procesan datos.")
    st.code(
        '@st.cache_data\n'
        'def cargar_datos():\n'
        '    return pd.read_csv("datos.csv")',
        language="python",
    )
    st.subheader("Caché de recursos")
    st.write("`st.cache_resource` es útil para recursos compartidos, como modelos cargados o conexiones reutilizables.")
    st.code(
        '@st.cache_resource\n'
        'def cargar_modelo():\n'
        '    return crear_modelo()',
        language="python",
    )
    st.warning("No caches datos privados de un usuario de forma compartida sin diseñar correctamente la separación de datos. Protege credenciales con `st.secrets`, no las escribas en el código.")
    st.subheader("Otros componentes")
    st.markdown(
        "- `st.rerun()`: solicita volver a ejecutar el script.\n"
        "- `st.dialog()`: crea un diálogo modal.\n"
        "- `st.fragment()`: permite ejecutar una sección de manera independiente en versiones compatibles.\n"
        "- `st.set_page_config()`: configura título, icono y diseño de página."
    )

elif seccion == "Mini proyecto CRUD":
    st.header("8. Mini proyecto CRUD en memoria")
    st.write("Ejemplo de crear, leer y eliminar registros usando widgets y `st.session_state`. Los datos se pierden al terminar la sesión o reiniciar el entorno; no se usa una base de datos.")
    if "usuarios_demo" not in st.session_state:
        st.session_state.usuarios_demo = [
            {"id": 1, "nombre": "Ana", "rol": "Admin"},
            {"id": 2, "nombre": "Luis", "rol": "Usuario"},
        ]
    with st.form("crear_usuario"):
        nuevo_nombre = st.text_input("Nombre del usuario")
        nuevo_rol = st.selectbox("Rol", ["Admin", "Usuario", "Editor"])
        crear = st.form_submit_button("Crear usuario")
    if crear:
        if nuevo_nombre.strip():
            next_id = max([u["id"] for u in st.session_state.usuarios_demo], default=0) + 1
            st.session_state.usuarios_demo.append({"id": next_id, "nombre": nuevo_nombre.strip(), "rol": nuevo_rol})
            st.success("Usuario creado.")
        else:
            st.error("El nombre no puede estar vacío.")
    st.subheader("Usuarios registrados")
    st.dataframe(pd.DataFrame(st.session_state.usuarios_demo), use_container_width=True, hide_index=True)
    ids = [u["id"] for u in st.session_state.usuarios_demo]
    if ids:
        eliminar_id = st.selectbox("ID para eliminar", ids)
        if st.button("Eliminar usuario"):
            st.session_state.usuarios_demo = [u for u in st.session_state.usuarios_demo if u["id"] != eliminar_id]
            st.success(f"Usuario {eliminar_id} eliminado.")
            st.rerun()
    st.code(
        'if "usuarios" not in st.session_state:\n'
        '    st.session_state.usuarios = []\n'
        'with st.form("crear"):\n'
        '    nombre = st.text_input("Nombre")\n'
        '    guardar = st.form_submit_button("Guardar")\n'
        'if guardar and nombre.strip():\n'
        '    st.session_state.usuarios.append({"nombre": nombre})\n'
        'st.dataframe(pd.DataFrame(st.session_state.usuarios))',
        language="python",
    )

elif seccion == "Chuleta de referencia":
    st.header("9. Chuleta rápida")
    referencia = [
        ("Texto", "st.title, st.header, st.subheader, st.write, st.markdown, st.caption, st.code, st.json"),
        ("Entradas", "st.button, st.text_input, st.text_area, st.number_input, st.checkbox, st.radio, st.selectbox, st.multiselect, st.slider"),
        ("Fecha y hora", "st.date_input, st.time_input"),
        ("Diseño", "st.columns, st.container, st.expander, st.tabs, st.sidebar, st.form"),
        ("Mensajes", "st.success, st.info, st.warning, st.error, st.toast, st.progress, st.spinner"),
        ("Datos", "st.dataframe, st.table, st.metric, st.json"),
        ("Gráficos", "st.line_chart, st.bar_chart, st.scatter_chart, st.pyplot, st.plotly_chart"),
        ("Archivos", "st.file_uploader, st.download_button, st.image, st.audio, st.video"),
        ("Estado", "st.session_state, st.rerun"),
        ("Rendimiento", "st.cache_data, st.cache_resource"),
        ("Estructura avanzada", "st.dialog, st.fragment, st.set_page_config"),
    ]
    st.dataframe(pd.DataFrame(referencia, columns=["Categoría", "Componentes"]), use_container_width=True, hide_index=True)
    st.subheader("Comandos para ejecutar")
    st.code("python -m venv .venv\n# Windows PowerShell:\n.venv\\Scripts\\Activate.ps1\n# macOS/Linux:\nsource .venv/bin/activate\npip install -r requirements.txt\nstreamlit run app.py", language="bash")
    st.subheader("Archivos para publicar")
    st.markdown("- `app.py`: aplicación.\n- `requirements.txt`: dependencias.\n- Opcional: `README.md` con instrucciones.")
    st.markdown("Documentación oficial: [docs.streamlit.io](https://docs.streamlit.io/)")

st.divider()
st.caption("Guía educativa de Streamlit • Los ejemplos están diseñados para ejecutarse localmente y desplegarse desde GitHub.")
