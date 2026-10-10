# Rounded screenshot presentation audit

Scope: the authorized subtle rounded-corner refinement on the separate Oonmoon website. The auditor makes no Desktop or app source edits. Baseline inspected: clean outer `main` commit `b9118b6` at `/Users/ponddmini/Desktop/Oonmoon-Website`.

During review the active project appeared one level deeper at `/Users/ponddmini/Desktop/Oonmoon-Website/Oonmoon-Website`, with its own clean `main` history (`46ee847`, preceded by `66a14d1`). The implementation owner identified this as the user's active checkout and instructed preservation of both Git identities and the existing layout. Final source reads use this nested path; no flattening or history replacement was performed by the auditor.

## Source and baseline checks

- All sixteen website screenshot derivatives and their accepted native simulator source captures match the SHA-256 pins in `assets/asset-provenance.json`.
- There are nine foreground screenshot placements across the language gateway and English/Thai Home and Features pages. Each uses the shared `.app-screen img` presentation and the full landscape aspect ratio (1600×736, or its proportional 800×368 derivative).
- `border-radius: clamp(4px, 1vw, 10px)` computes to 4px at 320/390px viewport widths, 7.68px at 768px, and 10px at 1024/1440px. This changes only the painted extreme corners.
- The existing reader, shelf, and dressing pixels were inspected directly. Reading controls, captions, shelf labels and the Back control sit well beyond the proposed tiny corner wedges. Background artwork is the only visible content at the extreme corners. No meaningful-control or text clipping is expected at this radius.
- Apply radius on the screenshot `img` while retaining its existing dimensions, natural proportional sizing, link, and shadow parameters. Adding a wrapper's `overflow:hidden`, `object-fit:cover`, a new border/frame, or modified image geometry would exceed this refinement and could clip shadows or focus indicators.
- In social composition, mask only the resized screenshot buffer; preserve transparency by ensuring alpha and encoding that intermediate as PNG before compositing it over the forest. Do not mask the complete social canvas or flatten transparent corners to black.

## Completed final source and social checks

- Current source declares `.app-screen img{width:100%;border-radius:clamp(4px,1vw,10px);border:0;box-shadow:var(--shadow)}`. The shadow token remains `0 24px 48px #0005`; the image's proportional geometry and full-size links are unchanged.
- The social compositor preserves the full 545×251 screenshot, uses an 8px rounded rectangle only on that screenshot buffer, ensures alpha, writes the intermediate as PNG, and then composites it into the existing 1200×630 forest image.
- Independent in-memory mask QA passed for both English and Thai: 92 pixels have affected alpha, all confined to the four extreme 8×8 corner regions. There are zero RGBA changes outside those corner regions and zero unexpected transparency. The marketing composites remain 1200×630.
- All 32 original website derivative assets and their recorded source files still match provenance SHA-256 hashes. Raw landscape captures and shipped screenshot JPEGs are immutable in this refinement.
- Both updated social-image pixel outputs were inspected. Their reader controls, complete narration captions, and image bounds remain visible. The curves are subtle, no border/frame is added, and clipped corners reveal the surrounding forest without black flattening artifacts.

## Completed final preview check

- Fresh full-resolution desktop (1440px), mobile (390px, Thai), and tablet (768px) previews in the active nested checkout's `verification` folder were inspected. Reader and shelf screenshots show gentle corner rounding, unchanged soft shadows, and no border/frame. They retain their full landscape shape. Reading buttons, full English/Thai narration captions, shelf controls and labels remain inside the visible image bounds; no meaningful content is removed by the corner clips.
- The refreshed browser report finished at `2026-10-10T06:01:00.652Z`: 46 passing checks and zero errors. It includes all eleven routes at five viewport sizes (320, 390, 768, 1024, 1440px), with no horizontal overflow. Five added screenshot checks cover all nine foreground placements and verify the 4–10px radius, zero border, original soft shadow, and landscape proportions.
- Source/hash checks and the independent social-mask pixel checks above support the visual inspection. The older `05:46:54.450Z` report is superseded by this refreshed evidence.

**Sign-off:** the authorized rounded-corner refinement passes this independent source and visual review. No clipping, geometry, shadow, or immutable-asset blocker remains. Both Git histories and the user's nested layout were preserved; no publication or Desktop/app source edit was performed by the auditor. This review is limited to the refinement and is not formal accessibility or physical-device certification.
