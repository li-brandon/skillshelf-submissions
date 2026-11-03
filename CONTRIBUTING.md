# Contributing to SkillShelf

Thanks for helping grow [SkillShelf](https://skillshelf-eight.vercel.app), the community library of Grok Bot skills.

## Submitting a new skill

1. Fork this repository.
2. Copy `submissions/_TEMPLATE.md` to `submissions/<slug>.md`.
3. Fill in all front matter fields and the `## Skill text` section.
4. Run the validator locally (optional, but it saves a round trip):

   ```sh
   pip install pyyaml
   python .github/scripts/validate.py
   ```

5. Open a pull request and complete the checklist.

One skill per file, and ideally one skill per pull request.

## Submission guidelines

- **Public and licensed.** The skill must be publicly available at the `source` URL and released under a license that allows redistribution (MIT, CC0-1.0, CC-BY-4.0, Apache-2.0, etc.).
- **Credit the author.** Put the original author in `author`. If you are submitting someone else's skill, make sure its license allows it and link to the original in `source`.
- **Slug rules.** Lowercase letters, digits, and hyphens only. The slug must match the file name.
- **Keep it accurate.** `description` and `connectors` should reflect what the skill actually does and needs. Set `lastTested` to the date you last confirmed it works.
- **No private data.** Never include email addresses, phone numbers, API keys, tokens, or other secrets or personal information.
- **Be safe and respectful.** Skills that are designed to deceive, harass, spam, or cause harm will not be accepted.

## Updating an existing skill

Open a pull request editing the existing `submissions/<slug>.md` file. Bump `lastTested` if you re-tested it. If you are not the original author, explain the change in the PR description.

## Removing a skill

If you are the author of a listed skill and want it removed, open a GitHub issue with a link to the submission file.

## Review process

1. The `validate` workflow checks every submission for required fields.
2. A maintainer reviews the skill for quality, licensing, and safety.
3. Once merged, the skill becomes eligible for listing on SkillShelf.

## Contact

All communication happens through [GitHub issues](../../issues) and pull requests. There is no email contact for this project.
