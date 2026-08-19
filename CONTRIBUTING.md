# Contributing

Thanks for considering a contribution to image-manipulation.

## Getting set up

```bash
git clone https://github.com/oniforo/image-manipulation.git
cd image-manipulation
python -m venv venv
venv\Scripts\activate   # on Windows
pip install Pillow
```

## Making a change

1. Create a branch off `main`: `git checkout -b feat/short-description`
2. Make your change
3. Run `python main.py` against the `images/` folder to confirm it still
   produces the expected output in `resized/` and `thumbnails/`
4. Commit with a clear message (Conventional Commits preferred:
   `feat: ...`, `fix: ...`, `docs: ...`)
5. Open a pull request against `main` and fill in the PR template

## Reporting bugs / requesting features

Use the issue templates — they ask for the details that make an issue
actionable (repro steps, expected vs. actual behavior, environment).

## Code style

No linter/formatter is configured yet; keep changes consistent with the
existing style in `manipulate.py`.

## Questions

Open an issue if you're not sure something counts as a bug.
