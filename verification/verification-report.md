# Oonmoon website verification

Prepared 10 October 2026. This website task performed no remote repository creation, push, deployment, purchase, App Store Connect change, credential creation or app-source edit.

## Deliverable

Website container: `/Users/ponddmini/Desktop/Oonmoon-Website`. The current user-created checkout and site root are nested at `/Users/ponddmini/Desktop/Oonmoon-Website/Oonmoon-Website`; its Git history and existing origin are preserved. No remote creation, push or publication was performed by this task.

Eleven static HTML URLs: neutral entry, plus Home, Features, Stories, Support and Privacy in both `/en/` and `/th/`. The app repository is separate. The original website asset baseline was verified on clean `main`, revision `59cdeb720555f65acb6b98428f14c186015e74b7`, version 0.7.8 (36).

Every localized page exposes its main content without JavaScript. Browser preference chooses the suggested language at the neutral entry; English is the fallback. An explicit choice is remembered in localStorage, and direct locale URLs never redirect. This avoids hiding localized content from crawlers.

## Completed checks

- Headless Chrome/Playwright: **46 checks passed, zero browser errors**. See `browser-checks.json` for details.
- All eleven pages: unique localized title/description, correct document language, one primary heading, main landmark, image alt attributes, working internal navigation and static English/Thai switch.
- All eleven pages at 320×568, 390×844, 768×1024, 1024×768 and 1440×900: **no horizontal overflow**.
- Thai/English browser preference, unsupported-language English fallback, remembered manual English override over Thai browser preference, same-page language switching, direct Thai URLs despite stored English, blocked storage and JavaScript disabled: passed. Independent JavaScriptCore checks also cover empty/ordered browser preferences and corrupt storage.
- Keyboard: first Tab exposes the skip link; Enter reaches main; native support disclosures open with Enter. Language controls remain in the sticky header. High-contrast focus styles and reduced-motion scrolling checked.
- Independent static audit: relative asset/navigation paths resolve from project subpaths; a synthetic HTTPS Pages subpath rebuild produced same-language self canonicals, reciprocal `en`/`th`/`x-default`, effective public robots output and eleven unique absolute sitemap URLs. Actual configuration remains unset and non-indexable.
- All accepted screenshot source hashes and character source hashes match the provided final manifests. Website variants preserve full landscape proportions, visible app caption/control regions and cutout alpha. Screenshots are simulator captures; they do not demonstrate physical-device testing.
- Known solid text/background colors meet 4.5:1 contrast in sixteen sampled pairs (lowest 5.29:1). Paper disclosure focus was corrected to a contrasting dark outline. Image-backed areas were visually inspected. This is an implementation review, not a formal accessibility certification or a complete assistive-technology audit.
- Desktop, mobile and tablet native PNG previews were captured after scrolling to load all lazy images. The moon, campfire, all-ten-story companions, real reader view and bookshelf were visually inspected. No decorative screenshot border/device shell or misleading portrait app UI.
- No remote fonts, analytics, advertising, cookies set by site code, backend or sign-in. Only explicit language preference is stored. Responsive image variants, lazy loading, async decoding and a small deferred script reduce transfer and rendering costs. Asset provenance and hashes accompany the source.

## Official references

Google and Apple guidance was verified from primary sources. Implementation choices follow [Google multilingual guidance](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites), [localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [robots scope](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), and [Apple marketing requirements](https://developer.apple.com/app-store/marketing/guidelines/). Additional source notes are in `official-guidance.md`.

Deployment instructions were checked against [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). App privacy and future hosting practices are separated, with a link to [GitHub’s privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). No hosting-log or retention guarantee is invented.

## Remaining owner decisions before publication

1. Supply the real HTTPS GitHub Pages URL, including its project subpath. Until then, metadata uses the reserved `example.invalid` placeholder and indexing is disabled. Run the documented rebuild with the actual address before publishing. For project sites, the project-path robots file is not authoritative at the host root; use host-root control/custom domain or submit the project sitemap separately.
2. Approve or revise privacy content and both languages: legal operator, effective date, intended markets, rights/contact procedures, support-message handling/retention, owner access to Apple platform reports, and actual hosting information. The privacy pages visibly remain drafts. Confirmed contact: `pondd.me@gmail.com`.
3. Approve final public content/artwork use. No App Store listing, price, launch date, reviews or store badge was invented. Add a real listing and Apple-provided localized badge only when appropriate.
4. Duo wording is design intent: selected simulator checks and layout improvements. Fold transitions, Split View and physical Duo remain unverified. Hardware is unreleased at this review date. No Apple certification or hardware guarantee.

Local implementation is complete. These are publication prerequisites and scope limitations, not failed website checks.


## Approved rounded-corner refinement

10 October 2026 (Asia/Bangkok): applied subtle rounded clipping to every foreground native screenshot on the website, and to the screenshot layers in the English/Thai social metadata composites. CSS radius adapts from 4 to 10 pixels; shadows, layout and proportions are retained, with no border. Five added browser checks verify all nine foreground placements across the five tested viewport sizes. Fresh desktop, mobile, tablet and both social images passed independent visual review; see `rounded-corners-audit.md`. Independent social-mask checks confirm only 92 extreme corner pixels acquire alpha; no source color pixels are altered outside those corner regions. The native source captures, website JPEG variants, forest and character cutouts remain byte-for-byte unchanged; all 32 original asset hashes still match the pre-refinement baseline. Revised marketing panel/overview exports are not required or copied: the website displays the still-valid native capture inputs directly.

Updated desktop/mobile/tablet previews and source ZIP replace the original Library files while preserving their identities. No publication or indexing change.

The app worker is separately updating navigation and language controls. Reconfirm final app claims and screenshot freshness against its next verified handoff before publication. Current website copy makes general feature claims and does not expose developer-only test access.
