# New Age refresh review

- Uses the official Start Bootstrap New Age distribution (MIT), vendored in `assets/new-age/`, plus app-specific colors and product artwork. No demo forms, remote fonts, tracking, or new runtime dependencies.
- Adds portfolio and app-directory links on every page and verified App Store links. Hosting and deployment settings are unchanged.
- Verified the live homepage exactly matched the source before editing.
- Static QA passed: every local link, anchor and asset resolves; every page has a heading and both portfolio links; no demo forms; `git diff --check`. Privacy/support body text and contact addresses are preserved (Oonmoon availability label updated separately).
- Browser preview sweep passed all pages at 320, 390 and 1365px: no persistent document overflow, broken loaded images or missing H1s. Visual samples covered Oonmoon English/Thai mobile and ReadSlip desktop. Oonmoon language navigation reached `/th/` with Thai content; Morse FAQ toggled closed/open using Enter. Local Chromium was unavailable, so these checks ran in an unpublished browser preview.
- Remaining QA limits: no axe/Lighthouse run, full external CTA navigation, real-device test or complete accessibility audit. Browser sweep and targeted interactions are not a substitute for owner review.
- No merge or production deployment performed.

## Rebuild
Run `python scripts/build.py`; the updated template preserves the New Age assets and links across all eleven English/Thai pages. Existing noindex configuration and historical support details are unchanged.
