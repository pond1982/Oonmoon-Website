#!/usr/bin/env node
/**
 * Optional asset regeneration. The finished site requires no Node dependency.
 * This script requires the local approved source assets recorded below, which
 * may not exist on a different computer. Keep shipped assets when unavailable.
 * Run with Node + sharp; OONMOON_SHARP_MODULE can override the module path.
 */
'use strict';
const fs = require('node:fs/promises');
const path = require('node:path');
const crypto = require('node:crypto');
let sharp;
try { sharp = require('sharp'); } catch (_) {
  sharp = require(process.env.OONMOON_SHARP_MODULE || '/Applications/ChatGPT.app/Contents/Resources/cua_node/lib/node_modules/sharp');
}
const stage = path.resolve(__dirname, '..');
const assets = path.join(stage, 'assets');
const sourceRoot = '/Users/ponddmini/Documents/Codex/2026-10-09/task';
const captures = path.join(sourceRoot, 'Final-Marketing-0.7.8-Campout-Sets-20261010');
const characterInventoryPath = path.join(sourceRoot, 'Marketing-0.7.8-Disney-Five-Panel-Proof-01/Character-Camp-Revision02/Inventory.json');
const backgroundPath = path.join(sourceRoot, 'Marketing-0.7.8-Disney-Five-Panel-Proof-01/Forest-Camp-Moon-Imagegen-02.png');
const iconPath = '/Users/ponddmini/Desktop/Oonmoon/Assets/IconMaster/WindowToDreams-Approved-v1.png';
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
async function fileDetails(file) {
  const bytes = await fs.readFile(file);
  const meta = await sharp(bytes).metadata();
  return { path: file, sha256: hash(bytes), bytes: bytes.length, width: meta.width, height: meta.height, format: meta.format, alpha: meta.hasAlpha };
}
async function main() {
  await fs.mkdir(assets, { recursive: true });
  const inventory = JSON.parse(await fs.readFile(characterInventoryPath, 'utf8'));
  const provenance = {
    schema: 'oonmoon-website-asset-provenance-v1',
    generatedUTC: new Date().toISOString(),
    appRevision: '59cdeb720555f65acb6b98428f14c186015e74b7',
    appVersion: '0.7.8 (36)',
    changesToAppSourceOrAssets: 0,
    notes: [
      'All screenshots are accepted native iOS Simulator captures, not physical-device or Duo evidence.',
      'Screenshot resizing preserves the complete landscape image; no crop, rotation, redraw, device frame, or stretch.',
      'Character cutouts preserve the complete original source canvas and alpha; uniform resize only.',
      'The existing forest illustration is marketing artwork, not an app screenshot.',
      'Regeneration is optional and requires the original local sources; shipped assets work independently.'
    ],
    characterInventory: await fileDetailsMetadata(characterInventoryPath),
    assets: []
  };
  async function output(sourcePath, filename, pipeline, transform, expectedHash, extra = {}) {
    const source = await fileDetails(sourcePath);
    if (expectedHash && source.sha256 !== expectedHash) throw new Error('Approved source hash mismatch: ' + sourcePath);
    const dest = path.join(assets, filename);
    await pipeline(sharp(sourcePath)).toFile(dest);
    const result = await fileDetails(dest);
    if (Math.abs(result.height - result.width * source.height / source.width) > 1) throw new Error('Aspect ratio changed: ' + filename);
    if (transform.format === 'png' && source.alpha && !result.alpha) throw new Error('Alpha removed: ' + filename);
    provenance.assets.push({ filename, source, output: { ...result, path: 'assets/' + filename }, transform, ...extra });
  }
  const slots = [
    ['shelf-en', '01-Shelf-EN'],
    ['dressing-girl-en', '02-Dressing-Girl-EN'],
    ['dressing-boy-en', '03-Dressing-Boy-EN'],
    ['reader-en', '04-Red-EN'],
    ['reader-th', '05-Red-TH'],
    ['library-en', '06-Child-Library-Preview-EN'],
    ['library-th', '07-Child-Library-Preview-TH']
  ];
  for (const family of ['iPhone', 'iPad13']) {
    const manifestPath = path.join(captures, family, 'Native-Input-Rows.json');
    const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf8'));
    for (const [stem, slot] of (family === 'iPhone' ? slots : [slots[0]])) {
      const row = manifest.captures.find(row => row.slot === slot);
      if (!row || !row.path.endsWith('-ImageIO.png') || !row.path.includes('/Screen02/Normalized/')) throw new Error('Unapproved screenshot path: ' + slot);
      for (const width of [800, 1600]) {
        const name = family === 'iPhone' ? stem : 'shelf-ipad-en';
        await output(row.path, `${name}-${width}.jpg`, img => img.resize({ width, withoutEnlargement: true }).jpeg({ quality: 85, mozjpeg: true, chromaSubsampling: '4:4:4' }),
          { operation: 'proportional-resize', width, format: 'jpeg', quality: 85, chromaSubsampling: '4:4:4', crop: false }, row.sha256,
          { kind: 'native-simulator-screenshot', family, slot, approvedManifestPath: manifestPath, approvedManifestSHA256: (await fileDetailsMetadata(manifestPath)).sha256 });
      }
    }
  }
  for (const [filename, width] of [['forest.jpg', 1902], ['forest-small.jpg', 1000]]) {
    await output(backgroundPath, filename, img => img.resize({ width, withoutEnlargement: true }).jpeg({ quality: 87, mozjpeg: true }),
      { operation: 'proportional-resize', width, format: 'jpeg', quality: 87, crop: false }, null, { kind: 'approved-existing-marketing-illustration' });
  }
  const companions = { GoldenFinal_hare_upright_right: 'golden-hare', LionMouseMouseStanding: 'lionMouse-mouse', ElvesShoemakerStanding: 'elves-shoemaker' };
  for (const character of inventory.assets) {
    const stem = character.role === 'primary' ? character.bookID + '-primary' : companions[character.assetID];
    if (!stem) throw new Error('Unmapped character: ' + character.assetID);
    await output(character.pngPath, stem + '.png', img => img.resize({ width: 320, withoutEnlargement: true }).png({ compressionLevel: 9 }),
      { operation: 'proportional-resize-full-canvas', width: 320, format: 'png', alphaPreserved: true, crop: false }, character.sha256,
      { kind: 'original-character-cutout', bookID: character.bookID, assetID: character.assetID, role: character.role, sourceKind: character.sourceKind });
  }
  await output(iconPath, 'favicon.png', img => img.resize({ width: 128, withoutEnlargement: true }).png({ compressionLevel: 9 }),
    { operation: 'proportional-resize', width: 128, format: 'png', crop: false }, null, { kind: 'approved-app-icon' });
  provenance.summary = {
    imageFiles: provenance.assets.length,
    combinedImageBytes: provenance.assets.reduce((total, asset) => total + asset.output.bytes, 0),
    nativeScreenshotFiles: provenance.assets.filter(asset => asset.kind === 'native-simulator-screenshot').length,
    originalCharacterFiles: provenance.assets.filter(asset => asset.kind === 'original-character-cutout').length,
    sourceHashesMatchedApprovedPins: true,
    proportionalSizingVerified: true,
    alphaPreservationVerified: true
  };
  await fs.writeFile(path.join(assets, 'asset-provenance.json'), JSON.stringify(provenance, null, 2) + '\n');
  console.log(JSON.stringify({ ...provenance.summary, filenames: provenance.assets.map(asset => asset.filename) }, null, 2));
}
async function fileDetailsMetadata(file) {
  const bytes = await fs.readFile(file);
  return { path: file, sha256: hash(bytes), bytes: bytes.length };
}
main().catch(error => { console.error(error.message); process.exitCode = 1; });
