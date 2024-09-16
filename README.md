# Tecnologías sin Servidor con Azure Functions

Este proyecto guía a través del proceso de creación y despliegue de Azure Functions utilizando diversos disparadores para automatizar tareas comunes en la nube. La actividad incluye la configuración de recursos en Azure, la creación de funciones sin servidor desde el equipo local y la validación del funcionamiento de estas funciones tanto localmente como en Azure.

## Descripción del Proyecto

Este proyecto implementa varias Azure Functions con diferentes disparadores para demostrar el uso de tecnologías sin servidor. Los disparadores utilizados incluyen HTTP, Timer, Blob, Queue, Service Bus, Event Grid, Cosmos DB, Event Hub, SignalR, e IoT Hub.

### Tecnologías y Herramientas Utilizadas

- **Azure Functions**: Servicios sin servidor para ejecutar funciones en respuesta a eventos.
- **Azure Storage**: Para almacenar datos como blobs, colas y tablas.
- **Visual Studio Code (VSC)**: Para el desarrollo local de funciones.
- **Python**: Lenguaje utilizado para desarrollar las funciones.
- **Postman**: Para probar las APIs localmente y en Azure.
- **Extensiones de VSC**: Azure Functions, Azurite, Azure Account, Azure Tools.

## Pasos Realizados

1. **Configuración en Azure**:
    - Creación de un grupo de recursos.
    - Creación de una cuenta de almacenamiento con contenedores y tablas.
    - Asignación de permisos de acceso al profesor para la cuenta de almacenamiento.
    
2. **Desarrollo Local**:
    - Verificación e instalación de Python.
    - Configuración del entorno local con las extensiones necesarias en VSC.
    - Creación de funciones con diferentes disparadores y ejecución en local usando Azurite como emulador.
    - Pruebas locales de las APIs usando Postman.

3. **Despliegue en Azure**:
    - Inicio de sesión en Azure desde VSC.
    - Despliegue de las funciones en Azure con la configuración de variables de ambiente necesarias.
    - Pruebas de las rutas desplegadas en Azure desde Postman.

4. **Validación de la Funcionalidad**:
    - Verificación de la creación y eliminación de colas en la cuenta de almacenamiento desde Azure Functions.
    - Envío de las rutas desarrolladas al profesor para la verificación.

## Rutas Desarrolladas

- **HTTP Trigger**: https://fa-mc-USUARIO.azurewebsites.net/api/http_trigger
- **Queue Delete Trigger**: https://fa-mc-USUARIO.azurewebsites.net/api/queue/delete

## Requisitos

- Cuenta de Azure con permisos para crear recursos y funciones.
- Visual Studio Code con extensiones de Azure instaladas.
- Python instalado en el equipo local.

## Ejecución de Funciones

Para probar las funciones localmente:

1. Abra el proyecto en Visual Studio Code.
2. Inicie Azurite utilizando el comando `Azurite:start`.
3. Ejecute la función localmente desde el menú "Run" seleccionando "Start Debugging".
4. Pruebe las rutas generadas localmente en su navegador o Postman.

Para probar las funciones desplegadas en Azure:

1. Asegúrese de que las variables de ambiente estén correctamente configuradas en Azure.
2. Utilice las rutas proporcionadas arriba en Postman o directamente en un navegador para verificar la funcionalidad.

