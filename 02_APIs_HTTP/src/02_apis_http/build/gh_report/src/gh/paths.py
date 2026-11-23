from pathlib import Path
from icecream import ic

# logs
log_file: Path = Path(__file__).parent.parent.parent / "data" / "logs" / "app.log"
log_file.parent.mkdir(parents=True, exist_ok=True)
log_file.touch()
ic(log_file)

env_path = Path(__file__).resolve().parent.parent.parent / "data" / ".env"
env_path.parent.mkdir(parents=True, exist_ok=True)
