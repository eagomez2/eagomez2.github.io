// Colours for programming languages and tools on the About page.
// Add a new entry here when you add a language to site.yaml.
export const LANGUAGE_COLORS: Record<string, string> = {
  'C': '#7A7F87',
  'C++': '#F34B7D',
  'Rust': '#DEA584',
  'Python': '#3572A5',
  'PyTorch': '#EE4C2C',
  'TensorFlow': '#FF8F00',
  'ONNX': '#4F7CAC',
  'MATLAB': '#E16737',
  'JUCE': '#8DC63F',
  'Max/MSP': '#C4A79C',
};

/** Splits a comma-separated skills line. Items that themselves contain a comma are kept whole. */
const KEEP_WHOLE: string[] = [];
export function splitTags(line: string): string[] {
  let rest = line;
  const tokens: string[] = [];
  for (const k of KEEP_WHOLE) {
    if (rest.includes(k)) { rest = rest.replace(k, `\u0000${tokens.length}\u0000`); tokens.push(k); }
  }
  return rest.split(',').map((s) => s.trim()).filter(Boolean)
    .map((s) => s.replace(/\u0000(\d+)\u0000/, (_, i) => tokens[Number(i)]));
}
