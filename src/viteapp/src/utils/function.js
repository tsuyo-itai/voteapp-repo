// 暗号化文字列の復号化
import CryptoJS from 'crypto-js';

// TODO: 環境変数へ
// 暗号化キー（16バイト、32バイト、または64バイト）
const secretKey = 'mysecretkey';

// 暗号化文字列の作成
export function createSafeEncryptedText(text) {
    // 1. 文字列を暗号化
    const cipherText = CryptoJS.AES.encrypt(text, secretKey).toString();
    // 2. 暗号文をBase64エンコード
    const base64CipherText = btoa(cipherText);
    // 3. '/' を取り除く
    const safeEncryptedText = base64CipherText.replace(/\//g, '_'); // 例: '/' を '_' に置き換える

    return safeEncryptedText;
}

// 暗号化文字列の複合
export function decryptSafeEncryptedText(safeEncryptedText) {
    console.log(safeEncryptedText)
    // 1. '_' を '/' に戻す
    const base64CipherText = safeEncryptedText.replace(/_/g, '/'); // 例: '_' を '/' に戻す
    // 2. Base64デコード
    const cipherText = atob(base64CipherText);
    // 3. 暗号文を復号化
    const bytes = CryptoJS.AES.decrypt(cipherText, secretKey);
    const originalText = bytes.toString(CryptoJS.enc.Utf8);

    return originalText;
}

// URLをクリップボードにコピーする
export function copyToClipboard(copyText) {
    // クリップボードAPIを使用してテキストをクリップボードにコピー
    navigator.clipboard.writeText(copyText)
    .then(() => {
        alert("URLがクリップボードにコピーされました。");
    })
    .catch(err => {
        console.error("クリップボードへのコピーに失敗しました:", err);
        alert("URLのコピーに失敗しました。");
    });
}