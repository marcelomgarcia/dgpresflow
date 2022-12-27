# Digital preservation workflow

import click
import dgplib as dglib
import pprint
import configparser


@click.command()
@click.argument("config_file", type=click.Path(exists=True))
def main(config_file) -> None:
    """Digital Preservation Workflow main routine."""

    # Read configuration file
    config = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    config.read(config_file)

    accessionFlow = dglib.mk_accession(config)

    pprint.pprint(accessionFlow)


if __name__ == "__main__":
    main()
