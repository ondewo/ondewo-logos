export const meta = {
  name: 'campaign-kit',
  description: 'Generate a full on-brand ONDEWO campaign (social post, banner, slide, landing hero, copy) from one message, then brand-check every asset.',
  whenToUse: 'When the user wants a complete set of branded assets for a launch, announcement, event, or campaign in one go.',
  phases: [
    { title: 'Brief', detail: 'Draft on-brand copy for the campaign message' },
    { title: 'Produce', detail: 'Generate each asset in parallel from templates' },
    { title: 'Brand-check', detail: 'Audit each asset against the guidelines' },
  ],
};

// args: { message: string, assets?: string[], theme?: 'light'|'brand'|'dark', outDir?: string }
const message = (args && args.message) || 'We automate your phone calls.';
const theme = (args && args.theme) || 'light';
const outDir = (args && args.outDir) || 'brand-kit/generated/campaign';
const assets = (args && args.assets) || ['social-post', 'linkedin-banner', 'slide', 'landing-hero'];

const TEMPLATE = {
  'social-post':     'brand-kit/templates/social-post-1080.svg',
  'linkedin-banner': 'brand-kit/templates/social-banner-linkedin.svg',
  'slide':           'brand-kit/templates/slide-title.svg',
  'landing-hero':    'brand-kit/templates/web-hero.html',
};

const COPY_SCHEMA = {
  type: 'object',
  required: ['eyebrow', 'headline', 'subline', 'cta'],
  properties: {
    eyebrow:  { type: 'string' },
    headline: { type: 'string' },
    subline:  { type: 'string' },
    cta:      { type: 'string' },
  },
};

const CHECK_SCHEMA = {
  type: 'object',
  required: ['verdict', 'issues'],
  properties: {
    verdict: { type: 'string', enum: ['on-brand', 'minor-issues', 'off-brand'] },
    issues:  { type: 'array', items: { type: 'string' } },
    file:    { type: 'string' },
  },
};

phase('Brief');
const copy = await agent(
  `Using the ONDEWO brand-copy skill (read brand-kit/voice-and-tone.md and brand-foundation.md), ` +
  `write campaign copy for this message: "${message}". Return an eyebrow (short, will be UPPERCASED), ` +
  `a sentence-case headline (≤7 words), a one-line subline, and a CTA (verb-first, no period). ` +
  `ONDEWO voice: clear, confident, human. Theme: ${theme}.`,
  { schema: COPY_SCHEMA, phase: 'Brief' }
);

log(`Copy ready: "${copy.headline}"`);

// Produce each asset, then brand-check it — pipelined so each check starts as soon
// as its asset is built (no barrier).
const results = await pipeline(
  assets.filter(a => TEMPLATE[a]),
  (a) => agent(
    `Invoke the create-brand-asset skill. Base template: ${TEMPLATE[a]}. ` +
    `Produce an ONDEWO ${a} using this copy: eyebrow="${copy.eyebrow}", headline="${copy.headline}", ` +
    `subline="${copy.subline}", cta="${copy.cta}". Theme: ${theme}. ` +
    `Embed the official logo from brand-kit/assets/logo, use only design tokens, keep magenta ≤10%. ` +
    `Save the result to ${outDir}/ondewo-${a}.<ext> and RENDER it to PNG to verify it looks correct. ` +
    `Return the saved file path.`,
    { label: `produce:${a}`, phase: 'Produce' }
  ),
  (savedPath, a) => agent(
    `Invoke the brand-check skill on the asset just produced for "${a}" (find it under ${outDir}). ` +
    `Report verdict and any issues with concrete fixes. Saved path info: ${savedPath}`,
    { label: `check:${a}`, phase: 'Brand-check', schema: CHECK_SCHEMA }
  ).then(v => ({ asset: a, ...v }))
);

const checked = results.filter(Boolean);
const clean = checked.filter(r => r.verdict === 'on-brand');
log(`Campaign done: ${clean.length}/${checked.length} assets on-brand, saved to ${outDir}`);

return {
  message,
  theme,
  copy,
  outDir,
  assets: checked,
  summary: `${clean.length}/${checked.length} on-brand`,
};
