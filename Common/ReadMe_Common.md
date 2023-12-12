# Common

## Overview
The `Common` app serves as a shared space for common utilities, models, and functions that are used throughout the Project-Musica. It provides a centralized repository for code that is agnostic to the specific functionalities of other apps but is essential for their operations.

## Features
- Shared Models: Central definitions for models that are used across multiple apps.
- Utility Functions: A collection of helper functions and utilities that can be imported and used in various contexts.
- Constants: Definitions of constants that are relevant across the entire project.
- Shared Templates: Common templates or template tags that can be included or extended in app-specific templates.
- Middleware: Common middleware classes that are applied globally across all requests and responses.

## Configuration
The `Common` app requires minimal configuration, as it mostly provides support to other apps. However, you might need to configure the following:

- `SHARED_SETTINGS`: A dictionary in `settings.py` that contains configurations used across different apps, such as date and time formats, pagination settings, or default permissions.
- `TEMPLATE_DIRS`: If the `Common` app includes shared templates, ensure they are correctly referenced in the `TEMPLATES` configuration in `settings.py`.

## Usage
The components within the `Common` app can be imported into other apps as follows:

```python
from Common.utilities import some_utility_function
from Common.models import SharedModel
