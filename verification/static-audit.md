# Independent static audit

Reviewed and rechecked after corrections on 10 October 2026. Scope: `site-stage` HTML, content JSON, privacy/support JSON, CSS, JavaScript, generator, image provenance, and fixed-color contrast. No app files or deployment destinations were changed by the auditor. All findings below are resolved. This is a static/source audit, not formal accessibility certification or physical-device testing.

## Passed

- Eleven complete HTML documents exist: the language gateway and Home, Features, Stories, Support, and Privacy in both English and Thai. All have meaningful content before JavaScript runs, one `main`, one `h1`, a skip link, semantic navigation, and an always-visible language switch in the source/CSS.
- English and Thai content have identical key sets, five localized titles/descriptions, six feature cards, ten story names/notes, five support questions, and the corresponding privacy sections. The locale documents declare `lang="en"` or `lang="th"`; every image has an `alt` attribute, including intentionally empty decorative brand-icon alt text.
- All ordinary HTML `href`, `src`, `srcset`, and fragment references resolve. No ordinary asset or navigation path begins at the domain root. Nested English/Thai page switches preserve the current page.
- Every document has a self canonical, reciprocal English and Thai alternates, `x-default`, localized Open Graph/Twitter title, description and alt metadata. The real deployment URL remains unconfigured (`base_url: null`); preview pages use the reserved `example.invalid` placeholder, `noindex,follow`, visible local-preview text, and robots disallow.
- In an isolated temporary copy, the generator successfully produced all eleven public documents using the synthetic test URL `https://audit.example/Oonmoon-Website/`. Self canonicals, reciprocal alternates, `x-default`, `index,follow`, eleven unique sitemap URLs, and the robots sitemap entry retained that project subpath. Resetting that temporary copy to preview restored robots disallow. The delivered staging config was not changed by this test.
- Eleven JavaScript scenarios passed in macOS JavaScriptCore: Thai and English first-visit browser preferences; unsupported and empty-language English fallback; `navigator.language` fallback; first supported ordered browser language; explicit stored English/Thai overrides; invalid stored preference; blocked storage; and an explicit locale URL. No storage write happens before an explicit click. Manual switches and Continue save only `en` or `th`. Locale pages do not redirect.
- The language scenarios were rerun against the final JavaScript, including an assertion that the suggested Continue link declares the selected language for screen readers. The public project-subpath build was also rerun against the final generator in an isolated temporary copy; all eleven metadata rows and sitemap/robots checks passed again.
- CSS provides visible keyboard focus, keyboard-native links and disclosure summaries, responsive layouts, and a reduced-motion media query that disables smooth scrolling and hover motion. No carousel or custom keyboard widget requires extra scripting.
- All 32 image derivatives match their provenance source/output SHA-256 hashes and byte sizes. Their dimensions preserve source aspect ratios to pixel-rounding tolerance. Sixteen screenshot derivatives use accepted `-ImageIO.png` source captures; thirteen original character derivatives represent all ten stories. No app source edit, device-frame insertion, screenshot crop, stretch, or replacement UI is part of the asset preparation.
- The app remains Coming soon, with no invented price, App Store URL/badge, testimonial, launch date, learning/sleep guarantee, Apple endorsement or certification. Duo wording describes design intent and selected simulator checks and explicitly keeps fold transitions, Split View and physical hardware unverified.
- Privacy is visibly an owner-review draft. It distinguishes audited app behavior from support email, browser localStorage, Apple services, and prospective GitHub Pages hosting. It does not promise that hosts collect no visitor data, invent retention periods, or claim a final legal operator/effective date. Confirmed public contact is `pondd.me@gmail.com`.

## Resolved findings

1. **Social images:** English and Thai JPEGs now exist, both verified at 1200×630. All eleven documents' social image references resolve.
2. **Language of parts:** gateway Thai eyebrow/status fragments have `lang="th"`; JavaScript assigns the selected language to Continue. New external privacy-notice labels are localized on the Thai page.
3. **Image dimensions:** all character images now use the accurate proportional dimensions from asset provenance. The final HTML dimensions were checked against that manifest, including nonsquare images.
4. **Heading order:** Features cards now use `h2` after their page `h1`; Home retains `h3` below its section `h2`.
5. **Support copy:** the duplicate introductory sentence was removed in both languages.
6. **Privacy review:** both privacy drafts now explicitly retain the unresolved owner access to Apple-provided analytics, sales/download reports, and diagnostics, separately from embedded app analytics.
7. **FAQ keyboard focus:** the initially pale outline on the paper background was corrected to `#315f67`. Final CSS contains the summary-specific focus rule; its contrast against paper is 6.47:1.

## Fixed-color contrast checks

Ratios use the WCAG relative-luminance formula. All sixteen sampled solid text/background pairs exceed 4.5:1 for ordinary text; the lowest is the feature number at 5.29:1. Focus outlines exceed 3:1 against the sampled adjoining backgrounds. Images, translucent artwork overlays, rendered app UI text, and every possible antialiasing/zoom state are outside this fixed-color calculation.

| Text or indicator | Foreground / background | Ratio |
| --- | --- | ---: |
| Paper body | `#183c47` / `#fbf4e5` | 10.79:1 |
| Paper secondary | `#49626a` / `#fbf4e5` | 5.92:1 |
| Feature secondary | `#49626a` / `#fffaf1` | 6.24:1 |
| Feature number | `#536f62` / `#fffaf1` | 5.29:1 |
| Included badge | `#2f5844` / `#e7efe4` | 6.87:1 |
| Full-library badge | `#6b5941` / `#efe8d9` | 5.50:1 |
| Draft note body | `#183c47` / `#f4e4c4` | 9.43:1 |
| Night body | `#fbf4e5` / `#102c3d` | 13.23:1 |
| Navigation | `#e3e6dd` / `#0d2738` | 12.19:1 |
| Active navigation | `#f4cf87` / `#0d2738` | 10.35:1 |
| Coming-soon status | `#ffe1a0` / `#163b4c` | 9.37:1 |
| Gold button | `#0c2230` / `#f4cf87` | 10.97:1 |
| Paper button | `#fbf4e5` / `#183c47` | 10.79:1 |
| Footer body | `#ced9d4` / `#0c2230` | 11.27:1 |
| Footer credits | `#b1c6c2` / `#0c2230` | 9.11:1 |
| Local-preview note | `#d1b987` / `#0c2230` | 8.55:1 |
| Focus on dark | `#fff3b6` / `#102c3d` | 12.93:1 |
| Paper link/FAQ focus | `#315f67` / `#fbf4e5` | 6.47:1 |

## Limits and publication prerequisites

No obvious source-level accessibility blocker remains in this scope. The separately generated `browser-checks.json` records passing navigation, five viewport sizes with no horizontal overflow on all eleven routes, static content without JavaScript, language behavior, reduced motion, keyboard skip navigation and FAQ disclosure, previews, and console/response checks. Those are the implementation owner's browser checks, rather than independent accessibility certification. The forest illustration and mobile preview were visually inspected by this auditor; the visible moon/campfire panorama alt text describes the supplied artwork accurately.

Publishing remains unperformed. Before indexing, configure the actual owner-controlled HTTPS URL and complete the stated owner/content/privacy approval. Legal operator, effective date, intended markets/rights procedures, support retention/handling, owner access to platform reports, and actual hosting details remain owner decisions. Physical Duo, fold transitions, and Split View remain unverified as the site states.
