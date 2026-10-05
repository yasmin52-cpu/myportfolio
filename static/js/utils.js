/**
 * Helper bersama untuk halaman yang memakai AJAX (Experience, Projects).
 */

// Semua teks dari server HARUS di-escape sebelum masuk innerHTML,
// supaya payload seperti <img onerror=...> tampil sebagai teks biasa (anti-XSS).
function escapeHtml(value) {
    return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
}

// Mengambil token CSRF dari cookie; dikirim lewat header X-CSRFToken pada POST AJAX.
function getCookie(name) {
    const prefix = `${name}=`;
    const match = document.cookie
        .split(';')
        .map(cookie => cookie.trim())
        .find(cookie => cookie.startsWith(prefix));
    return match ? decodeURIComponent(match.substring(prefix.length)) : null;
}

// Mengubah response error JSON Django ({errors: {field: [{message}]}} atau {message})
// menjadi satu string yang menyebutkan field bermasalah.
function formatErrorMessages(result, fallbackMessage) {
    if (result && result.errors) {
        return Object.entries(result.errors)
            .map(([field, errors]) => `${field}: ${errors.map(error => error.message).join(' ')}`)
            .join(' | ');
    }
    return (result && result.message) || fallbackMessage;
}
