import logging

logger = logging.getLogger(__name__)

async def safe_send(channel, content: str):
    """Envía un mensaje atrapando errores para evitar crashear el bot."""
    try:
        await channel.send(content)
    except Exception as e:
        logger.exception("Error enviando mensaje: %s", e)
