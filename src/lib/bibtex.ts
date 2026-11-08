/**
 * Re-indents a BibTeX entry for display: one field per line, 4-space indent,
 * "=" signs aligned. Field values are kept exactly as written.
 * If the entry cannot be parsed, it is returned unchanged.
 */
export function formatBibtex(raw: string): string {
  const src = raw.trim();
  const head = src.match(/^@(\w+)\s*\{\s*([^,\s]*)\s*,/);
  if (!head) return raw.trimEnd();
  let i = head[0].length;
  const fields: [string, string][] = [];
  const n = src.length;
  const skip = () => { while (i < n && /[\s,]/.test(src[i])) i++; };
  while (true) {
    skip();
    if (i >= n || src[i] === '}') break;
    const name = src.slice(i).match(/^([\w-]+)\s*=\s*/);
    if (!name) return raw.trimEnd();
    i += name[0].length;
    const start = i;
    if (src[i] === '{') {
      let depth = 0;
      for (; i < n; i++) {
        if (src[i] === '{') depth++;
        else if (src[i] === '}' && --depth === 0) { i++; break; }
      }
    } else if (src[i] === '"') {
      i++;
      while (i < n && !(src[i] === '"' && src[i - 1] !== '\\')) i++;
      i++;
    } else {
      while (i < n && src[i] !== ',' && src[i] !== '}' && src[i] !== '\n') i++;
    }
    fields.push([name[1], src.slice(start, i).trim()]);
  }
  if (!fields.length) return raw.trimEnd();
  const w = Math.max(...fields.map(([k]) => k.length));
  const body = fields.map(([k, v]) => `    ${k.padEnd(w)} = ${v}`).join(',\n');
  return `@${head[1]}{${head[2]},\n${body}\n}`;
}
