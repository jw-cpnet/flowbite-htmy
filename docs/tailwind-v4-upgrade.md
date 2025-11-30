# Tailwind CSS v4 Upgrade - Flowbite Design Tokens

## Current Limitation

The showcase app uses **Tailwind CSS v3 via CDN**, which doesn't support Flowbite's new design token system introduced in Flowbite v4.

### What We're Missing

Flowbite v4 introduces semantic design tokens like:

```html
<!-- Example secondary button with design tokens -->
<button type="button" class="text-body bg-neutral-secondary-medium box-border border border-default-medium hover:bg-neutral-tertiary-medium hover:text-heading focus:ring-4 focus:ring-neutral-tertiary shadow-xs font-medium leading-5 rounded-base text-sm px-4 py-2.5 focus:outline-none">
  Secondary
</button>
```

These tokens are not available with the CDN approach.

## Available Design Tokens in Flowbite v4

### Text Colors
- `text-body`, `text-body-subtle`
- `text-heading`
- `text-fg-brand`, `text-fg-brand-subtle`, `text-fg-brand-strong`
- `text-fg-success`, `text-fg-danger`, `text-fg-warning`
- `text-fg-disabled`

### Background Colors
**Neutral:**
- `bg-neutral-primary-soft`, `bg-neutral-primary-medium`, `bg-neutral-primary-strong`
- `bg-neutral-secondary-soft`, `bg-neutral-secondary-medium`, `bg-neutral-secondary-strong`
- `bg-neutral-tertiary-soft`, `bg-neutral-tertiary-medium`

**Brand & Status:**
- `bg-brand-softer`, `bg-brand-soft`, `bg-brand-medium`, `bg-brand-strong`
- `bg-success-soft`, `bg-success-medium`, `bg-success-strong`
- `bg-danger-soft`, `bg-danger-medium`, `bg-danger-strong`
- `bg-warning-soft`, `bg-warning-medium`, `bg-warning-strong`

### Border Colors
- `border-default-subtle`, `border-default-medium`, `border-default-strong`
- `border-muted`, `border-buffer`
- `border-brand-subtle`, `border-success-subtle`, `border-danger-subtle`

## How to Upgrade

### 1. Install Dependencies

```bash
npm install tailwindcss@next flowbite
```

### 2. Configure CSS Entry Point

Create/update `input.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import "flowbite/src/themes/default";
@import "tailwindcss";
@plugin "flowbite/plugin";
@source "../node_modules/flowbite";
```

### 3. Available Themes

Flowbite v4 includes five pre-built themes:
- `flowbite/src/themes/default` (Inter font)
- `flowbite/src/themes/minimal` (Open Sans font)
- `flowbite/src/themes/enterprise` (Shantell Sans font)
- `flowbite/src/themes/playful` (Google Sans Code font)
- `flowbite/src/themes/mono`

### 4. Custom Theme Variables

Customize in `@theme` block:

```css
@theme {
  /* Text colors */
  --color-body: var(--color-stone-600);
  --color-heading: var(--color-stone-900);

  /* Brand colors */
  --color-brand: var(--color-blue-700);
  --color-brand-soft: var(--color-blue-100);

  /* Fonts */
  --font-body: 'Inter', system-ui, sans-serif;
}
```

## Impact on flowbite-htmy

Once upgraded, we could:
1. Use semantic tokens in component class mappings
2. Support theming out of the box
3. Provide better dark mode support via CSS variables

## References

- [Flowbite Theming Documentation](https://flowbite.com/docs/customize/theming/)
- [Flowbite CSS Variables](https://flowbite.com/docs/customize/variables/)
- [Tailwind CSS v4 Theme Variables](https://tailwindcss.com/docs/theme)

---

*Created: November 2024*
*Status: Pending - Currently using Tailwind v3 CDN*
