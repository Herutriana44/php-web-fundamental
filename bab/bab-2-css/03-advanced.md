# Bab 2: CSS Advanced — Selectors, Animations, Grid, Flexbox Mastery

Setelah menguasai CSS dasar, langkah berikutnya adalah memahami advanced selectors, animations, dan layout modern (Grid dan Flexbox lanjutan).

## 1. Advanced CSS Selectors

### Combinator Selectors
```css
/* Descendant: semua p di dalam div (direct child atau nested) */
div p { }

/* Child: hanya p yang direct child dari div */
div > p { }

/* Adjacent sibling: p yang langsung setelah h2 */
h2 + p { }

/* General sibling: semua p yang sibling dengan h2 */
h2 ~ p { }
```

### Pseudo-class Selectors
```css
/* Structural pseudo-classes */
li:first-child { }     /* li pertama dalam parent */
li:last-child { }      /* li terakhir */
li:nth-child(2) { }    /* li urutan ke-2 */
li:nth-child(odd) { }  /* li urutan ganjil */
li:nth-child(3n+1) { } /* li urutan 1, 4, 7, 10... */

/* State pseudo-classes */
a:visited { }    /* link yang sudah diklik */
input:focus { }  /* input sedang active */
button:hover { } /* saat mouse over */
button:active { }/* saat tombol ditekan */

/* Form pseudo-classes */
input:valid { }      /* input yang valid */
input:invalid { }    /* input yang invalid */
input:disabled { }   /* input yang disabled */
input:checked { }    /* checkbox/radio yang checked */
```

### Pseudo-element Selectors
```css
/* Before & After (berguna untuk dekorasi) */
p::before {
    content: ">> ";
    color: red;
}

p::after {
    content: " ✓";
    color: green;
}

/* First letter & First line */
p::first-letter {
    font-size: 2em;
    font-weight: bold;
}

p::first-line {
    text-transform: uppercase;
}

/* Selection (warna saat text di-select) */
::selection {
    background: yellow;
    color: black;
}
```

### Attribute Selectors
```css
/* Exact match */
input[type="text"] { }

/* Attribute contains substring */
a[href*="example"] { }    /* href contain "example" */

/* Attribute starts with */
a[href^="https"] { }      /* href starts with "https" */

/* Attribute ends with */
img[src$=".png"] { }      /* src ends with ".png" */

/* Attribute contains word */
div[class~="highlight"] { } /* class contain "highlight" */

/* Attribute with dash (untuk bahasa) */
html[lang|="en"] { }      /* lang="en" atau lang="en-US" */
```

## 2. CSS Grid Layout

### Basic Grid
```css
.container {
    display: grid;
    grid-template-columns: 200px 1fr 200px;  /* 3 kolom */
    grid-template-rows: auto 1fr auto;       /* 3 baris */
    gap: 20px;  /* jarak antar grid items */
}

.header {
    grid-column: 1 / -1;  /* span semua kolom */
    grid-row: 1;
}

.sidebar {
    grid-column: 1;
    grid-row: 2;
}

.main {
    grid-column: 2;
    grid-row: 2;
}
```

### Grid Template Areas (lebih readable)
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-areas:
        "header header header"
        "sidebar main ads"
        "footer footer footer";
    gap: 20px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.ads { grid-area: ads; }
.footer { grid-area: footer; }
```

### Responsive Grid (Auto-fit & Auto-fill)
```css
/* Otomatis buat kolom sesuai space yang tersedia */
.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

/* auto-fit: collapse empty tracks */
/* auto-fill: keep empty tracks */
```

## 3. Animations & Transitions

### Transitions (perubahan smooth)
```css
.box {
    background: blue;
    width: 100px;
    transition: all 0.3s ease;  /* semua properties, 0.3s, easing ease */
}

.box:hover {
    background: red;
    width: 200px;
}

/* Specific properties */
.box {
    transition: background 0.2s ease, width 0.5s ease-out;
}

/* Easing functions: ease, ease-in, ease-out, ease-in-out, linear */
```

### Keyframe Animations
```css
@keyframes slideIn {
    0% {
        transform: translateX(-100%);
        opacity: 0;
    }
    50% {
        opacity: 0.5;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

.banner {
    animation: slideIn 1s ease-out;
    /* animation-name duration timing-function delay iteration-count direction fill-mode */
}

.banner {
    animation: slideIn 2s ease-out 0.5s infinite reverse;
}
```

### Transform (transformasi 2D & 3D)
```css
.box {
    /* 2D Transforms */
    transform: translateX(50px);      /* geser horizontal */
    transform: translateY(-20px);     /* geser vertical */
    transform: scale(1.5);            /* perbesar */
    transform: rotate(45deg);         /* putar */
    transform: skew(10deg, 20deg);    /* condong */

    /* Multiple transforms */
    transform: translate(50px, 20px) scale(1.2) rotate(5deg);
}

.box:hover {
    transform: scale(1.1) translateY(-10px);
}
```

## 4. Flexbox Advanced

### Flex Properties
```css
.container {
    display: flex;
    justify-content: space-between;  /* horizontal spacing */
    align-items: center;             /* vertical alignment */
    gap: 15px;
}

.item {
    flex: 1;           /* grow equally */
    flex: 1 1 200px;   /* grow shrink basis */
    flex-grow: 2;      /* grow 2x lebih besar */
    flex-shrink: 0;    /* don't shrink */
    flex-basis: 200px; /* minimum width */
}

/* Align self untuk satu item */
.item:last-child {
    align-self: flex-end;
}
```

### Flex Wrap & Direction
```css
.container {
    flex-wrap: wrap;       /* items wrap ke baris baru */
    flex-direction: column; /* vertical layout */
    flex-direction: row-reverse; /* reverse order */
}
```

## 5. CSS Performance Tips

### Will-change (notify browser)
```css
.animated-element {
    will-change: transform, opacity;
}

/* Use sparingly — can impact performance if overused */
```

### GPU Acceleration
```css
.smooth-scroll {
    transform: translate3d(0, 0, 0);  /* trigger GPU acceleration */
}
```

### Avoid Performance Killers
```css
/* ✗ Expensive: repaint setiap frame */
.box {
    animation: moveBox 1s infinite;
}

@keyframes moveBox {
    0% { left: 0; }      /* triggers layout recalc */
    100% { left: 300px; } /* avoid left/right/top/bottom */
}

/* ✓ Better: use transform (GPU accelerated) */
@keyframes moveBox {
    0% { transform: translateX(0); }
    100% { transform: translateX(300px); }
}
```

## 6. Best Practices

- **Mobile-first**: design untuk mobile dulu, grow ke desktop
- **Accessibility**: pastikan animations tidak aggressive (prefers-reduced-motion)
- **Performance**: gunakan transform & opacity untuk animations
- **Semantics**: struktur HTML dulu, styling dengan CSS
- **Testing**: test di berbagai devices & browsers
