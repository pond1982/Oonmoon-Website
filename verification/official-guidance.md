# Oonmoon website: official guidance checked 2026-10-10

This is an implementation note for the local, unpublished bilingual website. App-specific test coverage below is supplied by the task; public Apple documentation does not verify Oonmoon compatibility.

## Bilingual static pages

- Publish full English and Thai HTML at separate URLs, such as `en/features/` and `th/features/`. Translate main content, navigation, headings and metadata. Keep each localized URL available directly and without JavaScript. Google recommends language-specific URLs and visible language-switch links; Googlebot normally sends no `Accept-Language`. Do not redirect explicit language URLs based on inferred preferences. [Google multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- Set each document's `lang` to `en` or `th` for accessibility. Google determines language from visible content, so `lang` alone does not replace translation. [Google multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- Every translated pair needs an identical alternate set in the static `<head>`: itself, its counterpart and `x-default`. Use `en` and `th`, and fully qualified HTTPS URLs. Links must be reciprocal. `x-default` may target the English counterpart as fallback, or a meaningful neutral language gateway; it works particularly well with selectors. [Google localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Give each localized page its own same-language, self-referencing canonical. Keep canonical separate from hreflang, and keep HTML, sitemap and internal URL conventions consistent. Do not canonicalize all Thai pages to English. [Google canonical guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- Generate sitemap URLs from one configurable base URL that includes the GitHub Pages project path, if any. Sitemap URLs must be absolute and UTF-8 encoded. Regenerate after the final address is known; never publish an example-domain sitemap as if it were real. [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

## First-visit preference recommendation

Recommended implementation inference: apply browser preference only at a neutral entry point. Keep `/en/` and `/th/` authoritative even when a stored preference differs, so links remain shareable and crawlers can reach both versions. A static gateway with language links plus a preferred-language suggestion most closely follows Google's warning against automatic language redirects. If initial root navigation is used to satisfy the requested first-visit preference, retain meaningful static fallback and links, and never redirect locale pages. Avoid crawler-specific behavior.

Use the browser's ordered language list, match `en`/`th` primary subtags, and use English if no supported language is found. An explicit switch takes priority on future neutral entries. Store only that language choice, catch blocked-storage failures, and preserve the same page when switching. Test Thai, English, unsupported/empty browser lists, saved manual choice, direct language links and JavaScript-disabled access. These behavior details are implementation decisions, not Google mandates.

## GitHub Pages robots caveat

Include a permissive `robots.txt` and sitemap instruction in the source. Google checks robots at the host root; `/project/robots.txt` is not authoritative. For a project site at `username.github.io/project/`, document that the owner needs host-root control (user site or custom domain) to serve effective robots, and can submit the project sitemap in Search Console. Do not claim the project file controls crawling. [Google robots specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec)

## Apple badges, imagery and wording

- Keep plain text “Coming soon” until the real Oonmoon listing is supplied. Apple's pre-order badge is for an app actually available to pre-order; the download badge belongs with the released listing. Use Apple's provided localized artwork only, preserve its design, and link the real product page. No fabricated store button, badge or Apple logo. [Apple marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
- When approved badges are eventually added, allow at least 40 px onscreen height and clear space of one-quarter the badge height. Apple product imagery must follow Apple's separate rules; avoid invented device shells. Plain landscape Oonmoon screen captures keep this design centered on the actual app. [Apple marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
- Keep `iPhone`, `iPad`, `iPhone Duo` and `App Store` in English in Thai copy. Use correct product-name capitalization and an Apple trademark credit in the legal area. A worldwide website should use the international credit format, with no U.S.-only trademark symbols. [Apple marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
- Apple word marks may be used referentially, subordinate to Oonmoon, without implying endorsement. Broad compatibility claims require the app to actually work with the referenced product. Do not imply certification, sponsorship or approval. [Apple trademark guidance](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)

## iPhone Duo claim

Apple's current product page states availability begins October 23, 2026, so general hardware release is still ahead of the October 10 review date. Apple's design talk covers adaptation across poses, inner/outer displays and fold avoidance. Neither source validates Oonmoon. [Apple iPhone Duo](https://www.apple.com/iphone-duo/), [Apple design talk](https://developer.apple.com/videos/play/tech-talks/111466/)

Safe project wording: “Designed with iPhone Duo in mind.” Keep a nearby qualification explaining selected simulator checks and adaptive-layout work. Task-supplied evidence: Oonmoon 0.7.8 has window, safe-area and division-aware improvements; selected simulator tests were completed. Fold transitions, Split View and physical Duo remain unverified. Avoid “fully compatible,” “fully tested,” “Apple certified,” and promised behavior on unreleased hardware. The design-intent phrase is an evidence-based project description, not an Apple-approved certification phrase.

## Before publication

Configure the actual base URL, regenerate metadata/sitemap, inspect every en/th page, verify reciprocal annotations and root/subpath links, and obtain owner approval for privacy/content. Distinguish verified app practices from GitHub hosting practices; do not invent hosting-log guarantees. No remote repository, publishing, purchase, App Store Connect change or app-source edits are required for this local deliverable.


## GitHub deployment and hosting references checked 2026-10-10

GitHub documents publishing from `main` and repository root with branch deployment: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

Hosting processing is separate from app local data: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement. This link is informational; actual host details and owner practices still require confirmation.
