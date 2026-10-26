export const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
export const u = (p: string) => (p.startsWith('#') ? p : `${BASE}/${p.replace(/^\//, '')}`);
export const TEL = 'tel:+41788660426';
export const TEL_TXT = '078\u00a0866\u00a004\u00a026';
