from pathlib import Path

# roots
root = Path(__file__).parent.parent.parent
data = root / "data"

# logs
log_file: Path = data / "logs" / "app.log"
log_file.parent.mkdir(parents=True, exist_ok=True)
log_file.touch()

# env file
env_path = data / ".env"
env_path.parent.mkdir(parents=True, exist_ok=True)

# cache directory and files
cache_dir = data / "cache"
cache_dir.mkdir(parents=True, exist_ok=True)

cache_files = [
    cache_dir / "repos.json",
    cache_dir / "stats.json",
    cache_dir / "lang_stats.json",
]
for file in cache_files:
    file.touch()


# summary file
def get_summary_path(username: str) -> Path:
    summary_file = data / "output" / f"summary_{username}.json"
    summary_file.parent.mkdir(parents=True, exist_ok=True)

    return summary_file
