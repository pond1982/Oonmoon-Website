# Oonmoon Website

Standalone English and Thai static website, separate from the Oonmoon app. Prepared locally on 10 October 2026. Nothing has been published, and no remote repository has been created.

## Preview

Open `index.html` directly, or serve the project locally:

```sh
cd /Users/ponddmini/Desktop/Oonmoon-Website
python3 -m http.server 8080 --bind 127.0.0.1
```

Visit `http://127.0.0.1:8080/`. Serving is preferable for testing browser storage. The site has no build-time package dependencies, backend, account, analytics, advertising or remote fonts. Every page is complete HTML.

## Pages and language behavior

- `/` is a static bilingual language entry. Browser preference suggests English or Thai on the first visit; an unclear or unsupported preference falls back to English. It never forces a redirect.
- `/en/` and `/th/` each have Home, Features, Stories, Support and Privacy pages. The always-visible language links switch to the same page in the other language.
- Only an explicit language choice is stored, in browser `localStorage` under `oonmoon-language`. Stored choice guides future visits to `/`. Direct locale URLs stay authoritative. Blocked storage and disabled JavaScript preserve usable static links and content.
- Canonical, reciprocal `en`/`th` and `x-default` annotations are rendered into HTML. Each localized page has its own canonical. The home `x-default` is `/`; other pages use their English counterpart.

## Configure the real address

The real GitHub Pages address is unknown. `site.config.json` deliberately has `base_url: null` and `public_indexing: false`. Preview metadata uses the reserved `https://example.invalid/oonmoon/` placeholder, `noindex,follow`, and a blocking preview robots file. **Do not publish that configuration.**

Once the owner knows the actual address, replace the sample below with it, including the project subpath. These examples are instructions, not an assertion of a real Oonmoon domain.

```sh
python3 scripts/build.py --base-url https://YOUR-USER.github.io/YOUR-REPO/ --public
```

For a custom domain, use its actual HTTPS root instead. The command rebuilds all HTML, social URLs, robots and sitemap from one base URL. Run it again after changes to `content.json`, `privacy-support.json` or configuration. `--preview` returns to non-indexable preview mode. Images and navigation use relative paths, so they work at both a host root and a Pages project subpath.

The privacy draft still needs owner/content approval: legal operator, effective date, markets/rights procedures, mailbox handling, platform reports, hosting information, and both policy languages. `privacy_owner_approved` is informational; changing it does not approve or rewrite the policy. Update the actual privacy text and draft status only after the owner's review. The confirmed support/privacy contact is `pondd.me@gmail.com`.

## Publish later with GitHub Pages

1. Review the privacy/content decisions above and supply a real App Store listing only when one exists. The current site uses plain Coming soon text, without a fabricated badge, price or listing link.
2. Create the desired GitHub repository yourself. Keep this website separate from the app repository. The local project has a `main` branch and no remote.
3. Configure the actual URL and rebuild as above. Confirm `site.config.json`, every canonical/hreflang URL and `sitemap.xml` use that real address; check the site at a project subpath.
4. Add the remote you chose, then push `main` using your own GitHub authentication. No credentials are included or created by this project.
5. In GitHub repository Settings → Pages, choose Deploy from a branch, `main`, and `/ (root)`. The `.nojekyll` file makes the site serve as plain static files. Keep the project root contents at the repository root.
6. When GitHub reports the published address, verify both languages, images, support email and privacy URL at that address. This site work does not update the app or App Store Connect.
7. Submit the real sitemap in Google Search Console if desired. A project site's `/YOUR-REPO/robots.txt` does **not** govern crawling: Google reads `robots.txt` only at the host root. To control robots for a `github.io` project site, manage the user site/host root or use a custom domain. The included file is effective only if served at the host root.

Official deployment reference: [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). Current Google/Apple references are in `verification/official-guidance.md`.

## Content and assets

Edit `content.json` for translated navigation, headings, story descriptions and product wording. Edit `privacy-support.json` for the source-verified privacy/support text. `scripts/build.py` generates eleven static entry/page files; Python 3.9 or newer is sufficient. The site still works if the source scripts are absent.

`assets/asset-provenance.json` records the accepted native screenshots, original character inputs and their hashes. Shipped assets are optimized copies. The complete landscape capture is preserved with proportional sizing; foreground screenshots use a subtle rounded presentation clip with the approved soft shadow and no border or device frame. Raw landscape image files remain unchanged. The approved forest illustration is marketing artwork. Every app capture came from the simulator, rather than physical-device testing.

The first three books are Little Red Riding Hood, The Tortoise and the Hare, and The Three Little Pigs. The one-time full-library entitlement covers the additional seven and future completed books added to Oonmoon. No price is announced. The Duo wording describes design intent and selected simulator work; fold transitions, Split View and physical Duo remain unverified.

`scripts/prepare-assets.cjs` and `prepare-social.cjs` are optional asset-production tools for this Mac environment. They reference approved local source files and the installed `sharp` library; regeneration is not needed for hosting or ordinary content edits. Never regenerate app screenshots or characters with imagegen.

## Verification

`verification/verification-report.md` summarizes the completed checks and open decisions. Browser evidence and native PNG previews are in `verification/`. The development-only `scripts/verify.cjs` uses the installed Playwright and headless Chrome on this Mac. It is not sent to visitors as a dependency.

Artwork/content rights, policy approval and the final address remain owner publication decisions. No legal, sleep, learning or Apple certification guarantee is made.
