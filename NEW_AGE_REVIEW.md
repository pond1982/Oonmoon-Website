# New Age refresh review

- Uses the official Start Bootstrap New Age distribution (MIT), vendored in `assets/new-age/`, plus app-specific colors and product artwork. No demo forms, remote fonts, tracking, or new runtime dependencies.
- Adds portfolio and app-directory links on every page and verified App Store links. Hosting and deployment settings are unchanged.
- Verified the live homepage exactly matched the source before editing.
- Static QA passed: every local link, anchor and asset resolves; every page has a heading and both portfolio links; no demo forms; `git diff --check`. Privacy/support body text and contact addresses are preserved (Oonmoon availability label updated separately).
- Browser, responsive visual, keyboard and screenshot checks are NOT complete: local Chromium aborts on `socket() failed: Operation not permitted`, including escalated execution. Keep this PR draft until browser review. CSS provides mobile breakpoints, focus states and reduced-motion handling, but those require browser verification.
- No merge or production deployment performed.

## Rebuild
Run `python scripts/build.py`; the updated template preserves the New Age assets and links across all eleven English/Thai pages. Existing noindex configuration and historical support details are unchanged.
