/**
 * ONDEWO Tailwind CSS preset.
 * Generated from ondewo.tokens.json (canonical source).
 *
 * Usage (tailwind.config.js):
 *   const ondewo = require("./brand-kit/tokens/tailwind.preset.js");
 *   module.exports = { presets: [ondewo], content: [...] };
 *
 * Then: class="bg-ondewo-blue text-white font-display"
 */
module.exports = {
  theme: {
    extend: {
      colors: {
        ondewo: {
          blue: "#004C87",
          magenta: "#BE216B",
          ink: "#231F20",
        },
        blue: {
          50: "#EBF1F5", 100: "#D6E2EC", 200: "#A8C2D6", 300: "#739DBD", 400: "#3873A1",
          500: "#004C87", 600: "#004071", 700: "#00345C", 800: "#002644", 900: "#001A2E",
        },
        magenta: {
          50: "#FAEDF3", 100: "#F5DBE7", 200: "#E9B4CD", 300: "#DB85AE", 400: "#CC528C",
          500: "#BE216B", 600: "#A01C5A", 700: "#811649", 800: "#5F1036", 900: "#410B24",
        },
        neutral: {
          0: "#FFFFFF", 50: "#F7F8FA", 100: "#E5E4E6", 200: "#C7C5C9", 300: "#A4A2A8",
          400: "#7E7A83", 500: "#5A5560", 600: "#4C4751", 700: "#3D3A41", 800: "#2D2A30", 900: "#231F20",
        },
        success: "#1E7A4B",
        warning: "#B5710A",
        error: "#C02626",
      },
      fontFamily: {
        display: ["Futura PT", "Futura LT Pro", "Futura", "Jost", "Century Gothic", "Trebuchet MS", "system-ui", "sans-serif"],
        body: ["Futura PT", "Jost", "Century Gothic", "system-ui", "-apple-system", "Segoe UI", "Roboto", "sans-serif"],
        mono: ["JetBrains Mono", "SFMono-Regular", "Cascadia Code", "Consolas", "monospace"],
      },
      fontSize: {
        xs: "0.75rem", sm: "0.875rem", base: "1rem", lg: "1.25rem", xl: "1.5625rem",
        "2xl": "1.9375rem", "3xl": "2.4375rem", "4xl": "3.0625rem", "5xl": "3.8125rem",
      },
      letterSpacing: { tight: "-0.01em", normal: "0", wide: "0.04em", wider: "0.12em" },
      borderRadius: { sm: "0.25rem", md: "0.5rem", lg: "1rem", xl: "1.5rem", pill: "9999px" },
      boxShadow: {
        sm: "0 1px 2px rgba(0,38,68,0.08)",
        md: "0 4px 12px rgba(0,38,68,0.10)",
        lg: "0 12px 32px rgba(0,38,68,0.14)",
      },
      backgroundImage: {
        "ondewo-brand": "linear-gradient(135deg, #BE216B 0%, #004C87 100%)",
        "ondewo-brand-subtle": "linear-gradient(135deg, #FAEDF3 0%, #EBF1F5 100%)",
        "ondewo-blue-deep": "linear-gradient(160deg, #004C87 0%, #001A2E 100%)",
      },
    },
  },
};
