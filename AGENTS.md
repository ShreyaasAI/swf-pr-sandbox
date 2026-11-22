# slugify keeps repeated spaces and capitals

Small Python library used as a seeded bug for the SWF agent evaluation.
Run the tests with pytest. Keep fixes minimal; do not modify tests.

```yaml agent-config
image: python:3.12-slim
setup:
  - "python -m pip install --quiet pytest==9.2.0"
test: python -m pytest -q
allow:
  - "python -m pytest*"
resources:
  memory_mb: 512
  cpus: 0.5
```
