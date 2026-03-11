/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                background: '#0a0a0a',
                card: '#111827',
                primary: '#2563EB',
                accent: '#38BDF8',
            },
            boxShadow: {
                'glow': '0 0 15px rgba(56, 189, 248, 0.4)',
            }
        },
    },
    plugins: [],
}
