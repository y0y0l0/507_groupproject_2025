# Contributing to HHA507 Group Project

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a new branch for your work: `git checkout -b feature/your-feature-name`

## Workflow

### For Data Work
1. Place raw data in `data/raw/`
2. Document data sources in `docs/data_dictionary.md`
3. Create data processing scripts in `src/data_processing/`
4. Save processed data to `data/processed/`

### For Analysis
1. Use Jupyter notebooks in `notebooks/` for exploration
2. Create reusable functions in `src/analysis/`
3. Document your findings

### For Visualizations
1. Add visualization functions to `src/visualization/plots.py`
2. Use consistent styling (provided by `setup_style()`)
3. Save important plots with descriptive names

## Code Standards

### Python Style
- Follow PEP 8 style guidelines
- Use descriptive variable names
- Add docstrings to all functions
- Keep functions focused and small

### Documentation
- Update README.md if you add new features
- Comment complex code sections
- Keep the project plan updated

### Testing
- Add tests for new functions in `tests/`
- Run tests before committing: `pytest tests/`
- Ensure tests pass before pushing

## Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Update, Fix, Remove)
- Example: "Add function to calculate patient statistics"

## Pull Requests
1. Ensure your code works and tests pass
2. Update documentation as needed
3. Create a pull request with a clear description
4. Request review from team members

## Communication
- Discuss major changes with the team before implementing
- Use issues to track tasks and bugs
- Be respectful and collaborative

## Questions?
If you have questions, reach out to your team members or instructor.
