# turms

[![codecov](https://codecov.io/gh/jhnnsrs/turms/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/jhnnsrs/turms)
[![PyPI version](https://badge.fury.io/py/turms.svg)](https://pypi.org/project/turms/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://pypi.org/project/turms/)
![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/turms.svg)](https://pypi.python.org/pypi/turms/)
[![PyPI status](https://img.shields.io/pypi/status/turms.svg)](https://pypi.python.org/pypi/turms/)
[![PyPI download month](https://img.shields.io/pypi/dm/turms.svg)](https://pypi.python.org/pypi/turms/)

### BETA

## Inspiration

Turms is a pure python implementation following the awesome graphql-codegen library with a similar extensible design.
It makes heavy use of pydantic and its serialization capablities and provides fully typed querys, mutations and subscriptions

## Supports

Schema Generation
- Enums
- Inputs
- Objects

Documents Generation
- Fragments
- Operations


## Features

- minimal, but fully documented code generation
- agnostic of graphql transport (gql, and rath examples)
- Autocollapsing operation functions
- Specify type mixins, configuration
- full support type hints for variables (Pylance)
- Compliant with graphl-config
- Support for custom scalars


## Installation

```bash
pip install turms
```

## Configuration

Turms configuration is compliant with the graphql-config specification, allowing interoperability with other frameworks.

```yaml
projects:
  default:
    schema: http://api.spacex.land/graphql/
    documents: graphql/**.graphql
    extensions:
      turms: # path for configuration for turms
        out_dir: examples/api
        stylers:
          - type: turms.stylers.capitalize.CapitalizeStyler
          - type: turms.stylers.snake_case.SnakeCaseStyler
        plugins:
          - type: turms.plugins.enums.EnumsPlugin
          - type: turms.plugins.inputs.InputsPlugin
          - type: turms.plugins.fragments.FragmentsPlugin
          - type: turms.plugins.operations.OperationsPlugin
          - type: turms.plugins.funcs.FuncsPlugin
        processors:
          - type: turms.processors.black.BlackProcessor
          - type: turms.processors.isort.IsortProcessor
        scalar_definitions:
          uuid: str
          timestamptz: str
          Date: str
```

## Run 

```bash
turms gen
```


Turms configuration is based on plugins that can be configured in the graphql.config. There exist three major classes:

### Stylers

Stylers are responsible for applying different styles to the class names and field names (e.g. snakecasing of graphqls pascalcase),
they are chained in order of notation in the graphql config (they receive the output of the last styler). Turms takes care of automatically
aliasing these names if they are not the same as the graphql style)

### Plugins

Plugins are the generators of code, that traverse through the direcotry and ad new ast nodes to the global tree. Examplary pluings are:

- turms.plugins.enums.EnumsPlugin
- turms.plugins.inputs.InputsPlugin
- turms.plugins.fragments.FragmentsPlugin
- turms.plugins.operations.OperationsPlugin
- turms.plugins.funcs.FuncsPlugin

## Parsers

Parsers take the generated python.AST, and can parse this code. (e.g enabling polyfills for different python versions)
Includes Parsers are

- turms.parsers.polyfill.PolyfillParser (only working for python 3.7)

## Processors

Processors take the generated code (already a string), and can parse this code. (e.g. black processor for enforcing black style formatting) or isort of sorting imports.
Includes Processors are

- turms.processor.black.BlackProcessor
- turms.processor.isort.IsortProcessor

## Usage

Open your workspace (create a virtual env), in the root folder

```bash
turms init
```

This creates a graphql-config compliant configuration file in the working directory, edit this to reflect your settings (see Configuration)

```bash
turms gen
```

Generate beautifully typed Operations, Enums,...

### Why Turms

In Etruscan religion, Turms (usually written as 𐌕𐌖𐌓𐌌𐌑 Turmś in the Etruscan alphabet) was the equivalent of Roman Mercury and Greek Hermes, both gods of trade and the **messenger** god between people and gods.

## Transport Layer

Turms does *not* come with a default transport layer but if you are searching for an Apollo-like GraphQL Client you can check out [rath](https://github.com/jhnnsrs/rath), that works especially well with turms.

## Examples

This github repository also contains an example graphql.config.yaml with the public SpaceX api, as well as a sample of the generated api.

## Experimental

```bash
turms watch $PROJECT_NAME
```

Turms watch is able to automatically monitor your graphql folder for changes and autogenerate the api on save again.
Requires additional dependency for watchdog

```bash
pip install turms[watch]
```
