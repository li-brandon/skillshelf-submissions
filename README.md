# SkillShelf Submissions

This repository collects community submissions for [SkillShelf](https://skillshelf-eight.vercel.app), a library of Grok Bot skills.

Every skill on SkillShelf starts as a pull request here. Once a submission is reviewed and merged, it can be published to the site with credit to its author.

## How to submit a skill

1. **Fork** this repository to your own GitHub account.
2. **Copy the template**: duplicate `submissions/_TEMPLATE.md` to `submissions/<slug>.md`, where `<slug>` is a short, lowercase, hyphenated name for your skill (for example, `submissions/daily-news-digest.md`).
3. **Fill in every field** in the YAML front matter and paste the full skill into the `## Skill text` section. See the field reference below.
4. **Open a pull request** against `main`. The PR template includes a short checklist. Please complete it.
5. An automated check (`validate`) will confirm that your file has all required fields. Fix any errors it reports, then a maintainer will review your submission.

## Requirements

- **The skill must be public.** The `source` field must link to a publicly accessible copy of the skill (for example, a GitHub repo, gist, or public page).
- **The skill must have an open license** that allows SkillShelf to redistribute it, such as `MIT`, `CC0-1.0`, `CC-BY-4.0`, or `Apache-2.0`. Use an [SPDX identifier](https://spdx.org/licenses/) where possible.
- **You must have the right to submit it.** Either you wrote it, or its license permits redistribution and you credit the original author.
- **Authors are credited.** The `author` field is shown on SkillShelf alongside the skill. Use your GitHub username or a name you are happy to have displayed publicly.
- **No personal contact details.** Do not include email addresses, phone numbers, or other private information anywhere in a submission.

## Field reference

| Field         | Type             | Description                                                               |
| ------------- | ---------------- | ------------------------------------------------------------------------- |
| `name`        | string           | Human-readable name of the skill.                                         |
| `slug`        | string           | Lowercase, hyphenated identifier. Must match the file name (without `.md`). |
| `description` | string           | One or two sentences describing what the skill does.                      |
| `connectors`  | list of strings  | Connectors or integrations the skill relies on (for example, `web-search`). Use `[none]` if it needs none. |
| `license`     | string           | License of the skill text, ideally an SPDX identifier (`MIT`, `CC0-1.0`, ...). |
| `source`      | URL              | Public URL where the original skill lives.                                |
| `author`      | string           | Name or GitHub username to credit.                                        |
| `lastTested`  | date             | Date you last confirmed the skill works, in `YYYY-MM-DD` format.          |

The body must contain a `## Skill text` section with the full, copy-pasteable skill.

## Validating locally

```sh
pip install pyyaml
python .github/scripts/validate.py
```

## Questions and contact

Please use [GitHub issues](../../issues) for questions, bug reports, takedown requests, or anything else. There is no email contact for this project.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detail.

## License

The repository tooling and documentation are released under the [MIT License](LICENSE). Each submitted skill is licensed under the license stated in its own `license` field.
