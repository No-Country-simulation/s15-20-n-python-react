/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'pale-brown': "#F4CA8D",
        'darkblue' : '#0E1626',
        'blue' : '#293B5F',
        'cream' : '#F4CA8D',
        'greentag': '#EBFAE2',
        'greentexttag': '#4F9C20',
        'boardbg': '#000714',

      },
    },
  },
  plugins: [],
}
