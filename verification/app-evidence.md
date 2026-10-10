# Oonmoon website source evidence

Read-only audit on 2026-10-10 of `/Users/ponddmini/Desktop/Oonmoon`, clean `main`, HEAD `59cdeb7`. No app files changed, builds launched, simulator state changed, or captures interrupted. Current Xcode settings identify 0.7.8 (36), e.g. `Oonmoon.xcodeproj/project.pbxproj:378,399`.

## Verified catalog

Use current native labels in `Components/BookcaseLayout.swift:377–403`, rather than old availability fields in `Documentation/TenStoryCoversManifest.json`. Current catalog uses all ten runtimes (`BookcaseLayout.swift:329–350`).

| Order / ID | English | Thai | Cover asset |
| --- | --- | --- | --- |
| 1 / red | Little Red Riding Hood | หนูน้อยหมวกแดง | StoryCover01Red |
| 2 / golden | The Tortoise and the Hare | เต่าและกระต่าย | StoryCover02TortoiseHare |
| 3 / pigs | The Three Little Pigs | หมูน้อยสามตัว | StoryCover03ThreePigs |
| 4 / duckling | The Ugly Duckling | ลูกเป็ดขี้เหร่ | StoryCover04Duckling |
| 5 / goldilocks | Goldilocks and the Three Bears | โกลดิล็อกส์กับหมีสามตัว | StoryCover05Goldilocks |
| 6 / lionMouse | The Lion and the Mouse | ราชสีห์กับหนู | StoryCover06LionMouse |
| 7 / redHen | The Little Red Hen | แม่ไก่สีแดง | StoryCover07RedHen |
| 8 / billyGoats | The Three Billy Goats Gruff | แพะสามตัวผู้กล้าหาญ | StoryCover08BillyGoats |
| 9 / elves | The Elves and the Shoemaker | เอลฟ์กับช่างทำรองเท้า | StoryCover09Elves |
| 10 / gingerbread | The Gingerbread Man | มนุษย์ขนมปังขิง | StoryCover10Gingerbread |

Each cover is in `Oonmoon/Assets.xcassets/<asset>.imageset/`; filenames and checksums are in `Documentation/TenStoryCoversManifest.json`. Original cover ratio is 1024×1536 (2:3), no cropping. Cover mappings also appear in `Components/BookcaseLayout.swift:354–366`.

## Product wording supported by source

- Ten completed English/Thai stories; native landscape iPhone/iPad reader; separate paper-cut scene layers: `README.md:5`.
- Little Red Riding Hood, The Tortoise and the Hare, and The Three Little Pigs are included: `Components/LibraryAccessPolicy.swift:16–20`. The other seven require verified full-library ownership.
- One-time non-consumable full-library unlock includes remaining completed stories and future completed stories added to Oonmoon: `LibraryAccessPolicy.swift:16–31`, `Components/FullLibraryStore.swift:18–23`. No subscription. Do not invent a production price; the actual app reads `Product.displayPrice` (`Components/FullLibraryPurchaseView.swift:62–94`).
- Bilingual app offer text: “The first three stories are included. A one-time purchase unlocks all the remaining stories and every future story added to Oonmoon.” / “นิทานสามเรื่องแรกอ่านได้เลย ซื้อเพียงครั้งเดียวเพื่อปลดล็อกนิทานที่เหลือทั้งหมด รวมถึงนิทานใหม่ทุกเรื่องที่จะเพิ่มในอุ่นมูน” (`FullLibraryPurchaseView.swift:68–75`).
- English Gabby and Thai Siriporn are bundled recordings. All ten readers have captions, finite tap interactions, and optional Auto turn driven by successful native narration completion: `README.md:15`, `Documentation/ElevenLabs-Narration-0.7.6.md:24`, `Oonmoon/PaperStoryReaderView.swift:8,321,407`. Use “recorded narration in Thai and English” rather than live AI narration or on-demand voice generation. No new TTS call happens during reading.
- Character selection is real, but do not imply every story inserts the child's personal name into its narration. Red/Golden use generic Child/Boy/Girl references (`Components/CharacterStoryCopy.swift:3–59`); fixed fictional story casts remain fixed (`Components/PaperStoryRuntime.swift:229,429–444`). Name previews are unavailable and bundled narrator previews ignore supplied personal names (`Components/VoiceEngine.swift:620–640`). Appropriate concise wording: “Choose a character, then explore stories together.” / “เลือกตัวละคร แล้วเปิดโลกนิทานไปด้วยกัน”.
- Purchase and Restore Purchases controls are behind the grown-ups parental gate: `README.md:11`, `Components/FullLibraryPurchaseView.swift:4`, `Components/FullLibraryStore.swift:264–273`. Restore may request Apple Account authentication. Deleting local choices does not erase Apple purchase history.
- Coming-soon website status is required by the user until a real listing exists. Do not confuse that whole-app launch status with historical “Coming Soon” labels in old app checkpoint files.

## App privacy facts and limits

- No developer collection or tracking implementation found in current app audit; manifest sets tracking false with empty tracking domains and collected-data types: `Documentation/Privacy-Release-Readiness-0.7.8.md:3`, `Oonmoon/PrivacyInfo.xcprivacy:5–10`.
- Character name and appearance preferences, selected reading language and first-story completion are stored in app-owned `UserDefaults`: `Oonmoon/Models.swift:98–142`. Current app wording says no accounts, advertisements or photo uploads (`Models.swift:162–171`).
- Local bookmarks: `Components/ReadingProgress.swift:7–34`, `Components/TortoiseHareReadingProgress.swift:7–31`, `Components/PaperStoryReadingProgress.swift:7–33`. Sound choices persist locally (`Components/VoiceEngine.swift:612–617`).
- Grown-ups can delete saved character/local choices and bookmarks: `Oonmoon/OonmoonApp.swift:809–833`. Do not promise deletion of Apple purchase records, device backups or external support emails; this action does not delete them.
- Narration is bundled and played by native local audio (`Components/VoiceEngine.swift:709–739`), with no backend inference or provider request triggered by reading (`VoiceEngine.swift:609–610`). Historical provider provenance is not current runtime transmission of child names or reading activity.
- StoreKit can communicate with Apple for product metadata, purchase, restore, ownership/refund updates: `FullLibraryStore.swift:169–184,241–246,264–295`. StoreKit's signed cache is the only persisted ownership record (`FullLibraryStore.swift:18–19`). No developer payment-details collection implementation was found. Avoid promising “completely offline” because purchase/restore and storefront availability require Apple services.
- Privacy manifest declares app-owned UserDefaults reason CA92.1 and system uptime for elapsed intervals reason 35F9.1 (`PrivacyInfo.xcprivacy:13–27`). These technical declarations are not an owner legal approval or an App Store Connect attestation.
- This app evidence cannot establish GitHub Pages request logging, provider cookies, email retention or legal roles. Keep app privacy and website hosting separate. The website may describe only the implemented language preference storage and no implemented analytics; do not claim the hosting provider never processes visitor data.
- Owner legal operator/controller, effective date, applicable markets and final privacy-content approval remain unresolved (`Documentation/Privacy-Release-Readiness-0.7.8.md:7–11`). Public contact `pondd.me@gmail.com` is explicitly approved by the user and can replace the earlier unresolved privacy contact; other owner details still need approval. No current approved policy URL is configured (`Config/Oonmoon-Info.plist`, `Components/AppPrivacyPolicy.swift:3–6`).

## Reusable artwork inspection

Asset root: `/Users/ponddmini/Desktop/Oonmoon/Oonmoon/Assets.xcassets/`. Actual pixels inspected via `view_image`:

- `WoodlandBackground.imageset/forest-background.png`: warm sunset forest path/cottage, no campfire or night moon.
- `WoodlandCanopy.imageset/forest-canopy.png`: transparent foliage in upper corners.
- `GoldenFinal_bg_oak_finish_evening.imageset/bg_oak_finish_evening.png`: sunset oak clearing.
- `StoryBookshelfWide.imageset/bookshelf-wide.png`: warm empty paper shelf.
- Complete source characters: `StoryGrandma.imageset/grandma.png`, `GoldenTortoiseStandingRight.imageset/tortoise_standing_right.png`, `PigsPigPip.imageset/PigsPigPip.png`, `DucklingSwanAdult.imageset/DucklingSwanAdult.png`, `GoldilocksActorStanding.imageset/GoldilocksActorStanding.png`, `LionMouseMouseStanding.imageset/LionMouseMouseStanding.png`, `RedHenRubyStanding.imageset/RedHenRubyStanding.png`, `BillyGoatsLittleStanding.imageset/BillyGoatsLittleStanding.png`, `ElvesTealDressed.imageset/ElvesTealDressed.png`, `GingerbreadWaiting.imageset/GingerbreadWaiting.png`.
- Preserve true RGBA alpha. Some source RGB contains a preview glow that must be invisible where alpha is zero. `Documentation/StoryArtSourceManifest.json:426` explicitly requires standard alpha compositing, no flattening onto black, no raw nonzero fringe used for sizing. PNG alpha presence also checked with `sips`.
- Parent has now supplied approved worker camp/moon artwork and Character-Camp-Revision02/Inventory.json. Prefer those final website assets over reconstructing this older app art; no new imagegen is necessary.

## Duo wording limits

Use the user's approved phrase “Designed with iPhone Duo in mind”. Source 0.7.8 has owning-window, safe-area and reserved-division code (`Components/BookcaseLayout.swift:418–599`); this is not Apple certification or verified physical-device support. Retained 0.7.7 continuation confirms one observed 678×466 landscape window and background/explicit-resume cases, with opposite-orientation assertion failure, fold/partial-fold/portrait-inner-window/Split View tests blocked and no physical Duo test (`Documentation/Duo-Compatibility-0.7.7.md:5–15`). Parent's worker report should control any newer exact 0.7.8 test statement. Do not imply all fold transitions, physical hardware, or uninterrupted fold playback are verified.
