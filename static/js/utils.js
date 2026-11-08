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
function formatErrorMessages(result, fallbackMessage) { // Mengubah respons error API menjadi teks yang dapat ditampilkan di toast.
    if (!result || typeof result !== 'object') { // Memeriksa apakah respons error kosong atau bukan objek.
        return fallbackMessage; // Menggunakan pesan default jika respons tidak dapat diproses.
    }

    if (result.errors) { // Memeriksa apakah respons menggunakan format error Django lama.
        return Object.entries(result.errors) // Mengubah objek errors menjadi pasangan nama field dan daftar error.
            .map(([field, errors]) => // Memproses setiap field yang mengalami kesalahan.
                `${field}: ${errors.map(error => error.message).join(' ')}` // Menggabungkan pesan error dari field tersebut.
            )
            .join(' | '); // Menggabungkan seluruh pesan error menjadi satu string.
    }

    const messages = Object.entries(result) // Mengambil pasangan field dan pesan error dari respons DRF.
        .map(([field, errors]) => { // Memproses pesan error untuk setiap field.
            const errorList = Array.isArray(errors) ? errors : [errors]; // Memastikan pesan error berbentuk array.

            return `${field}: ${errorList.map(error => // Menambahkan nama field sebelum pesan kesalahannya.
                typeof error === 'string' ? error : JSON.stringify(error) // Menggunakan string langsung atau mengubah objek menjadi teks.
            ).join(' ')}`; // Menggabungkan seluruh pesan error untuk field tersebut.
        });

    return messages.join(' | ') || fallbackMessage; // Mengembalikan seluruh pesan atau pesan default jika kosong.
}
