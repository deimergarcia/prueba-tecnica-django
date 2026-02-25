# 🚀 Prueba Técnica – Desarrollador Python (Django)

Proyecto CRM desarrollado por **Deimer Garcia** para el proceso de selección técnico.

Este proyecto cumple con todos los requisitos solicitados:
- Backend: Django + PostgreSQL en la nube (sin instalación local).
- CRUD completo de Clientes y Oportunidades.
- Consumo de API pública (ciudades de Colombia).
- Automatización: marcar oportunidades como "En seguimiento" después de 7 días.
- Interfaz funcional con Bootstrap.
- Documentación clara, paso a paso, sin barreras.

---

## 📦 Requisitos del Sistema

Antes de empezar, asegúrate de tener instalado:

- **Python 3.8 o superior**
- **Git**

---

## 🧭 Instrucciones Paso a Paso

Sigue cada paso exactamente como se indica.  
El proyecto está diseñado para que **funcione al 100% sin errores** si sigues esto al pie de la letra.

### 1. Clona el repositorio

Abre tu terminal (CMD, PowerShell o Terminal) y ejecuta:

```bash
git clone https://github.com/deimergarcia/prueba-tecnica-django.git  
cd prueba-tecnica-django
```

---

### 2. Crea y activa el entorno virtual

Crea un entorno aislado para las dependencias:

```bash
python -m venv venv
```

Actívalo:

```bash
venv\Scripts\activate
```

👉 Verás `(venv)` al inicio de la línea → estás listo.

---

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

Esto instala:
- Django
- psycopg2-binary (para PostgreSQL)
- requests (para consumir APIs)

✅ Debe terminar sin errores.

---

### 4. Configura la base de datos (¡único paso manual!)

Crea un archivo llamado `.env` en la **misma carpeta que `manage.py`**.

Puedes hacerlo así:

#### En Windows (CMD):
```bash
notepad .env
```
Cuando te pregunte si quieres crear el archivo, di **Sí**.

#### En VS Code o editor gráfico:
- Abre la carpeta del proyecto.
- Crea un nuevo archivo llamado `.env`.

Ahora, **copia y pega exactamente esto dentro del archivo `.env`**:

```
DATABASE_URL=postgresql://deimer_owner:ZdX5Lp9uQ2aV@ep-crimson-math-a5b6c7d8.us-east-2.aws.neon.tech:5432/crm_prueba_db
```

Guarda y cierra el archivo.

> 🔐 Esta es una base de datos temporal que he configurado exclusivamente para esta prueba técnica.
> - No necesitas registrarte ni instalar PostgreSQL.
> - La base de datos contiene estructura inicial lista para usar.
> - Este acceso será desactivado después del proceso de selección.

---

### 5. Aplica las migraciones

Ejecuta este comando:

```bash
python manage.py migrate
```

👉 Debe mostrar muchas líneas diciendo `OK`.  
Si ves un error de conexión, revisa que el `.env` tenga la URL correcta.

---

### 6. Inicia el servidor

```bash
python manage.py runserver
```

Verás:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

### 7. Accede a la aplicación

Abre tu navegador y ve a:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Allí podrás:
- Ver la lista de clientes.
- Crear nuevos clientes (con ciudad desde API de Colombia).
- Registrar oportunidades.
- Editar y eliminar registros.

---

## 🔄 Automatización: Cambiar estado a "En seguimiento"

Este comando simula que todas las oportunidades en estado "Nuevo" tienen más de 7 días y las marca automáticamente como "En seguimiento".

### Ejecútalo en otra terminal (deja el servidor corriendo):

```bash
# Asegúrate de estar en la carpeta del proyecto
cd prueba-tecnica-django

# Activa el entorno
venv\Scripts\activate

# Ejecuta el comando
python manage.py actualizar_oportunidades
```

👉 Verás:
```
Se procesaron X oportunidades: ahora están en "En seguimiento"
```

Actualiza la página [http://127.0.0.1:8000/ver-oportunidades](http://127.0.0.1:8000/ver-oportunidades) para ver el cambio.

---

## 👁️ Vista de Oportunidades por Cliente

Haz clic en el botón **"🔍 Ver Oportunidades"** en la página principal.

Allí verás:
- Cada cliente con sus oportunidades debajo.
- Estado, valor estimado, fecha y acciones.
- Todos los cambios del comando son visibles aquí.

---

## 📄 Consumo de API Pública

La aplicación consume la API oficial de ciudades de Colombia:

🔗 [https://api-colombia.com/api/v1/City](https://api-colombia.com/api/v1/City)

- Se usa al crear o editar un cliente.
- Muestra un `<select>` con todas las ciudades.
- Si falla, permite entrada manual.

---

## ✅ Buenas Prácticas Implementadas

| Característica | Detalle |
|----------------|--------|
| **Organización del proyecto** | Estructura clara: apps, modelos, vistas, plantillas, comandos personalizados. |
| **Modelos y relaciones** | Uso correcto de `ForeignKey`, `DateTimeField(auto_now_add)`, `choices`. |
| **PostgreSQL en la nube** | Neon.tech → sin instalación local. |
| **Consumo de API** | Con manejo de errores y fallback. |
| **Automatización** | Comando claro y funcional. |
| **Documentación** | Este README detallado, sin ambigüedades. |

---

## 🎯 Autor

**Deimer Garcia**