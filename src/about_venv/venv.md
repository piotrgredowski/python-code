## What is Venv in Python?

`venv` is a tool that creates isolated Python environments, allowing you to manage different sets of packages for different projects. Each environment acts as a sandbox, avoiding conflicts with the system-wide Python installation.

### Key Features:

- **Isolation**: Packages in a virtual environment won't affect the system Python or other environments.

- **Package Management**: Different package versions can be installed for each project.

- **Dependency Control**: Ensures project stability by defining specific package versions.

- **Activation/Deactivation**: Easily switch between environments for different projects.

- **Cross-platform Compatibility**: Works on various operating systems.

### How to Use `venv`:

1. Create a virtual environment: `python -m venv .venv`

2. Activate the environment:

   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

3. Deactivate: `deactivate`

### Differences between `conda env` and `venv`

- `venv`: Built-in, lightweight, Python-specific, uses `pip`, limited handling of native dependencies.
- `conda`: External, cross-platform, multi-language, uses `conda`, excels with native dependencies, popular in data science.

### Global, wide accessible environments

- `venv`: You can create a virtual environment with venv, install common packages using `pip`, and then reuse that environment for multiple projects. This approach allows you to maintain consistency between projects that need the same set of packages. But usage will be harder - you will need to know where activation script is located and run it manually.

- `conda`: Conda environments are well-suited for creating global reusable environments because they support multi-language packages and can handle complex dependencies more effectively. You can create an environment with the necessary packages using conda, and then use that environment as a base or template for different projects.
