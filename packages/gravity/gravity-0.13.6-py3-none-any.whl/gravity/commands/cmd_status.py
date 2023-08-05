import click

from gravity import process_manager


@click.command("status")
@click.pass_context
def cli(ctx):
    """Display server status."""
    with process_manager.process_manager(state_dir=ctx.parent.state_dir, start_daemon=False) as pm:
        pm.status()
