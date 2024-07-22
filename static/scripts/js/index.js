window.sr = ScrollReveal();

// ANIMATIONS WITH USER SCROLL
sr.reveal('.w_content', {
    duration: 1500,
    origin: 'bottom',
    reset: 'true'
});

sr.reveal('.cards-container', {
    duration: 2000,

    origin: 'bottom',
    distance: '-20px',
});

sr.reveal('.longest-cards-space', {
    duration: 2000,
    origin: 'bottom',
    distance: '-20px',
});

sr.reveal('.color-palette', {
    duration: 2000,
    delay: 200,
    origin: 'bottom',
    distance: '-20px',
});