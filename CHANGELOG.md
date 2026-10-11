# Changelog

All notable changes to the DataBank IMX Python Developer Training repository are documented here.

## Rules and Conventions

This file follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### What gets a changelog entry

- New files, chapters, or supplemental topics
- Structural or organizational changes to the repository
- Lesson runner changes
- Major content updates (new Python version coverage, significant lesson rewrites)
- Major policy changes

### What does not

- Prose edits, typo fixes, and minor wording improvements within existing documents
- Formatting-only changes

---

## [Unreleased]

### Added

- `.github/` structure: `CODEOWNERS`, `instructions/copilot-instructions.md`, `instructions/sonarqube_mcp.instructions.md`, `workflows/sonarqube.yml`, `workflows/standards-policy.yml`, `standards.yml`
- `sonar-project.properties` - excludes all `textbook-downloads/` folders from SonarQube analysis and coverage
- `.github/standards.yml` - excludes all `textbook-downloads/` folders from the standards-policy checker

---

## [1.0.0] - 2026-10-10

### Added

- Repository structure: `part-i-basics/`, `part-ii-projects/`, `part-iii-beyond-the-book/`, `lesson-runner/`, `resources/setup/`
- `README.md` - full project README modelled on the C# training repository
- `CHANGELOG.md` - this file
- `development-rules-of-engagement.md` - shared policy document covering custom code obligations
- Migrated from personal repository (`python-crash-course`) to DataBank IMX organization

[Unreleased]: https://github.com/databankimx/training-python/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/databankimx/training-python/releases/tag/v1.0.0
