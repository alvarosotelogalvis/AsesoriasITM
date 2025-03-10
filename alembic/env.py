from project.shared.config.database import Base
from project.shared.config.createTables import get_tables

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from dotenv import load_dotenv
from alembic import context

import os

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
get_tables()
load_dotenv()
config = context.config
section = config.config_ini_section
config.set_section_option(section, "DB_USERNAME", os.getenv("DB_USERNAME"))
config.set_section_option(section, "DB_PASSWORD", os.getenv("DB_PASSWORD"))
config.set_section_option(section, "DB_HOST", os.getenv("DB_HOST"))
config.set_section_option(section, "DB_PORT", os.getenv("DB_PORT"))
config.set_section_option(section, "DB_DATABASE", os.getenv("DB_DATABASE"))
config.set_section_option(section, "DB_SSL_PEM_CA", "")

# DB_SSL_PEM_CA = os.getenv("DB_SSL_PEM_CA", "mysql-ssl-ca.crt.pem")
# if os.path.exists(DB_SSL_PEM_CA):
#     config.set_section_option(section, "DB_SSL_PEM_CA", f"?ssl_ca={DB_SSL_PEM_CA}")


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [Base.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def exclude_tables_from_config(config_):
    tables_ = config_.get("tables", None)
    if tables_ is not None:
        tables = tables_.split(",")
    return tables

# Exclude Models from Views
exclude_tables = [
    "survey_question_view"
]

def include_object(object, name, type_, *args, **kwargs):
    return not (type_ == 'table' and name in exclude_tables)



def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        include_object=include_object,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print(f"config.config_ini_section: {config.config_ini_section}")
    print(f"config.config_ini_section: {config.get_section(config.config_ini_section)}")
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
