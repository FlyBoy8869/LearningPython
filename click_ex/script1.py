import click


@click.command()
@click.argument("name")
@click.argument("last", required=False, default="")
def say_hello(name, last):
    click.echo(f"Hello, {name} {last}.")


if __name__ == "__main__":
    say_hello()
