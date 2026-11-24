export const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
export const u = (p: string) => (p.startsWith('#') ? p : `${BASE}/${p.replace(/^\//, '')}`);
export const TEL = 'tel:+41788660426';
export const TEL_TXT = '078\u00a0866\u00a004\u00a026';
export const TEL2 = 'tel:+41766790873';
export const TEL2_TXT = '076\u00a0679\u00a008\u00a073';
export const ADDR = 'Quai Ernest-Ansermet 6, 1205 Genève';
export const EMAIL = 'service.clients@fvpeinture.ch';
export const MAILTO = `mailto:${EMAIL}`;
