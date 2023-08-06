# MetAIBricks : Meteorological AI Bricks

**Status (develop branch)**

[![Lines of Code](http://sonar.meteo.fr/api/project_badges/measure?project=metaibricks&metric=ncloc)](http://sonar.meteo.fr/dashboard?id=metaibricks) [![Maintenabilité Sonar](http://sonar.meteo.fr/api/project_badges/measure?project=metaibricks&metric=sqale_rating)](http://sonar.meteo.fr/dashboard?id=metaibricks) [![Fiabilité Sonar](http://sonar.meteo.fr/api/project_badges/measure?project=metaibricks&metric=reliability_rating)](http://sonar.meteo.fr/dashboard?id=metaibricks) [![Sécurité Sonar](http://sonar.meteo.fr/api/project_badges/measure?project=metaibricks&metric=security_rating)](http://sonar.meteo.fr/dashboard?id=metaibricks) [![Coverage](http://sonar.meteo.fr/api/project_badges/measure?project=metaibricks&metric=coverage)](http://sonar.meteo.fr/dashboard?id=metaibricks)

[![pipeline status](http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks/badges/dev/pipeline.svg)](http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks/-/commits/dev)

MetAIBricks is a package that allows you to easily train a neural network, by providing the basic development bricks you may need.

For now MetAIBricks allows you to download files through FTP and HTTP protocols.

## Installation

### Dependencies

* Python (>= 3.9.7)
* pydantic
* requests
* beautifulsoup4

**Note**: If you are using a conda environmment, it is recommended to manually install these dependencies through the command `conda install`. Else the dependencies will automatically be downloaded during the  installation via `pip`.

### User installation

To install MetAIBricks, simply :

```bash
pip install metaibricks
```

To install the latest development release from MF Nexus:

```bash
pip install --index-url http://nexm01-sidev.meteo.fr/repository/pypi-snapshots-metaibricks/simple --trusted-host nexm01-sidev.meteo.fr metaibricks
```

## Documentation

[MetAIBricks documentation](docs/home.md) contains :

* a [User documentation](docs/user_docs.md)
* a [Developper documentation](docs/dev_docs.md)

## Changelog

See the [changelog](CHANGELOG.md) for a history of notable changes to MetAIBricks.

## Development

### Important links

* Official source code repo: http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks
* Download releases: https://pypi.org/project/metaibricks/
* Issue tracker: http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks/-/issues
* [Developper documentation](docs/dev_docs.md)

### Source code

You can check the latest sources with the command:

```bash
git clone http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks.git
```

To install the MetAIBricks in dev-mode, checkout the [developper installation guide](docs/dev_docs.md#dev-installation).
