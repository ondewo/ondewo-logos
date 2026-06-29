export const meta = {
  name: 'brand-audit',
  description: 'Audit many files (or a repo of marketing/web assets) against the ONDEWO brand guidelines in parallel and produce a consolidated compliance report.',
  whenToUse: 'When the user wants a brand QA sweep across a folder, a website, or a set of assets before a release.',
  phases: [
    { title: 'Discover', detail: 'List candidate assets to audit' },
    { title: 'Audit', detail: 'Brand-check each asset in parallel' },
    { title: 'Report', detail: 'Synthesise a prioritised report' },
  ],
};

// args: { files?: string[], glob?: string }
const CHECK_SCHEMA = {
  type: 'object',
  required: ['file', 'verdict', 'issues'],
  properties: {
    file:    { type: 'string' },
    verdict: { type: 'string', enum: ['on-brand', 'minor-issues', 'off-brand'] },
    issues:  {
      type: 'array',
      items: {
        type: 'object',
        required: ['severity', 'dimension', 'problem', 'fix'],
        properties: {
          severity:  { type: 'string', enum: ['high', 'medium', 'low'] },
          dimension: { type: 'string' },
          problem:   { type: 'string' },
          fix:       { type: 'string' },
        },
      },
    },
  },
};

phase('Discover');
let files = (args && args.files) || [];
if (!files.length) {
  const glob = (args && args.glob) || 'svg/html/css/md design or marketing files';
  const found = await agent(
    `List the files in this repo that are design/marketing/brand-facing assets to audit ` +
    `(${glob}): SVG, HTML, CSS, MD with branding, images. Exclude node_modules, .git, and the ` +
    `brand-kit/ source-of-truth files themselves. Return a JSON array of repo-relative paths.`,
    { phase: 'Discover', schema: { type: 'object', required: ['files'], properties: { files: { type: 'array', items: { type: 'string' } } } } }
  );
  files = (found && found.files) || [];
}
log(`Auditing ${files.length} asset(s)`);

phase('Audit');
const reports = (await parallel(
  files.map(f => () => agent(
    `Invoke the brand-check skill on "${f}". Compare against brand-kit guidelines ` +
    `(colour, logo, typography, layout, accessibility, voice). Return file, verdict, and a ` +
    `list of issues each with severity/dimension/problem/fix.`,
    { label: `audit:${f}`, phase: 'Audit', schema: CHECK_SCHEMA }
  ))
)).filter(Boolean);

phase('Report');
const counts = reports.reduce((a, r) => (a[r.verdict] = (a[r.verdict] || 0) + 1, a), {});
const highs = reports.flatMap(r => (r.issues || []).filter(i => i.severity === 'high').map(i => ({ file: r.file, ...i })));
log(`Audit complete — on-brand:${counts['on-brand']||0} minor:${counts['minor-issues']||0} off-brand:${counts['off-brand']||0}; ${highs.length} high-severity issues`);

return {
  audited: reports.length,
  counts,
  highSeverity: highs,
  reports,
};
