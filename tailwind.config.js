const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
    content: ["*.{html,js}"],
    theme: {
        extend: {
            colors: {
                "orange-base": "#F06C00",
                "orange-dark": "#E55000",
                "plum-light": "#B1065C",
                "plum-base": "#7F0442",
                "plum-dark": "#4F0229",
                "sale-base": "#D50000",
                "new-base": "#1976D2",
            },
            fontFamily: {
                sans: ["Inter var", ...defaultTheme.fontFamily.sans],
            },
        },
    },
    plugins: [require("@tailwindcss/forms")],
};
