#Create venv
python -m venv venv

# Init git
git init

# Run local postgres container
Start docker desktop
docker run --name local-postgres ^
  -e POSTGRES_USER=youruser ^

  -e POSTGRES_PASSWORD=yourpassword ^
  -e POSTGRES_DB=yourdb ^
  -p 5432:5432 ^
  -d postgres:latest

# Run migrations
python scripts/run_migrations.py

