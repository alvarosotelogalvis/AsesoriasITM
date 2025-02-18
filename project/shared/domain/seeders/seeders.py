from project.shared.domain.seeders import *

from flask.cli import with_appcontext
import click
import logging
import traceback

log = logging.getLogger('application.commands')


@click.command("dbseed")
@click.option(
    "--class",
    "class_name",
    type=str,
    default=None,
    help="Specifies the class to be executed"
)
@with_appcontext
def run_seeders(class_name):
    seeders = [
        professorSeeder,
        ScheduleSeeder
    ]
    try:
        if not class_name:
            click.echo("Starting seeders processing")
            for seeder in seeders:
                seeder().handle()
            click.echo("Seeders finished")
        elif eval(class_name) in seeders:
            click.echo("Starting seeders processing")
            eval("{}().handle()".format(class_name))
            click.echo(f"Seeders {class_name} processed")
    except NameError:
        click.echo("Seeder not recognized")
    except Exception as error:
        log.error(
            "Error in module RunSeeders: {} - Line: {}".format(
                error, traceback.format_exc())
        )
        click.echo(error)
