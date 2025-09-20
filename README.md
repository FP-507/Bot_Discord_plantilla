# Discord Bot 

## Requisitos
- Python 3.10+
- Docker (opcional)

## Configuración local
1. Copia `.env.example` a `.env` y añade tu `DISCORD_TOKEN` (lo obtienes en el [Discord Developer Portal](https://discord.com/developers/applications)).
2. Instala dependencias:
```bash
copy .env.example .env #copiar el .env.example en el .env
venv\Scripts\activate    # Windows
pip install -r requirements.txt #installar los requerimientos 
python -m bot.main #activar el bot

