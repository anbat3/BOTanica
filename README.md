# 🌸 BOTanica

**BOTanica** es un asistente virtual desarrollado con el framework **Rasa** que proporciona información detallada sobre diversas flores. Este chatbot está diseñado para ayudar a los usuarios a conocer más sobre las características, temporadas y cuidados de diferentes especies florales.

---

## 🚀 Comenzando

Estas instrucciones te guiarán para obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### 📋 Pre-requisitos

Asegúrate de tener instalados los siguientes componentes:

- **Python 3.9**
---

### ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/anbat3/BOTanica.git
```

2. Navega al directorio del proyecto:

```bash
cd BOTanica
```

3. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa 'venv\Scripts\activate'
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Entrena el modelo:

```bash
rasa train
```

---

## 🧠 Uso

1. Ejecuta el servidor de acciones personalizadas:

```bash
rasa run actions
```

2. En una nueva terminal, inicia el chatbot:

```bash
rasa shell
```

Ahora puedes interactuar con BOTanica para descubrir todo sobre tus flores favoritas 🌺.

---

## 📁 Estructura del Proyecto

- `data/` → Datos de entrenamiento (intents, entities, stories)
- `actions/` → Acciones personalizadas
- `models/` → Modelos entrenados
- `domain.yml` → Intents, entidades, slots, respuestas y acciones
- `config.yml` → Configuración del pipeline y políticas

---

## 🤝 Contribuyendo

¿Quieres mejorar BOTanica? ¡Genial!

1. Realiza un fork del proyecto
2. Crea una rama:

```bash
git checkout -b feature/mi-mejora
```

3. Haz tus cambios y haz commit:

```bash
git commit -m "Mejora: añade info sobre rosas"
```

4. Push a tu rama:

```bash
git push origin feature/mi-mejora
```

5. Abre una Pull Request 🚀

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

---

## 🌻 Agradecimientos

- A las flores 🌷 por inspirar este bot 🌼

---

*¡Gracias por usar BOTanica!*
