import shutil
from pathlib import Path
from datetime import datetime
import sys


def backup_files(source_directory, backup_directory):

    source = Path(source_directory)
    backup = Path(backup_directory)

    backup.mkdir(exist_ok=True)

    log_file = backup / "backup_log.txt"

    for file in source.iterdir():

        if file.suffix in [".csv", ".json"]:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            new_name = f"{file.stem}_{timestamp}{file.suffix}"

            dest = backup / new_name

            shutil.copy2(file, dest)

            with open(log_file, "a") as log:
                log.write(f"Copied {file.name} -> {new_name}\n")

            # keep only last 5 backups
            backups = sorted(backup.glob(f"{file.stem}_*{file.suffix}"))

            if len(backups) > 5:
                for old_file in backups[:-5]:
                    old_file.unlink()

                    with open(log_file, "a") as log:
                        log.write(f"Deleted old backup {old_file.name}\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python Part-B_AM.py <source_dir> <backup_dir>")
    else:
        source_dir = sys.argv[1]
        backup_dir = sys.argv[2]
        backup_files(source_dir, backup_dir)
