/* Only an explicit language choice is stored. Locale URLs never redirect. */
(() => {
  const key = 'oonmoon-language';
  const valid = language => language === 'en' || language === 'th';
  const read = () => { try { const value = localStorage.getItem(key); return valid(value) ? value : null; } catch { return null; } };
  const save = language => { try { if (valid(language)) localStorage.setItem(key, language); } catch { /* Static links remain usable. */ } };
  document.querySelectorAll('[data-language]').forEach(link => link.addEventListener('click', () => save(link.dataset.language)));
  const gateway = document.querySelector('[data-language-gateway]');
  if (!gateway) return;
  const supported = (navigator.languages || [navigator.language]).map(value => String(value || '').toLowerCase().split('-')[0]).find(valid);
  const preferred = read() || supported || 'en';
  gateway.querySelectorAll('[data-language]').forEach(link => {
    link.classList.toggle('is-preferred', link.dataset.language === preferred);
  });
  const continueLink = gateway.querySelector('[data-continue]');
  continueLink.href = preferred + '/';
  continueLink.dataset.language = preferred;
  continueLink.lang = preferred;
  continueLink.textContent = preferred === 'th' ? 'เข้าสู่เว็บไซต์ภาษาไทย →' : 'Continue in English →';
  continueLink.addEventListener('click', () => save(preferred));
  const note = gateway.querySelector('[data-preference-note]');
  note.textContent = preferred === 'th' ? 'เลือกภาษาไทยตามการตั้งค่าภาษาของคุณ เปลี่ยนภาษาได้ทุกเมื่อ' : 'English is selected from your language preference, or used as the fallback. You can switch anytime.';
  note.lang = preferred;
})();
